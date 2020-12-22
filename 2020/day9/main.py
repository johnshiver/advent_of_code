# XMAS starts by transmitting a preamble of 25 numbers. After that, each number you receive should be
# the sum of any two of the 25 immediately previous numbers. The two numbers will have different values,
# and there might be more than one such pair.


def get_input(file_name):
    with open(file_name, "r") as f:
        return [int(x.rstrip("\n")) for x in f.readlines()]


def find_invalid_nums(nums, preamble):
    # load preamble into data structure
    # check to see if curr is valid, find pair in preamble that would == curr
    # load curr, remove whatever is at index 0
    x, y = 0, preamble
    curr = preamble
    done = False
    while not done:
        if not pair_found(sorted(nums[x:y]), nums[curr]):
            return nums[curr]
        x += 1
        y += 1
        curr += 1
        if curr > len(nums) - 1:
            done = True


def pair_found(nums, target):
    start, end = 0, len(nums) - 1
    while start < end:
        s, e = nums[start], nums[end]
        if s + e == target:
            return True
        elif s + e > target:
            end -= 1
        else:
            start += 1
    return False


def find_contiguous_set(nums, target):
    x, y = 0, 2
    done = False
    while not done:
        curr_sum = sum(nums[x:y])
        if curr_sum == target:
            return nums[x:y]
        elif curr_sum < target:
            y += 1
        else:
            x += 1
            y = x + 2
        if y > len(nums) - 1:
            done = True
    return None


if __name__ == "__main__":
    test_input = get_input("test_input")
    print(find_invalid_nums(test_input, 5))

    input = get_input("input")
    invalid_num = find_invalid_nums(input, 25)
    # import ipdb

    # ipdb.set_trace()
    c_set = find_contiguous_set(input, invalid_num)
    print(min(c_set) + max(c_set))