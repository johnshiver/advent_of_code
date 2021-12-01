from collections import defaultdict


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [int(l) for l in input_file.readlines()]


def calc_increases(vals):
    count = 0
    if len(vals) < 2:
        return count
    last = vals[0]
    for v in vals[1:]:
        if v > last:
            count += 1
        last = v
    return count

def calc_increases_in_window(vals):
    count = 0
    last = -1
    for window in range(len(vals)):
        total = sum(vals[window])
        if last == -1:
            last = total
            continue
        if total > last:
            count += 1
        last = total
    return count

def create_windows(vals):
    window_size = 3
    output = defaultdict(list)
    for i in range(len(vals)):
        output[i] = vals[i:i+window_size]
    return output


if __name__ == "__main__":
    test_vals = get_input("test_input")
    count = calc_increases(test_vals)
    assert count == 7
    vals = get_input("input")
    count = calc_increases(vals)
    print(count)

    print("# part 2")
    test_vals = create_windows(test_vals)
    count = calc_increases_in_window(test_vals)
    assert count == 5

    vals = create_windows(vals)
    count = calc_increases_in_window(vals)
    print(count)



