def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def find_four_unique_from_packet(packet):
    start, end = 0, 4
    while end < len(packet):
        if len(set(packet[start:end])) == 4:
            return end
        start += 1
        end += 1
    return -1


def find_unique_message_from_packet(packet):
    start, end = 0, 14
    while end <= len(packet):
        if len(set(packet[start:end])) == 14:
            return end
        start += 1
        end += 1
    return -1


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    vals = get_input("input")

    assert find_four_unique_from_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    print(find_four_unique_from_packet(vals[0]))

    print("# part 2------------------")

    assert find_unique_message_from_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    print(find_unique_message_from_packet(vals[0]))
