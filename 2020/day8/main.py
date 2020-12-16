def get_input(file_name):
    commands = []
    with open(file_name, "r") as f:
        for l in f.readlines():
            l = l.rstrip("\n")
            operation, arg = l.split(" ")
            commands.append({"operation": operation, "arg": int(arg)})
    return commands


def analze_program(commands):
    accumulator = 0
    curr = 0
    seen = set()
    while True:
        if curr > len(commands) - 1:
            print("finished!")
            return accumulator, 1
        command = commands[curr]
        print(curr, command)
        if curr in seen:
            print("found loop, returning")
            return accumulator, 0
        seen.add(curr)
        op = command["operation"]
        if op == "acc":
            accumulator += command["arg"]
            curr += 1
        elif op == "jmp":
            curr += command["arg"]
        elif op == "nop":
            curr += 1
        elif curr > len(commands) - 1:
            print("finished!")
            return accumulator, 1
        else:
            print("invalid op ${op}")
            return 0, 0


def fix_program(program):
    last_flip = 0
    while True:
        program, flipped = flip_command(program, last_flip)
        if flipped == -1:
            print("no more commands to flip...")
            break
        acc, passed = analze_program(program)
        if passed == 1:
            return acc
        program[flipped]["operation"] = "jmp"
        last_flip = flipped + 1


def flip_command(program, limit):
    for i, v in enumerate(program):
        if i < limit:
            continue
        if v["operation"] == "jmp":
            v["operation"] = "nop"
            return program, i
        # if v["operation"] == "nop":
        #     v["operation"] = "jmp"
        #     return program, i
    return program, -1


if __name__ == "__main__":
    # print(analze_program(get_input("test_input")))
    print(fix_program(get_input("input")))