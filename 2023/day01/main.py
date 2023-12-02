"""
--- Day 1: Trebuchet?! ---

Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
"""


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip() for l in input_file.readlines()]


def calibrate(text):
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    first_seen = None
    last_seen = None

    for i, c in enumerate(text):
        if c.isdigit():
            if first_seen is None:
                first_seen = c
            last_seen = c
        # part 2, comment out for part 1 only
        else:
            # see if the current letter forms a number
            for n in numbers:
                if text[i:].startswith(n):
                    if first_seen is None:
                        first_seen = numbers[n]
                    last_seen = numbers[n]

    return int(first_seen + last_seen)


# print("# part 1------------------")
# test_vals = get_input("test_input")
# fixed = sum([calibrate(l) for l in test_vals])
# assert fixed == 142

# test_vals = get_input("input")
# fixed = sum([calibrate(l) for l in test_vals])
# print(fixed)

print("# part 2------------------")
test_vals = get_input("test_input_2")
fixed = sum([calibrate(l) for l in test_vals])
assert fixed == 281

test_vals = get_input("input")
fixed = sum([calibrate(l) for l in test_vals])
print(fixed)
