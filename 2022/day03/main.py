from string import ascii_letters


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def find_item_in_rucksack(input):
    mid = len(input) // 2
    first, second = input[:mid], input[mid:]
    shared = set(first) & set(second)
    return shared.pop()


def find_item_in_trio(input):
    shared = set(input[0]) & set(input[1]) & set(input[2])
    return shared.pop()


def get_priority(c):
    return ascii_letters.find(c) + 1


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    assert sum([get_priority(find_item_in_rucksack(v)) for v in test_vals]) == 157
    vals = get_input("input")
    print(sum([get_priority(find_item_in_rucksack(v)) for v in vals]))

    print("# part 2------------------")
    test_trios = [test_vals[n : n + 3] for n in range(0, len(test_vals), 3)]
    assert sum([get_priority(find_item_in_trio(t)) for t in test_trios]) == 70

    trios = [vals[n : n + 3] for n in range(0, len(vals), 3)]
    print(sum([get_priority(find_item_in_trio(t)) for t in trios]))
