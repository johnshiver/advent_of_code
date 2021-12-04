def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def analyze_report(report):
    gamma = [0] * len(report[0])
    # episolon is equal to not gamma

    for line in report:
        line = [int(l) for l in line]
        for i in range(len(gamma)):
            if line[i] > 0:
                gamma[i] += 1
            else:
                gamma[i] -= 1
    gamma = ["0" if i < 0 else "1" for i in gamma]
    epis = ["0" if i == "1" else "1" for i in gamma]

    gamma = int("".join(gamma), 2)
    epis = int("".join(epis), 2)
    return gamma * epis


def analyze_report_part_2(report):
    life_support_rating = 0
    oxygen_rating = 0
    co2_rating = 0

    common, uncommon = analyze_most_common_bits(report)

    oxy_candidates = report[:]
    co2_candidates = report[:]

    curr_bit = 0
    while len(oxy_candidates) > 1:
        oxy_candidates = [x for x in oxy_candidates if x[curr_bit] == common[curr_bit]]
        common, uncommon = analyze_most_common_bits(oxy_candidates)
        curr_bit += 1
    oxygen_rating = int("".join(oxy_candidates[0]), 2)

    curr_bit = 0
    while len(co2_candidates) > 1:
        co2_candidates = [
            x for x in co2_candidates if x[curr_bit] == uncommon[curr_bit]
        ]
        common, uncommon = analyze_most_common_bits(co2_candidates)
        curr_bit += 1
    co2_rating = int("".join(co2_candidates[0]), 2)

    return oxygen_rating * co2_rating


def analyze_most_common_bits(report):
    counter = [0] * len(report[0])
    # episolon is equal to not gamma

    for line in report:
        line = [int(l) for l in line]
        for i in range(len(counter)):
            if line[i] > 0:
                counter[i] += 1
            else:
                counter[i] -= 1
    gamma = ["0" if i < 0 else "1" for i in counter]
    epis = ["0" if i >= 0 else "1" for i in counter]

    return gamma, epis


if __name__ == "__main__":
    print("day 3 part 1")
    test_report = get_input("test_input")
    resp = analyze_report(test_report)
    print(resp)
    assert resp == 198
    report = get_input("input")
    resp = analyze_report(report)
    print(resp)

    print("day 3 part 2")
    resp = analyze_report_part_2(test_report)
    assert resp == 230
    print(analyze_report_part_2(report))
