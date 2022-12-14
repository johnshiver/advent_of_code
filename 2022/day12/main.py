from collections import namedtuple
from string import ascii_lowercase
from collections import defaultdict
import heapq as heap

pos = namedtuple("pos", ["x", "y"])


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [list(l) for l in input_file.read().split("\n")]


def print_grid(grid):
    print("\n".join([" ".join([str(cell) for cell in row]) for row in grid]))
    divider = "-" * 2 * (len(grid[0]))
    print(divider)
    print()


def get_starting_pos(grid):
    # find starting position
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    for y, row in enumerate(grid):
        if "S" in row:
            start_x = row.index("S")
            start_y = y
        if "E" in row:
            end_x = row.index("E")
            end_y = y

    return pos(start_x, start_y), pos(end_x, end_y)


def can_move(grid, x_pos: pos, y_pos: pos):
    if not (0 <= x_pos.x < len(grid[0]) and 0 <= x_pos.y < len(grid)):
        return False
    if not (0 <= y_pos.x < len(grid[0]) and 0 <= y_pos.y < len(grid)):
        return False
    x = grid[x_pos.y][x_pos.x]
    y = grid[y_pos.y][y_pos.x]
    if x == "S":
        return True
    if y == "S":
        return False
    if y == "E":
        return x == "z"
    return (ascii_lowercase.find(y) - ascii_lowercase.find(x)) <= 1


def distance(x, y):
    return abs(y.x - x.x) + abs(y.y - x.y)


def create_graph(grid):
    """
    want dictionary of tuples (node, weight)
    """
    graph = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            graph[pos(x, y)] = dict()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            curr = graph[pos(x, y)]
            up = pos(x, y - 1)
            down = pos(x, y + 1)
            left = pos(x - 1, y)
            right = pos(x + 1, y)
            for adj in (up, down, left, right):
                # add connections if we can move there
                if can_move(grid, pos(x, y), adj):
                    # for now, all weights are 1
                    curr[adj] = 1
    return graph


def dijkstra(graph, starting_node, end_node):
    visited = set()
    parents_map = {}
    pq = []
    node_costs = defaultdict(lambda: float("inf"))
    node_costs[starting_node] = 0
    heap.heappush(pq, (0, starting_node))

    while pq:
        # go greedily by always extending the shorter cost nodes first
        _, node = heap.heappop(pq)
        visited.add(node)

        # after this is working, add in this short circuit
        # we are done
        # if node == end_node:

        for adj_node, weight in graph[node].items():
            if adj_node in visited:
                continue

            new_cost = node_costs[node] + weight
            if node_costs[adj_node] > new_cost:
                parents_map[adj_node] = node
                node_costs[adj_node] = new_cost
                heap.heappush(pq, (new_cost, adj_node))

    return parents_map, node_costs


if __name__ == "__main__":
    print("# part 1------------------")

    t_grid = get_input("/Users/jshiver/projects/advent_of_code/2022/day12/test_input")
    print_grid(t_grid)
    graph = create_graph(t_grid)
    start, end = get_starting_pos(t_grid)
    parents, costs = dijkstra(graph, start, end)
    assert costs[end] == 31

    t_grid = get_input("/Users/jshiver/projects/advent_of_code/2022/day12/input")
    graph = create_graph(t_grid)
    start, end = get_starting_pos(t_grid)
    parents, costs = dijkstra(graph, start, end)
    print(costs[end])

    print("# part 2------------------")
