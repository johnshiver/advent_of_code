import math


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [int(l) for l in input_file.readlines()]


def calc_2sum(vals, target):
    vals = set(vals)
    for v in vals:
        if target - v in vals:
            return (target - v), v
    return None, None


def calc_3sum(vals, target):
    for v in vals:
        new_target = target - v
        v2, v3 = calc_2sum(vals, new_target)
        if v2 is not None:
            return v, v2, v3
    return None, None, None


if __name__ == "__main__":
    test_vals = get_input("test_input")
    v1, v2 = calc_2sum(test_vals, 2020)
    if v1 * v2 != 514579:
        print("test failed, received {ans}")
    vals = get_input("input")
    v1, v2 = calc_2sum(vals, 2020)
    print(v1 * v2)
    v1, v2, v3 = calc_3sum(test_vals, 2020)
    ans = v1 * v2 * v3
    if ans != 241861950:
        print("3sum test failed, received {ans}")
    v1, v2, v3 = calc_3sum(vals, 2020)
    print(v1 * v2 * v3)
