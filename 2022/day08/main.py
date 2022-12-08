from collections import defaultdict
from functools import reduce


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


# all other trees between it and edge of grid are shorter than it
def find_visible_trees(tree_grid):
    # skip the first line
    is_visible = defaultdict(list)
    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            if x == 0 or x == len(tree_grid[0]) - 1:
                is_visible[(x, y)].extend(["U", "D", "L", "R"])
            elif y == 0 or y == len(tree_grid) - 1:
                is_visible[(x, y)].extend(["U", "D", "L", "R"])
            else:
                is_visible[(x, y)] = []

    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            if is_visible[(x, y)]:
                continue

            curr = tree_grid[y][x]

            # try going left
            tmp_x = x - 1
            while tmp_x >= 0:
                new_left = tree_grid[y][tmp_x]
                if curr <= new_left:
                    break
                # means we have reached the edge and curr hasnt found a bigger option yet
                if tmp_x == 0:
                    is_visible[(x, y)].append("L")
                tmp_x -= 1

            # try going up
            tmp_y = y - 1
            while tmp_y >= 0:
                new_up = tree_grid[tmp_y][x]
                if curr <= new_up:
                    break
                # means we have reached the edge and curr hasnt found a bigger option yes
                if tmp_y == 0:
                    is_visible[(x, y)].append("U")
                tmp_y -= 1

            # try going right
            tmp_x = x + 1
            while tmp_x < len(tree_grid[0]):
                new_right = tree_grid[y][tmp_x]
                if curr <= new_right:
                    break
                # means we have reached the edge and curr hasnt found a bigger option yet
                if tmp_x == len(tree_grid[0]) - 1:
                    is_visible[(x, y)].append("R")
                    break
                tmp_x += 1

            # try going down
            tmp_y = y + 1
            while tmp_y < len(tree_grid):
                new_down = tree_grid[tmp_y][x]
                if curr <= new_down:
                    break
                # means we have reached the edge and curr hasnt found a bigger option yet
                if tmp_y == len(tree_grid) - 1:
                    is_visible[(x, y)].append("D")
                    break
                tmp_y += 1

    # print(is_visible)
    return sum([1 for x in is_visible.values() if len(x)])


def find_tree_with_visibility(tree_grid):
    # skip the first line
    trees_visible = defaultdict(list)

    for y in range(len(tree_grid)):
        for x in range(len(tree_grid[0])):
            if x == 0 or x == len(tree_grid[0]) - 1:
                continue
            elif y == 0 or y == len(tree_grid) - 1:
                continue

            curr = tree_grid[y][x]

            # try going left
            tmp_x = x - 1
            while tmp_x >= 0:
                new_left = tree_grid[y][tmp_x]
                if curr <= new_left:
                    trees_visible[(x, y)].append(x - tmp_x)
                    break
                # means we have reached the edge and curr hasnt found a bigger option yet
                if tmp_x == 0:
                    trees_visible[(x, y)].append(x - tmp_x)
                tmp_x -= 1

            # try going up
            tmp_y = y - 1
            while tmp_y >= 0:
                new_up = tree_grid[tmp_y][x]
                if curr <= new_up:
                    trees_visible[(x, y)].append(y - tmp_y)
                    break
                # means we have reached the edge and curr hasnt found a bigger option yes
                if tmp_y == 0:
                    trees_visible[(x, y)].append(y - tmp_y)
                tmp_y -= 1

            # try going right
            tmp_x = x + 1
            while tmp_x < len(tree_grid[0]):
                new_right = tree_grid[y][tmp_x]
                if curr <= new_right:
                    trees_visible[(x, y)].append(tmp_x - x)
                    break
                # means we have reached the edge and curr hasnt found a bigger option yet
                if tmp_x == len(tree_grid[0]) - 1:
                    trees_visible[(x, y)].append(tmp_x - x)
                tmp_x += 1

            # try going down
            tmp_y = y + 1
            while tmp_y < len(tree_grid):
                new_down = tree_grid[tmp_y][x]
                if curr <= new_down:
                    trees_visible[(x, y)].append(tmp_y - y)
                    break
                # means we have reached the edge and curr hasnt found a bigger option yet
                if tmp_y == len(tree_grid) - 1:
                    trees_visible[(x, y)].append(tmp_y - y)
                    break
                tmp_y += 1

    # print(trees_visible)
    return max([reduce(lambda x, y: x * y, vals) for vals in trees_visible.values()])


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    trees = []
    for line in test_vals:
        trees.append([int(c) for c in line])

    # print(find_visible_trees(trees))
    assert find_visible_trees(trees) == 21

    vals = get_input("input")
    trees = []
    for line in vals:
        trees.append([int(c) for c in line])

    print(find_visible_trees(trees))

    print("# part 2------------------")
    test_vals = get_input("test_input")
    trees = []
    for line in test_vals:
        trees.append([int(c) for c in line])
    print(find_tree_with_visibility(trees))
    assert find_tree_with_visibility(trees) == 8

    vals = get_input("input")
    trees = []
    for line in vals:
        trees.append([int(c) for c in line])

    print(find_tree_with_visibility(trees))
