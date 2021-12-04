def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [int(l) for l in input_file.readlines()]


def calc_increases(vals):
    count = 0
    last = vals[0]
    for v in vals[1:]:
        if v > last:
            count += 1
        last = v
    return count


def calc_increases_in_window(vals, window_size):
    count = 0
    last = sum(vals[0:window_size])
    for i in range(len(vals) - window_size):
        curr = last - vals[i]
        curr += vals[i + window_size]
        if curr > last:
            count += 1
        last = curr
    return count


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("2021/day1/test_input")
    count = calc_increases(test_vals)
    assert count == 7

    vals = get_input("2021/day1/input")
    count = calc_increases(vals)
    assert count == 1387

    print("# part 2------------------")
    count = calc_increases_in_window(test_vals, 3)
    assert count == 5

    count = calc_increases_in_window(vals, 3)
    assert count == 1362
