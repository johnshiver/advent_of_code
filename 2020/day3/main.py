import math


def read_input(file_name):
    with open(file_name, "r") as f:
        return [l.rstrip("\n") for l in f.readlines()]


def adjust_terrain(terrain, x, y):
    height = len(terrain)
    needed_width = x * height
    multiply_factor = needed_width // len(terrain[0]) * 10
    return [l * multiply_factor for l in terrain]


def run_terrain(terrain, i, j):
    count = 0
    x, y = 0, 0
    while y < len(terrain):
        x += i
        y += j
        try:
            if terrain[y][x] == "#":
                count += 1
        except Exception:
            break
    return count


if __name__ == "__main__":
    test_terrain = adjust_terrain(read_input("test_input"), 3, 1)
    trees_found = run_terrain(test_terrain, 3, 1)
    if trees_found != 7:
        print("found {trees_found} expected 7")
    terrain = adjust_terrain(read_input("input"), 3, 1)
    # trees_found = run_terrain(terrain, 3, 1)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = []
    for s in slopes:
        terrain = adjust_terrain(read_input("input"), s[0], s[1])
        total.append(run_terrain(terrain, s[0], s[1]))
    print(math.prod(total))
