def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip() for l in input_file.readlines()]


def calc_elf_calories_from_input(vals):
    most_seen = -1
    accumulate = 0
    for v in vals:
        try:
            cal = int(v)
            accumulate += cal
        except:
            most_seen = max(most_seen, accumulate)
            accumulate = 0
    return most_seen


def calc_top_three_elf_calories_from_input(vals):
    all_elves = []
    accumulate = 0
    for v in vals:
        try:
            cal = int(v)
            accumulate += cal
        except:
            all_elves.append(accumulate)
            accumulate = 0
    if accumulate != 0:
        all_elves.append(accumulate)
    return sum(sorted(all_elves, reverse=True)[:3])


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    most_cals = calc_elf_calories_from_input(test_vals)
    assert most_cals == 24000

    vals = get_input("input")
    most_cals = calc_elf_calories_from_input(vals)
    print(most_cals)

    print("# part 2------------------")
    top_three = calc_top_three_elf_calories_from_input(test_vals)
    assert top_three == 45000
    top_three = calc_top_three_elf_calories_from_input(vals)
    print(top_three)
