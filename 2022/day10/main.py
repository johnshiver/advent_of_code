def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


def determine_cpu_signal(inputs):
    cpu_register = 1
    instructions = []
    signals = []

    # pull them off like stack
    inputs = inputs[::-1]

    curr_cycle = 1
    while inputs:
        # only keep 1 instruction at a time
        if not instructions:
            input = inputs.pop()
            parts = input.split(" ")
            match parts[0]:
                case "noop":
                    instructions.append((0, 1))
                case "addx":
                    value = int(parts[1])
                    instructions.append((value, 2))  # takes 2 cycles

        # during cycle, check signal
        if curr_cycle in (20, 60, 100, 140, 180, 220):
            signals.append(curr_cycle * cpu_register)

        # at the end of cycle, update curr instructions
        if instructions:
            val, cycles_left = instructions.pop()
            if cycles_left - 1 == 0:
                cpu_register += val
            else:
                instructions.append((val, cycles_left - 1))

        curr_cycle += 1
    return sum(signals)


def draw_display(inputs):
    display = crt_display()
    cpu_register = 1
    instructions = []

    # pull them off like stack
    inputs = inputs[::-1]

    curr_cycle = 1
    while inputs:
        # only keep 1 instruction at a time
        if not instructions:
            input = inputs.pop()
            parts = input.split(" ")
            match parts[0]:
                case "noop":
                    instructions.append((0, 1))
                case "addx":
                    value = int(parts[1])
                    instructions.append((value, 2))  # takes 2 cycles

        display = draw_pixel(display, curr_cycle, cpu_register)
        # print_diplay(display)

        # at the end of cycle, update curr instructions
        if instructions:
            val, cycles_left = instructions.pop()
            if cycles_left - 1 == 0:
                cpu_register += val
            else:
                instructions.append((val, cycles_left - 1))

        curr_cycle += 1
    print(curr_cycle)
    return display


def crt_display():
    # You count the pixels on the CRT: 40 wide and 6 high.
    # This CRT screen draws the top row of pixels left-to-right, then the row below that, and so on.
    # The left-most pixel in each row is in position 0, and the right-most pixel in each row is in position 39.
    return ["." for _ in range(240)]


def draw_pixel(display, cpu_cycle, pixel_pos):
    # Like the CPU, the CRT is tied closely to the clock circuit:
    # the CRT draws a single pixel during each cycle. Representing each pixel of the screen as a #,
    # here are the cycles during which the first and last pixel in each row are drawn:

    # is pixel position in view of cpu cycle?
    cpu_cycle -= 1
    check_cycle = cpu_cycle % 40
    # print(cpu_cycle - 1, pixel_pos)
    if pixel_pos - 1 <= check_cycle <= pixel_pos + 1:
        display[cpu_cycle] = "#"
    return display


def print_diplay(display):
    display = [display[n : n + 40] for n in range(0, len(display), 40)]
    print("\n".join([" ".join([str(cell) for cell in row]) for row in display]))
    divider = "-" * 2 * (len(display[0]))
    print(divider)
    print()


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input(
        "/Users/johnshiver/projects/advent_of_code/2022/day10/test_input"
    )
    assert determine_cpu_signal(test_vals) == 13140
    vals = get_input("/Users/johnshiver/projects/advent_of_code/2022/day10/input")
    assert determine_cpu_signal(vals) == 14760

    print("# part 2------------------")

    display = draw_display(test_vals)
    print_diplay(display)

    display = draw_display(vals)
    print_diplay(display)
