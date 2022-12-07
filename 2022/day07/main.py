from collections import namedtuple


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


class Tree:
    def __init__(self, name, parent=None):
        self.parent = parent
        self.children = dict()
        self.files = list()
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}-{[c.name for c in self.children]}"

    def size(self):
        file_sizes = sum(c[0] for c in self.files)
        dir_sizes = sum(c.size() for c in self.children.values())
        return file_sizes + dir_sizes


def create_fs_from_terminal_output(terminal_output):
    root = Tree("/")
    curr_level = root
    for line in terminal_output:
        # commands
        if line.startswith("$"):
            parts = line.split(" ")
            cmd = parts[1]
            match cmd:
                case "cd":
                    target = parts[2]
                    if target == "/":
                        curr_level = root
                        continue
                    elif target == "..":
                        curr_level = curr_level.parent
                        continue
                    else:
                        curr_level = curr_level.children[target]
                        continue
                case "ls":
                    continue
        # we are listing directory
        else:
            parts = line.split(" ")
            if parts[0].isdigit():
                curr_level.files.append((int(parts[0]), parts[1]))
            else:
                curr_level.children[parts[1]] = Tree(parts[1], parent=curr_level)
    return root


def gather_dir_sizes(file_system_root):
    sizes = []
    stack = [file_system_root]
    while stack:
        curr = stack.pop()
        sizes.append(curr.size())
        for c in curr.children.values():
            stack.append(c)
    return sizes


def find_smallest_to_delete(sizes):
    system_memory = 70000000
    current_free = system_memory - sizes[0]

    target_free = 30000000

    sizes = sorted(sizes)
    for s in sizes:
        if current_free + s >= target_free:
            return s
    return -1


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day07/test_input")
    root = create_fs_from_terminal_output(test_vals)
    sizes = gather_dir_sizes(root)
    assert sum([s for s in sizes if s <= 100000]) == 95437

    vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day07/input")
    root = create_fs_from_terminal_output(vals)
    sizes = gather_dir_sizes(root)
    print(sum([s for s in sizes if s <= 100000]))

    print("# part 2------------------")

    root = create_fs_from_terminal_output(test_vals)
    sizes = gather_dir_sizes(root)
    assert find_smallest_to_delete(sizes) == 24933642

    root = create_fs_from_terminal_output(vals)
    sizes = gather_dir_sizes(root)
    print(find_smallest_to_delete(sizes))
