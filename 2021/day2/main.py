def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.split(" ") for l in input_file.readlines()]


def run_commands(cmds):
    depth = 0
    horz = 0
    for cmd, x in cmds:
        x = int(x)
        if cmd == "up":
            depth -= x
        elif cmd == "down":
            depth += x
        elif cmd == "forward":
            horz += x
    return depth * horz


def run_commands_v2(cmds):
    aim = 0
    depth = 0
    horz = 0
    for cmd, x in cmds:
        x = int(x)
        if cmd == "up":
            aim -= x
        elif cmd == "down":
            aim += x
        elif cmd == "forward":
            horz += x
            depth += aim * x
    return depth * horz


if __name__ == "__main__":
    print("day 2 part 1")
    test_vals = get_input("test_input")
    assert run_commands(test_vals) == 150
    vals = get_input("input")
    print(run_commands(vals))

    print("day 2 part 2")
    assert run_commands_v2(test_vals) == 900
    print(run_commands_v2(vals))
