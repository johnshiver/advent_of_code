def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def compare_shifts(shift):
    elf1, elf2 = shift.split(",")
    elf1_times = [int(i) for i in elf1.split("-")]
    elf2_times = [int(i) for i in elf2.split("-")]
    times = [elf1_times, elf2_times]
    # if second is smaller than first
    one = times[0][0] <= times[1][0] and times[0][1] >= times[1][1]
    two = times[0][0] >= times[1][0] and times[0][1] <= times[1][1]
    return one or two


def compare_any_shifts(shift):
    elf1, elf2 = shift.split(",")
    elf1_times = [int(i) for i in elf1.split("-")]
    elf2_times = [int(i) for i in elf2.split("-")]
    inter = set(range(elf1_times[0], elf1_times[1] + 1)) & set(
        range(elf2_times[0], elf2_times[1] + 1)
    )
    return bool(inter)


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    vals = get_input("input")

    assert sum([int(compare_shifts(s)) for s in test_vals]) == 2
    print(sum([int(compare_shifts(s)) for s in vals]))

    print("# part 2------------------")
    assert sum([int(compare_any_shifts(s)) for s in test_vals]) == 4
    print(sum([int(compare_any_shifts(s)) for s in vals]))
