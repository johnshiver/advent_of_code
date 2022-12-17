from collections import namedtuple

pos = namedtuple("pos", ["x", "y"])


def get_input(file_name):
    with open(file_name, "r") as input_file:
        intermediate = [
            [tuple([int(i) for i in x.strip().split(",")]) for x in l.split("->")]
            for l in input_file.read().split("\n")
        ]
        return [[pos(x=j[0], y=j[1]) for j in i] for i in intermediate]


def get_grid_dimensions(rock_formations):
    max_x = 0
    max_y = 0
    for f in rock_formations:
        for pos in f:
            max_x = max(max_x, pos.x)
            max_y = max(max_y, pos.y)
    return max_x, max_y


def create_grid(x, y):
    return [["." for columns in range(x + 1)] for rows in range(y + 1)]


def print_grid(grid):
    print("\n".join([" ".join([str(cell) for cell in row]) for row in grid]))


def draw_rocks_on_grid(grid, formations):
    """ """
    for f in formations:
        # apply one at a time
        for i in range(len(f) - 1):
            start, end = f[i], f[i + 1]

            # move right
            if start.x < end.x:
                for x in range(start.x, end.x + 1):
                    grid[start.y][x] = "#"

            # move left
            elif start.x > end.x:
                for x in range(end.x, start.x + 1):
                    # print(start.y, x)
                    grid[start.y][x] = "#"

            # move down
            elif start.y < end.y:
                for y in range(start.y, end.y + 1):
                    grid[y][start.x] = "#"

            # move up
            elif start.y > end.y:
                for y in range(end.y, start.y + 1):
                    grid[y][start.x] = "#"

    # print_grid(grid)
    return grid


def pour_sand(rock_grid, x, y):
    """
    A unit of sand always falls down one step if possible.

    If the tile immediately below is blocked (by rock or sand)
    the unit of sand attempts to instead move diagonally one step down and to the left

    If that tile is blocked, the unit of sand attempts to instead move diagonally one step down and to the right
    Sand keeps moving as long as it is able to do so
    at each step trying to move down, then down-left, then down-right

    If all three possible destinations are blocked
    the unit of sand comes to rest and no longer moves
    at which point the next unit of sand is created back at the source
    """
    sand = pos(x, y)
    keep_going = True
    moves = 0
    while (
        0 <= sand.y < len(rock_grid) and 0 <= sand.x < len(rock_grid[0]) and keep_going
    ):
        match rock_grid[sand.y + 1][sand.x]:
            case ".":
                sand = pos(sand.x, sand.y + 1)
                moves += 1
                continue
            case "O" | "#":
                # check diag left
                match rock_grid[sand.y + 1][sand.x - 1]:
                    # if that is blocked, try right
                    case ".":
                        sand = pos(sand.x - 1, sand.y + 1)
                        moves += 1
                        continue
                    case "O" | "#":
                        # check diag left
                        match rock_grid[sand.y + 1][sand.x + 1]:
                            case ".":
                                sand = pos(sand.x + 1, sand.y + 1)
                                moves += 1
                                continue
                            # if blocked
                            case "O" | "#":
                                rock_grid[sand.y][sand.x] = "O"
                                keep_going = False

    return moves > 0


if __name__ == "__main__":
    print("# part 1------------------")
    # rock_formations = get_input(
    #     "/Users/johnshiver/projects/advent_of_code/2022/day14/test_input"
    # )
    # x, y = get_grid_dimensions(rock_formations)
    # print(x, y)
    # grid = create_grid(x, y)
    # # print_grid([l[490:520] for l in grid])
    # grid = draw_rocks_on_grid(grid, rock_formations)
    # # for x in range(len(grid[-1])):
    # #     grid[-1][x] = "#"
    # print_grid([l[490:520] for l in grid])

    # count = 0
    # keep_pouring = True
    # while keep_pouring:
    #     keep_pouring = pour_sand(grid, 500, 0)
    #     count += 1
    #     print(count)
    #     print()
    #     print_grid([l[490:520] for l in grid])
    # # grid = draw_rocks_on_grid(grid, rock_formations)
    # # grid = pour_sand(grid)
    # # count sand on grid
    # print(count)

    # rock_formations = get_input(
    #     "/Users/johnshiver/projects/advent_of_code/2022/day14/input"
    # )
    # x, y = get_grid_dimensions(rock_formations)
    # grid = create_grid(x, y)
    # grid = draw_rocks_on_grid(grid, rock_formations)

    # count = 0
    # keep_pouring = True
    # while keep_pouring:
    #     keep_pouring = pour_sand(grid, 500, 0)
    #     count += 1
    #     print(count)
    # # grid = draw_rocks_on_grid(grid, rock_formations)
    # # grid = pour_sand(grid)
    # # count sand on grid
    # print(count)

    print("# part 2------------------")

    rock_formations = get_input(
        "/Users/johnshiver/projects/advent_of_code/2022/day14/test_input"
    )
    x, y = get_grid_dimensions(rock_formations)
    grid = create_grid(x * 2, y + 2)
    grid = draw_rocks_on_grid(grid, rock_formations)
    for x in range(len(grid[-1])):
        grid[-1][x] = "#"

    count = 0
    keep_pouring = True
    while keep_pouring:
        keep_pouring = pour_sand(grid, 500, 0)
        count += 1
        print(count)
        print()
        print_grid([l[474:550] for l in grid])
    # grid = draw_rocks_on_grid(grid, rock_formations)
    # grid = pour_sand(grid)
    # count sand on grid
    print(count)

    rock_formations = get_input(
        "/Users/johnshiver/projects/advent_of_code/2022/day14/input"
    )
    x, y = get_grid_dimensions(rock_formations)
    grid = create_grid(x * 2, y + 2)
    grid = draw_rocks_on_grid(grid, rock_formations)
    for x in range(len(grid[-1])):
        grid[-1][x] = "#"

    count = 0
    keep_pouring = True
    while keep_pouring:
        keep_pouring = pour_sand(grid, 500, 0)
        count += 1
        print(count)
    # grid = draw_rocks_on_grid(grid, rock_formations)
    # grid = pour_sand(grid)
    # count sand on grid
    print(count)
