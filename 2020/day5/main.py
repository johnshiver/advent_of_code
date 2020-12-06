import math


def get_boarding_passes(file_name):
    with open(file_name, "r") as f:
        return [l.rstrip("\n") for l in f.readlines()]


def get_row(commands, rows=128):
    low, high = 0, rows - 1
    curr = 0
    while curr < len(commands) - 1:
        cmd = commands[curr]
        mid = (high + low) / 2
        if cmd == "F":
            mid = math.floor(mid)
            high = mid
        else:
            mid = math.ceil(mid)
            low = mid
        curr += 1
    if commands[-1] == "F":
        return min(low, high)
    return max(low, high)


def get_col(commands, cols=8):
    low, high = 0, cols - 1
    curr = 0
    while curr < len(commands) - 1:
        mid = (high + low) / 2
        cmd = commands[curr]
        if cmd == "L":
            mid = math.floor(mid)
            high = mid
        else:
            mid = math.ceil(mid)
            low = mid
        curr += 1
    if commands[-1] == "L":
        return min(low, high)
    return max(low, high)


def get_seat_id(bp):
    row = get_row(bp[:7])
    col = get_col(bp[7:])
    sid = row * 8 + col
    return sid


if __name__ == "__main__":
    bps = get_boarding_passes("test_input")
    print(max([get_seat_id(bp) for bp in bps]))
    bps = get_boarding_passes("input")
    seats = sorted([get_seat_id(bp) for bp in bps])
    prev = seats[0]
    for s in seats[1:]:
        if s != (prev + 1):
            print(s - 1)
            break
        prev = s
