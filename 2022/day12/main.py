from collections import namedtuple
from string import ascii_lowercase

pos = namedtuple("pos", ["x", "y"])


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [list(l) for l in input_file.read().split("\n")]


def print_grid(grid):
    print("\n".join([" ".join([str(cell) for cell in row]) for row in grid]))
    divider = "-" * 2 * (len(grid[0]))
    print(divider)
    print()


def get_starting_pos(grid):
    # find starting position
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for y, row in enumerate(grid):
        if "S" in row:
            start_x = row.index("S")
            start_y = y
        if "E" in row:
            end_x = row.index("E")
            end_y = y

    return pos(start_x, start_y), pos(end_x, end_y)


def can_move(grid, x, y):
    if x == "S":
        return True
    if y == "S":
        return False
    if y == "E":
        return x == "z"
    return (ascii_lowercase.find(y) - ascii_lowercase.find(x)) <= 1


def elevation_diff(grid, x, y):
    y_c = grid[y.y][y.x]
    x_c = grid[x.y][x.x]
    if y_c == "S":
        return 10
    if y_c == "E" and x_c == "z":
        return 1
    return ascii_lowercase.find(y_c) - ascii_lowercase.find(x_c)


def distance(x, y):
    return abs(y.x - x.x) + abs(y.y - x.y)


def find_shortest_path(grid, start: pos, end: pos, positions):
    print(f"{start} {end} {grid[start.y][start.x]}")

    if start == end:
        return 0

    # can we go up
    up = pos(start.x, start.y - 1)
    down = pos(start.x, start.y + 1)
    left = pos(start.x - 1, start.y)
    right = pos(start.x + 1, start.y)

    directions = [up, down, left, right]
    best_choices = sorted(
        [
            (d, elevation_diff(grid, start, d), distance(d, end))
            for d in directions
            if 0 <= d.x < len(grid[0])
            and 0 <= d.y < len(grid)
            and d not in positions
            and elevation_diff(grid, start, d) <= 1
        ],
        key=lambda x: x[2],
    )

    if not best_choices:
        return float("inf")

    best_paths = []
    for direction, diff, _ in best_choices:
        positions.add(direction)
        d_weight = 1 + find_shortest_path(grid, direction, end, positions)
        positions.remove(direction)
        if start.x == 0 and start.y == 0:
            print(f"{direction} {d_weight}")
        best_paths.append(d_weight)
        if diff == 1:
            break

    return min(best_paths)


if __name__ == "__main__":
    print("# part 1------------------")
    t_grid = get_input(
        "/Users/johnshiver/projects/advent_of_code/2022/day12/test_input"
    )
    print_grid(t_grid)
    start, end = get_starting_pos(t_grid)
    positions = set()
    # positions.add(start)
    # assert find_shortest_path(t_grid, start, end, positions) == 31
    print(find_shortest_path(t_grid, start, end, positions))

    grid = get_input("/Users/johnshiver/projects/advent_of_code/2022/day12/input")
    start, end = get_starting_pos(grid)
    positions = set()
    print(find_shortest_path(grid, start, end, positions))

    print("# part 2------------------")
