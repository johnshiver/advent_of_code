def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [[eval(p) for p in l.split("\n")] for l in input_file.read().split("\n\n")]


def get_input2(file_name):
    with open(file_name, "r") as input_file:
        return [eval(p) for l in input_file.read().split("\n\n") for p in l.split("\n")]


def compare_packet_pairs(l, r):
    l = l[::-1]
    r = r[::-1]

    while l and r:
        left = l.pop()
        right = r.pop()

        left_t = type(left)
        right_t = type(right)
        # print(f"compare {left} vs {right}")

        if left_t == int and right_t == int:
            if left != right:
                return left < right
        if left_t == list and right_t == list:
            compared = compare_packet_pairs(left, right)
            if compared is not None:
                return compared
        if left_t == int and right_t == list:
            compared = compare_packet_pairs([left], right)
            if compared is not None:
                return compared
        if left_t == list and right_t == int:
            compared = compare_packet_pairs(left, [right])
            if compared is not None:
                return compared

    # we ran out of items to compare
    # print(f"ran out of items: l: {len(l)} r: {len(r)}")

    # if only left is empty, we're good
    if not len(l) and len(r):
        return True

    if len(l) and not len(r):
        return False

    # means we cant make a comparison
    return None


def merge_sort(pairs):
    if len(pairs) < 2:
        return pairs

    mid = len(pairs) // 2
    left, right = pairs[:mid], pairs[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    final = []
    l = r = 0
    while l < len(left) and r < len(right):
        l_val = left[l]
        r_val = right[r]
        if compare_packet_pairs(l_val, r_val):
            final.append(l_val)
            l += 1
        else:
            final.append(r_val)
            r += 1

    while l < len(left):
        l_val = left[l]
        final.append(l_val)
        l += 1

    while r < len(right):
        r_val = right[r]
        final.append(r_val)
        r += 1

    return final


if __name__ == "__main__":
    print("# part 1------------------")

    pairs = get_input("/Users/jshiver/projects/advent_of_code/2022/day13/test_input")
    inicies = []
    for i, pair in enumerate(pairs):
        # print(f"compare {pair}")
        right = compare_packet_pairs(pair[0], pair[1])
        # print(f"{i+1} {right} is in the right order {pair}")
        if right:
            inicies.append(i + 1)
    assert sum(inicies) == 13

    pairs = get_input("/Users/jshiver/projects/advent_of_code/2022/day13/input")
    indicies = []
    for i, pair in enumerate(pairs):
        # print(f"compare {pair[0]} vs {pair[1]}")
        right = compare_packet_pairs(pair[0], pair[1])
        # print(f"{i+1} {right}")
        if right is True:
            indicies.append(i + 1)
    print(indicies)
    print(sum(indicies))

    print("# part 2------------------")

    pairs = get_input2("/Users/jshiver/projects/advent_of_code/2022/day13/test_input")
    pairs.append([[2]])
    pairs.append([[6]])

    pairs_sorted = merge_sort(pairs)
    print(pairs_sorted)
    x = pairs_sorted.index([[2]]) + 1
    y = pairs_sorted.index([[6]]) + 1
    print(x * y)

    pairs = get_input2("/Users/jshiver/projects/advent_of_code/2022/day13/input")
    pairs.append([[2]])
    pairs.append([[6]])

    pairs_sorted = merge_sort(pairs)
    x = pairs_sorted.index([[2]]) + 1
    y = pairs_sorted.index([[6]]) + 1
    print(x * y)
