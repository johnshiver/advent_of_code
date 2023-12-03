def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip() for l in input_file.readlines()]


def find_nums(vals):
    nums = []
    curr = ""
    valid_num = False
    for y in range(len(vals)):
        for x in range(len(vals[0])):
            if vals[y][x].isdigit():
                curr += vals[y][x]
                left = x - 1
                right = x + 1
                down = y + 1
                up = y - 1
                if left >= 0 and not vals[y][left].isdigit() and vals[y][left] != ".":
                    valid_num = True
                if up >= 0 and not vals[up][x].isdigit() and vals[up][x] != ".":
                    valid_num = True
                if (
                    right < len(vals[0])
                    and not vals[y][right].isdigit()
                    and vals[y][right] != "."
                ):
                    valid_num = True
                if (
                    down < len(vals)
                    and not vals[down][x].isdigit()
                    and vals[down][x] != "."
                ):
                    valid_num = True

                # Additional diagonal checks
                # Upper left
                if (
                    left >= 0
                    and up >= 0
                    and not vals[up][left].isdigit()
                    and vals[up][left] != "."
                ):
                    valid_num = True
                # Upper right
                if (
                    right < len(vals[0])
                    and up >= 0
                    and not vals[up][right].isdigit()
                    and vals[up][right] != "."
                ):
                    valid_num = True
                # Lower left
                if (
                    left >= 0
                    and down < len(vals)
                    and not vals[down][left].isdigit()
                    and vals[down][left] != "."
                ):
                    valid_num = True
                # Lower right
                if (
                    right < len(vals[0])
                    and down < len(vals)
                    and not vals[down][right].isdigit()
                    and vals[down][right] != "."
                ):
                    valid_num = True
            else:
                if curr and valid_num:
                    nums.append(int(curr))
                curr = ""
                valid_num = False
    return nums


def find_gear_ratios(vals):
    nums = []
    for y in range(len(vals)):
        curr = ""
        start_x = None
        for x in range(len(vals[0])):
            if vals[y][x].isdigit():
                if start_x is None:
                    start_x = x
                curr += vals[y][x]
            else:
                if curr:
                    nums.append((y, start_x, x - 1, int(curr)))
                curr = ""
                start_x = None
    return nums


def find_gears_and_calculate_ratio(vals, nums):
    gear_ratios = []

    def is_adjacent_to_gear(y, x, num_y, start_x, end_x):
        return num_y == y and start_x <= x <= end_x

    for y in range(len(vals)):
        for x in range(len(vals[0])):
            if vals[y][x] == "*":
                adjacent_numbers = set()

                # Check all eight directions
                for dy, dx in [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1),
                ]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < len(vals) and 0 <= nx < len(vals[0]):
                        for num in nums:
                            if is_adjacent_to_gear(ny, nx, num[0], num[1], num[2]):
                                adjacent_numbers.add(num[3])
                                break

                # Calculate gear ratio if exactly two unique part numbers are adjacent
                if len(adjacent_numbers) == 2:
                    gear_ratio = 1
                    for num in adjacent_numbers:
                        gear_ratio *= num
                    gear_ratios.append(gear_ratio)

    return sum(gear_ratios)


print("# part 1------------------")
test_vals = get_input("test_input")
ans = sum(find_nums([list(v) for v in test_vals]))
assert 4361 == ans
test_vals = get_input("input")
ans = sum(find_nums([list(v) for v in test_vals]))
print(ans)

# print("# part 2------------------")
# test_vals = get_input("test_input")
# nums = find_gear_ratios(test_vals)
# gear_ratio = find_gears_and_calculate_ratio(test_vals, nums)
# assert 467835 == gear_ratio
# test_vals = get_input("input")
# nums = find_gear_ratios(test_vals)
# gear_ratio = find_gears_and_calculate_ratio(test_vals, nums)
# print(gear_ratio)
