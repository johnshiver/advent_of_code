def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [int(l) for l in input_file.readlines()]


if __name__ == "__main__":
    print("# part 1------------------")
    test_vals = get_input("test_input")
