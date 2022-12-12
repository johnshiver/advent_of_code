from queue import PriorityQueue
from typing import List
from math import prod


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.split("\n") for l in input_file.read().split("\n\n")]


class Monkey:
    def __init__(
        self,
        identifier: int,
        starting_items: List[int],
        operation,
        test_level,
        target_monkey_true,
        target_monkey_false,
    ) -> None:
        # identifier identifies this monkey
        self.identifier = identifier

        # Starting items lists your worry level for each item the monkey
        # is currently holding in the order they will be inspected.

        # ex. [23, 11, 11]
        # priority by position
        self.starting_items = starting_items

        # Operation shows how your worry level changes as that monkey inspects an item.
        # (An operation like new = old * 5 means that your worry level after the monkey inspected the item is five times whatever your worry level was before inspection.)
        self.operation = operation

        # Test shows how the monkey uses your worry level to decide where to throw an item next.
        self.test_level = test_level
        self.test = lambda x: x % test_level == 0

        # If true shows what happens with an item if the Test was true.
        self.if_true = target_monkey_true

        # If false shows what happens with an item if the Test was false.
        self.if_false = target_monkey_false

        self.inspections = 0

    def __str__(self) -> str:
        return f"Monkey {self.identifier} \n\tStarting items: {self.starting_items}\n"

    def __repr__(self) -> str:
        return str(self)

    def catch_item(self, item):
        # put at the end
        """ """
        self.starting_items.append(item)


def parse_monkey(monkey_input):
    """
    Monkey 0:
    Starting items: 79, 98
    Operation: new = old * 19
    Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3
    """
    identifier_raw = monkey_input[0].strip()
    items_raw = monkey_input[1].strip()
    operation_raw = monkey_input[2].strip()
    test_raw = monkey_input[3].strip().split(" ")
    if_true = monkey_input[4].strip().split(" ")
    if_false = monkey_input[5].strip().split(" ")

    identifier = int(identifier_raw.split(" ")[1].rstrip(":"))

    items = [int(i.rstrip(",")) for i in items_raw.split(" ")[2:]]

    operation_parts = operation_raw.split(" ")
    match operation_parts[-2]:
        case "*":
            if operation_parts[-1] == "old":
                operation = lambda x: x * x
            else:
                operation = lambda x: x * int(operation_parts[-1])

        case "+":
            if operation_parts[-1] == "old":
                operation = lambda x: x + x
            else:
                operation = lambda x: x + int(operation_parts[-1])

    test_level = int(test_raw[-1])
    if_true = int(if_true[-1])
    if_false = int(if_false[-1])

    return Monkey(
        identifier=identifier,
        starting_items=items,
        operation=operation,
        test_level=test_level,
        target_monkey_false=if_false,
        target_monkey_true=if_true,
    )


def monkey_inspections(monkeies: List[Monkey]):
    # After each monkey inspects an item but before it tests your worry level
    # your relief that the monkey's inspection didn't damage the item causes your worry level to be
    # divided by three
    # and rounded down to the nearest integer.

    # each monkey takes a turn (round)
    # 20 rounds
    for i in range(20):
        print(f"round {i}")
        for m in monkeies:
            # it inspects and throws all of the items it is holding one at a time and in the order listed
            # Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn
            # The process of each monkey taking a single turn is called a round.

            # monkey inspects and
            items = m.starting_items[::-1]
            while items:
                item_to_inspect = items.pop()
                # print(f"monkey {m.identifier} inspects {item_to_inspect}")

                # monkey inspects + applies operation to item
                inspected_item = m.operation(item_to_inspect)

                # print(f"worry level {inspected_item}")

                m.inspections += 1

                # because monkey didnt destroy, divide by 3 round down
                inspected_item //= 3  # TODO: check this

                target_monkey = None
                if m.test(inspected_item):
                    target_monkey = monkies[m.if_true]
                else:
                    target_monkey = monkies[m.if_false]

                # print(
                #     f"monkey {m.identifier} throws {inspected_item} to monkey {target_monkey.identifier}"
                # )
                target_monkey.catch_item(inspected_item)
            m.starting_items = []
    for m in monkeies:
        print(f"monkey {m.identifier} {m.inspections}")
    top_monkies = sorted([m.inspections for m in monkeies], reverse=True)
    print(top_monkies)
    return top_monkies[0] * top_monkies[1]


def monkey_inspections_no_worries(monkeies: List[Monkey], level):
    # After each monkey inspects an item but before it tests your worry level
    # your relief that the monkey's inspection didn't damage the item causes your worry level to be
    # divided by three
    # and rounded down to the nearest integer.

    # each monkey takes a turn (round)
    for i in range(10000):
        # print(f"round {i}")
        for m in monkeies:
            # it inspects and throws all of the items it is holding one at a time and in the order listed
            # Monkey 0 goes first, then monkey 1, and so on until each monkey has had one turn
            # The process of each monkey taking a single turn is called a round.

            # monkey inspects and
            items = m.starting_items[::-1]
            while items:
                item_to_inspect = items.pop()

                # monkey inspects + applies operation to item
                inspected_item = m.operation(item_to_inspect)

                inspected_item %= level

                m.inspections += 1

                target_monkey = None
                if m.test(inspected_item):
                    target_monkey = monkies[m.if_true]
                else:
                    target_monkey = monkies[m.if_false]

                # print(
                #     f"monkey {m.identifier} throws {inspected_item} to monkey {target_monkey.identifier}"
                # )
                target_monkey.catch_item(inspected_item)
            m.starting_items = []
        # if i % 1000 == 0 or i == 20:
        #     print(f"round {i}")
        #     for m in monkeies:
        #         print(f"monkey {m.identifier} {m.inspections}")
    top_monkies = sorted([m.inspections for m in monkeies], reverse=True)
    print(top_monkies)
    return top_monkies[0] * top_monkies[1]


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day11/test_input")
    monkies = [parse_monkey(m) for m in test_vals]
    monkey_inspections(monkies) == 10605
    vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day11/input")
    monkies = [parse_monkey(m) for m in vals]
    print(monkey_inspections(monkies))

    print("# part 2------------------")
    monkies = [parse_monkey(m) for m in test_vals]
    level = prod([m.test_level for m in monkies])
    print(monkey_inspections_no_worries(monkies, level))

    monkies = [parse_monkey(m) for m in vals]
    level = prod([m.test_level for m in monkies])
    print(monkey_inspections_no_worries(monkies, level))
