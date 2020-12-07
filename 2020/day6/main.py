from collections import defaultdict


def get_input(input_file):
    final = []
    with open(input_file, "r") as f:
        while (contents := f.read()) :
            group_answers = contents.split("\n\n")
            for a in group_answers:
                counter = defaultdict(int)
                total_people = a.count("\n") + 1
                a = a.replace("\n", "")
                for c in a:
                    counter[c] += 1
                totals = [k for k, v in counter.items() if v == total_people]
                final.append(totals)
    return final


if __name__ == "__main__":
    resp = get_input("test_input")
    print(sum([len(i) for i in resp]))
    # resp = get_input("input")

    resp = get_input("input")
    print(sum([len(i) for i in resp]))
