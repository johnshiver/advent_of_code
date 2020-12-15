import re


FIND_BAGS = re.compile(r"([a-z]+ [a-z]+) bag")
FIND_BAG_COUNTS = re.compile(r"([\d]) [a-z]+ [a-z]+ bag")

# create graph
def get_input(file_name):
    graph = {}
    with open(file_name, "r") as f:
        for l in f.readlines():
            l = l.rstrip("\n")
            node, *children = re.findall(FIND_BAGS, l)
            counts = re.findall(FIND_BAG_COUNTS, l)
            counts = [int(i) for i in counts]
            child_counts = {
                children[i]: counts[i]
                for i in range(len(children))
                if children[i] != "no other"
            }
            graph[node] = child_counts
    return graph


def find_bag(graph, target="shiny gold"):
    count = 0
    for b in graph:
        if b == target:
            continue
        stack = [b]
        bag_count = 0
        while stack:
            curr = stack.pop()
            if curr not in graph:
                continue
            if curr == target:
                print("found target, starting from ", b)
                count += 1
                break
            # account for 'no other'
            children = graph[curr]["children"]
            stack.extend(children)
    return count


def get_total_bags(graph, bag):
    if bag not in graph:
        return 0
    curr_children = graph[bag]
    if not curr_children:
        return 1
    count = 0
    for child, child_count in curr_children.items():
        count += child_count * get_total_bags(graph, child)
    return 1 + count


if __name__ == "__main__":
    bag_graph = get_input("input")
    print(get_total_bags(bag_graph, "shiny gold"))
    # bag_graph = get_input("input")
    # print(find_bag_count(bag_graph))
