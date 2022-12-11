from collections import namedtuple

pos = namedtuple("pos", ["x", "y"])


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def get_dimensions(moves):
    x, y = 0, 0
    max_x, max_y = 0, 0
    min_x, min_y = 0, 0
    for m in moves:
        direction, count = m.split(" ")
        count = int(count)
        match direction:
            case "R":
                x += count
            case "L":
                x -= count
            case "U":
                y += count
            case "D":
                y -= count
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)
    # print(f"x range: {min_x}-{max_x} y range: {min_y}-{max_y}")
    return ((max_x - min_x) * 3, (max_y - min_y) * 3)


def print_grid(grid):
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in grid]))
    divider = "-" * 100
    print(divider)
    print()


def generate_grid(dimensions):
    grid = [["." for columns in range(dimensions[0])] for rows in range(dimensions[1])]
    return grid


def apply_moves(moves, knot_count):
    # If the head is ever two steps directly up, down, left, or right from the tail
    # the tail must also move one step in that direction so it remains close enough
    # otherwise, if the head and tail aren't touching and aren't in the same row or column
    # the tail always moves one step diagonally to keep up:

    # if T isnt on board (only H), they are overlapping
    # You just need to work out where the tail goes as the head follows a series of motions.
    # Assume the head and the tail both start at the same position, overlapping.

    head = "H"
    tail = "T"

    grid = generate_grid(get_dimensions(moves))
    tail_positions = set()

    starting_x = len(grid[0]) // 2
    starting_y = len(grid) // 2
    # head_pos = pos(starting_x, starting_y)
    # tail_pos = pos(starting_x, starting_y)
    positions = [pos(starting_x, starting_y) for _ in range(knot_count)]
    tail_positions.add((positions[-1].x, positions[-1].y))
    grid[starting_y][starting_x] = head
    # print_grid(grid)

    for m in moves:
        direction, count = m.split(" ")
        count = int(count)
        # print(f"{direction} == {count}")
        for _ in range(count):
            # move each position
            head_pos = positions[0]
            match direction:
                case "R":
                    head_pos = pos(head_pos.x + 1, head_pos.y)
                case "L":
                    head_pos = pos(head_pos.x - 1, head_pos.y)
                case "U":
                    head_pos = pos(head_pos.x, head_pos.y - 1)
                case "D":
                    head_pos = pos(head_pos.x, head_pos.y + 1)
            positions[0] = head_pos

            # after moving head, move everything else relative to it
            for i in range(len(positions) - 1):
                curr, nex = positions[i], positions[i + 1]
                # print(curr, nex)

                curr, nex = move_rope(curr, nex, direction)
                positions[i] = curr
                positions[i + 1] = nex

                # put tail first, because overlap will be an H
                grid[curr.y][curr.x] = f"{i+1}"
                grid[nex.y][nex.x] = f"{i}"

            tail_positions.add(positions[-1])

            # print_grid(grid)

    return len(tail_positions)


def move_rope(curr_pos, next_pos, direction):
    # given where head_pos is, move tail

    # if they are touching, we are good
    if curr_pos == next_pos:
        return curr_pos, next_pos
    # check right
    if curr_pos.x + 1 == next_pos.x and curr_pos.y == next_pos.y:
        return curr_pos, next_pos
    # check left
    if curr_pos.x - 1 == next_pos.x and curr_pos.y == next_pos.y:
        return curr_pos, next_pos
    # check up
    if curr_pos.x == next_pos.x and curr_pos.y - 1 == next_pos.y:
        return curr_pos, next_pos
    # check down
    if curr_pos.x == next_pos.x and curr_pos.y + 1 == next_pos.y:
        return curr_pos, next_pos
    # diag right top
    if curr_pos.x + 1 == next_pos.x and curr_pos.y - 1 == next_pos.y:
        return curr_pos, next_pos
    # diag right bot
    if curr_pos.x + 1 == next_pos.x and curr_pos.y + 1 == next_pos.y:
        return curr_pos, next_pos
    # diag left top
    if curr_pos.x - 1 == next_pos.x and curr_pos.y - 1 == next_pos.y:
        return curr_pos, next_pos
    # diag left bot
    if curr_pos.x - 1 == next_pos.x and curr_pos.y + 1 == next_pos.y:
        return curr_pos, next_pos

    # if not touching, we need to figure out where to move the tail

    # if on same x, move closer on y
    if curr_pos.x == next_pos.x:
        if curr_pos.y > next_pos.y:
            next_pos = pos(next_pos.x, next_pos.y + 1)
        else:
            next_pos = pos(next_pos.x, next_pos.y - 1)

        return curr_pos, next_pos

    # if on same y, move closer on x
    if curr_pos.y == next_pos.y:
        if curr_pos.x > next_pos.x:
            next_pos = pos(next_pos.x + 1, next_pos.y)
        else:
            next_pos = pos(next_pos.x - 1, next_pos.y)
        return curr_pos, next_pos

    # if head is above T and to right of T
    if curr_pos.x > next_pos.x and curr_pos.y < next_pos.y:
        # move diagonally top right
        next_pos = pos(next_pos.x + 1, next_pos.y - 1)
        return curr_pos, next_pos

    # if head is below T and to right of T
    # move diagonally top right
    if curr_pos[0] > next_pos[0] and curr_pos[1] > next_pos[1]:
        # move diagonally top right
        next_pos = pos(next_pos.x + 1, next_pos.y + 1)
        return curr_pos, next_pos

    if curr_pos[0] < next_pos[0] and curr_pos[1] > next_pos[1]:
        # move diagonally top right
        next_pos = pos(next_pos.x - 1, next_pos.y + 1)
        return curr_pos, next_pos

    if curr_pos[0] < next_pos[0] and curr_pos[1] < next_pos[1]:
        # move diagonally top right
        next_pos = pos(next_pos.x - 1, next_pos.y - 1)
        return curr_pos, next_pos

    return curr_pos, next_pos


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    vals = get_input("input")
    assert apply_moves(test_vals, 2) == 13
    assert apply_moves(vals, 2) == 6406

    print("# part 2------------------")
    test_vals = get_input("test_input_2")
    assert apply_moves(test_vals, 10) == 36
    assert apply_moves(vals, 10) == 2643
