def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip() for l in input_file.readlines()]


# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def cound_points(raw_cards):
    card_nu_raw, vals = raw_cards.split(":")
    # card_nu = card_nu_raw.split(" ")[-1]
    all_nums = vals.split("|")
    winning_nums, my_nums = all_nums[0], all_nums[1]
    winning_nums = set(winning_nums.split(" "))
    my_nums = set(my_nums.split(" "))
    matching = my_nums & winning_nums
    if len(matching) == 1:
        return 0
    # 2 instead of 1 to account for empty '' that always matches
    return 2 ** (len(matching) - 2)


def cound_matches(raw_cards):
    card_nu_raw, vals = raw_cards.split(":")
    # card_nu = card_nu_raw.split(" ")[-1]
    all_nums = vals.split("|")
    winning_nums, my_nums = all_nums[0], all_nums[1]
    winning_nums = set(winning_nums.split(" "))
    my_nums = set(my_nums.split(" "))
    matching = my_nums & winning_nums
    return len(matching) - 1


def generate_cards(all_cards):
    from collections import defaultdict

    card_counts = defaultdict(int)
    for i in range(len(all_cards)):
        card_counts[i] = 1
    for i, c in enumerate(all_cards):
        count = card_counts[i]
        matches = cound_matches(c)
        # print(i, count, matches)
        for j in range(i + 1, i + 1 + matches):
            if j > len(all_cards):
                continue
            card_counts[j] += count
    return sum(card_counts.values())


print("# part 1------------------")
test_vals = get_input("test_input")
points = [cound_points(l) for l in test_vals]
assert sum(points) == 13

test_vals = get_input("input")
points = [cound_points(l) for l in test_vals]
print(sum(points))

print("# part 2------------------")
test_vals = get_input("test_input")
total_cards = generate_cards(test_vals)
assert total_cards == 30

test_vals = get_input("input")
total_cards = generate_cards(test_vals)
print(total_cards)
