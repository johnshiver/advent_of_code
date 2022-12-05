from collections import namedtuple


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


move = namedtuple("move", ["source", "count", "destination"])


def parse_input(input_lines):
    vals = [l for l in input_lines]
    mid = vals.index("")
    stack_input, move_input = vals[:mid], vals[mid + 1 :]
    stacks = parse_stack_input(stack_input)
    moves = parse_move_input(move_input)
    return stacks, moves


def parse_stack_input(input):
    stack_count = 0
    # read last line for stack count
    for i, c in enumerate(input[-1]):
        if c.isdigit():
            stack_count = max(stack_count, int(c))
    stacks = [[] for i in range(stack_count)]
    for line in input:
        for i, c in enumerate(line):
            if not c.isalpha():
                continue
            stacks[i // 4].append(c)

    return [s[::-1] for s in stacks]


def parse_move_input(input):
    moves = []
    for line in input:
        parts = line.split(" ")
        count = int(parts[1])
        source = int(parts[3])
        dest = int(parts[5])
        moves.append(move(source=source, count=count, destination=dest))

    return moves


def apply_moves_to_stacks_9000(stacks, moves):
    for move in moves:
        for _ in range(move.count):
            stacks[move.destination - 1].append(stacks[move.source - 1].pop())
    return stacks


def apply_moves_to_stacks_9001(stacks, moves):
    for move in moves:
        stacks[move.destination - 1].extend(stacks[move.source - 1][-move.count :])
        for _ in range(move.count):
            stacks[move.source - 1].pop()

    return stacks


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
    vals = get_input("input")

    stacks, moves = parse_input(test_vals)
    stacks = apply_moves_to_stacks_9000(stacks, moves)
    assert "".join([s[-1] for s in stacks]) == "CMZ"

    stacks, moves = parse_input(vals)
    stacks = apply_moves_to_stacks_9000(stacks, moves)
    print("".join([s[-1] for s in stacks]))

    print("# part 2------------------")

    stacks, moves = parse_input(test_vals)
    stacks = apply_moves_to_stacks_9001(stacks, moves)
    assert "".join([s[-1] for s in stacks]) == "MCD"

    stacks, moves = parse_input(vals)
    stacks = apply_moves_to_stacks_9001(stacks, moves)
    print("".join([s[-1] for s in stacks]))
