from typing import DefaultDict


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [x for x in input_file.readlines()]


def policy1(minval, maxval, val, password):
    counter = DefaultDict(int)
    for char in password:
        counter[char] += 1

    if not (minval <= counter[val] <= maxval):
        return False

    return True


def policy2(pos1, pos2, val, password):
    found1 = password[pos1 - 1] == val
    found2 = password[pos2 - 1] == val
    return int(found1) + int(found2) == 1


def check_inputs(vals, policy):
    count = 0
    for v in vals:
        occurence_raw, val_raw, password = v.split(" ")
        minval, maxval = occurence_raw.split("-")
        val = val_raw.rstrip(":")
        if policy(int(minval), int(maxval), val, password):
            count += 1
    return count


if __name__ == "__main__":
    test_vals = get_input("test_input")
    valid_pws = check_inputs(test_vals, policy1)
    if valid_pws != 2:
        print("test failed for policy 1, received {valid_pws} expected 2")
    valid_pws = check_inputs(test_vals, policy2)
    if valid_pws != 1:
        print("test failed for policy 2, received {valid_pws} expected 1")
    vals = get_input("input")
    valid_pws = check_inputs(vals, policy1)
    print(valid_pws)
    valid_pws = check_inputs(vals, policy2)
    print(valid_pws)