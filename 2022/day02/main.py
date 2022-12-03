def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def calc_increases(vals):
    count = 0
    last = vals[0]
    for v in vals[1:]:
        if v > last:
            count += 1
        last = v
    return count


def calculate_score_from_round(round):
    opp_move, my_mov = round[0], round[2]
    win = 6
    tie = 3
    loss = 0
    match opp_move:
        case "A":  # rock
            match my_mov:
                case "Y":  # paper
                    return 2 + win
                case "X":  # rock
                    return 1 + tie
                case "Z":  # scissors
                    return 3 + loss
        case "B":  # paper
            match my_mov:
                case "Y":  # paper
                    return 2 + tie
                case "X":  # rock
                    return 1 + loss
                case "Z":  # scissors
                    return 3 + win
        case "C":  # scissors
            match my_mov:
                case "Y":  # paper
                    return 2 + loss
                case "X":  # rock
                    return 1 + win
                case "Z":  # scissors
                    return 3 + tie
    raise Exception(f"this didnt work {opp_move} {my_mov}")


def calculate_score_from_round_with_prediction(round):
    opp_move, my_mov = round[0], round[2]
    win = 6
    tie = 3
    loss = 0
    paper = 2
    rock = 1
    scissors = 3
    match opp_move:
        case "A":  # rock
            match my_mov:
                case "Y":  # tie
                    return rock + tie
                case "X":  # loss
                    return scissors + loss
                case "Z":  # win
                    return paper + win
        case "B":  # paper
            match my_mov:
                case "Y":  # tie
                    return paper + tie
                case "X":  # loss
                    return rock + loss
                case "Z":  # win
                    return scissors + win
        case "C":  # scissors
            match my_mov:
                case "Y":  # tie
                    return scissors + tie
                case "X":  # loss
                    return paper + loss
                case "Z":  # win
                    return rock + win
    raise Exception(f"this didnt work {opp_move} {my_mov}")


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    assert sum([calculate_score_from_round(round) for round in test_vals]) == 15

    vals = get_input("input")
    print(sum([calculate_score_from_round(round) for round in vals]))

    print("# part 2------------------")
    assert (
        sum([calculate_score_from_round_with_prediction(round) for round in test_vals])
        == 12
    )
    print(sum([calculate_score_from_round_with_prediction(round) for round in vals]))
