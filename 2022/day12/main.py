def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [list(l) for l in input_file.read().split("\n")]

def find_shortest_path(grid):
    # find starting position
    for i, row in enumerate(grid):
        if "S" in row:
            
        if "E" in row:

    # find end position


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day12/test_input")
    print(test_vals)

    # vals = get_input("/Users/jshiver/projects/advent_of_code/2022/day12/input")

    print("# part 2------------------")
