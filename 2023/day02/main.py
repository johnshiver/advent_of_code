

"""
"""

def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip() for l in input_file.readlines()]

def parse_game_number(game_input):
    left, _ = game_input.split(":")
    return left.split(' ')[1].rstrip(":")


def check_game_records(game_record, max_red, max_green, max_blue):
    # get game number
    game_number = parse_game_number(game_record)
    _, all_rounds = game_record.split(":")
    all_rounds = all_rounds.split(";")
    for r in all_rounds:
        colors = r.split(',')
        for c in colors:
            count, color = c.lstrip().split(' ')
            count = int(count)
            if color == "green" and count > max_green:
                return 0
            if color == "red" and count > max_red:
                return 0
            if color == "blue" and count > max_blue:
                return 0
    return int(game_number)

def check_game_records_2(game_record):
    _, all_rounds = game_record.split(":")
    all_rounds = all_rounds.split(";")
    max_red = max_blue = max_green = 0
    for r in all_rounds:
        colors = r.split(',')
        for c in colors:
            count, color = c.lstrip().split(' ')
            count = int(count)
            if color == "green":
                max_green = max(max_green, count)
            if color == "red": 
                max_red = max(max_red, count)
            if color == "blue": 
                max_blue = max(max_blue, count)
    return max_blue * max_green * max_red




def main():

    print("# part 1------------------")
    test_vals = get_input("test_input")
    assert 8 == (sum([check_game_records(v, 12, 13, 14) for v in test_vals]))
    test_vals = get_input("input")
    print(sum([check_game_records(v, 12, 13, 14) for v in test_vals]))

    print("# part 2------------------")
    test_vals = get_input("test_input")
    assert 2286  == (sum([check_game_records_2(v) for v in test_vals]))
    test_vals = get_input("input")
    print(sum([check_game_records_2(v) for v in test_vals]))

main()
