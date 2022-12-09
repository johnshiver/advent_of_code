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
    divider = "-" * 200
    print(divider)
    print()


def generate_grid(dimensions):
    grid = [["." for columns in range(dimensions[0])] for rows in range(dimensions[1])]
    return grid


def move_rope(moves):
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
    head_pos = (starting_x, starting_y)
    tail_pos = (starting_x, starting_y)
    tail_positions.add(tail_pos)
    grid[starting_y][starting_x] = head
    print_grid(grid)

    for m in moves:
        direction, count = m.split(" ")
        count = int(count)
        print(f"== {direction} {count}")
        for _ in range(count):
            head_pos, tail_pos = move_rope(head_pos, tail_pos, direction)
            tail_positions.add(tail_pos)

            # put tail first, because overlap will be an H
            grid[tail_pos[1]][tail_pos[0]] = tail
            grid[head_pos[1]][head_pos[0]] = head
            print_grid(grid)

    return len(tail_positions)


def move_rope(head_pos, tail_pos, direction):
    match direction:
        case "R":
            head_pos[0] += 1
        case "L":
            head_pos[0] -= 1
        case "U":
            head_pos[1] -= 1
        case "D":
            head_pos[1] += 1

    # given where head_pos is, move tail

    # if they are touching, we are good
    # check right
    # check left
    # check up
    # check down
    # diag right top
    # diag right bot
    # diag left top
    # diag left bot

    # if not touching, we need to figure out where to put

    # if on same x, move closer on y
    if head_pos[0] - tail_pos[0] == 0:
        if head_pos[1] > tail_pos[1]:
            tail_pos[1] += 1
        else:
            tail_pos[1] -= 1

        return head_pos, tail_pos

    # if on same y, move closer on x
    if head_pos[1] - tail_pos[1] == 0:
        if head_pos[0] > tail_pos[0]:
            tail_pos[0] += 1
        else:
            tail_pos[0] -= 1
        return head_pos, tail_pos

    # if head is above T and to right of T
    # move diagonally top right

    # if head is above T and to right of T
    # move diagonally top right

    # if they arent close, figure out where to go
    return head_pos, tail_pos


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day09/test_input")
    vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day09/input")
    move_rope(test_vals)
    # get_dimensions(vals)

    print("# part 2------------------")
