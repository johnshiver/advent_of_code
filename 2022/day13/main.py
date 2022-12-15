def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [[eval(p) for p in l.split("\n")] for l in input_file.read().split("\n\n")]


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
            compared = compare_packet_pairs(left[:], right[:])
            if compared is not None:
                return compared
        if left_t == int and right_t == list:
            compared = compare_packet_pairs([left], right[:])
            if compared is not None:
                return compared
        if left_t == list and right_t == int:
            compared = compare_packet_pairs(left[:], [right])
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
