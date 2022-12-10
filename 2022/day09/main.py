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
    print(f"x range: {min_x}-{max_x} y range: {min_y}-{max_y}")
    return ((max_x - min_x) * 3, (max_y - min_y) * 3)


def print_grid(grid):
    print("\n".join(["\t".join([str(cell) for cell in row]) for row in grid]))
    divider = "-" * 100
    print(divider)
    print()


def generate_grid(dimensions):
    grid = [["." for columns in range(dimensions[0])] for rows in range(dimensions[1])]
    return grid


def apply_moves(moves):
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
    head_pos = pos(starting_x, starting_y)
    tail_pos = pos(starting_x, starting_y)
    tail_positions.add((tail_pos.x, tail_pos.y))
    grid[starting_y][starting_x] = head
    # print_grid(grid)

    for m in moves:
        direction, count = m.split(" ")
        count = int(count)
        # print(f"{direction} == {count}")
        for _ in range(count):
            grid[tail_pos.y][tail_pos.x] = "."
            grid[head_pos.y][head_pos.x] = "."
            head_pos, tail_pos = move_rope(head_pos, tail_pos, direction)
            tail_positions.add((tail_pos.x, tail_pos.y))
            # put tail first, because overlap will be an H
            grid[tail_pos.y][tail_pos.x] = tail
            grid[head_pos.y][head_pos.x] = head
            # print_grid(grid)

    return len(tail_positions)


def move_rope(head_pos, tail_pos, direction):
    # move head
    match direction:
        case "R":
            head_pos = pos(head_pos.x + 1, head_pos.y)
        case "L":
            head_pos = pos(head_pos.x - 1, head_pos.y)
        case "U":
            head_pos = pos(head_pos.x, head_pos.y - 1)
        case "D":
            head_pos = pos(head_pos.x, head_pos.y + 1)

    # given where head_pos is, move tail

    # if they are touching, we are good
    if head_pos == tail_pos:
        return head_pos, tail_pos
    # check right
    if head_pos.x + 1 == tail_pos.x and head_pos.y == tail_pos.y:
        return head_pos, tail_pos
    # check left
    if head_pos.x - 1 == tail_pos.x and head_pos.y == tail_pos.y:
        return head_pos, tail_pos
    # check up
    if head_pos.x == tail_pos.x and head_pos.y - 1 == tail_pos.y:
        return head_pos, tail_pos
    # check down
    if head_pos.x == tail_pos.x and head_pos.y + 1 == tail_pos.y:
        return head_pos, tail_pos
    # diag right top
    if head_pos.x + 1 == tail_pos.x and head_pos.y - 1 == tail_pos.y:
        return head_pos, tail_pos
    # diag right bot
    if head_pos.x + 1 == tail_pos.x and head_pos.y + 1 == tail_pos.y:
        return head_pos, tail_pos
    # diag left top
    if head_pos.x - 1 == tail_pos.x and head_pos.y - 1 == tail_pos.y:
        return head_pos, tail_pos
    # diag left bot
    if head_pos.x - 1 == tail_pos.x and head_pos.y + 1 == tail_pos.y:
        return head_pos, tail_pos

    # if not touching, we need to figure out where to move the tail

    # if on same x, move closer on y
    if head_pos.x == tail_pos.x:
        if head_pos.y > tail_pos.y:
            tail_pos = pos(tail_pos.x, tail_pos.y + 1)
        else:
            tail_pos = pos(tail_pos.x, tail_pos.y - 1)

        return head_pos, tail_pos

    # if on same y, move closer on x
    if head_pos.y == tail_pos.y:
        if head_pos.x > tail_pos.x:
            tail_pos = pos(tail_pos.x + 1, tail_pos.y)
        else:
            tail_pos = pos(tail_pos.x - 1, tail_pos.y)
        return head_pos, tail_pos

    # if head is above T and to right of T
    if head_pos.x > tail_pos.x and head_pos.y < tail_pos.y:
        # move diagonally top right
        tail_pos = pos(tail_pos.x + 1, tail_pos.y - 1)
        return head_pos, tail_pos

    # if head is below T and to right of T
    # move diagonally top right
    if head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]:
        # move diagonally top right
        tail_pos = pos(tail_pos.x + 1, tail_pos.y + 1)
        return head_pos, tail_pos

    if head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]:
        # move diagonally top right
        tail_pos = pos(tail_pos.x - 1, tail_pos.y + 1)
        return head_pos, tail_pos

    if head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]:
        # move diagonally top right
        tail_pos = pos(tail_pos.x - 1, tail_pos.y - 1)
        return head_pos, tail_pos

    return head_pos, tail_pos


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    vals = get_input("input")
    assert apply_moves(test_vals) == 13
    print(apply_moves(vals))

    print("# part 2------------------")
