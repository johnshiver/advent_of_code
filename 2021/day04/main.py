from typing import Counter


def get_input(file_name):
    with open(file_name, "r") as input_file:
        return [l.rstrip("\n") for l in input_file.readlines()]


class BingoBoard:
    def __init__(self, vals) -> None:
        self.vals = vals
        self.final_score = -1

    @staticmethod
    def Build(raw_board):
        vals = {}
        n = len(raw_board)
        for x in range(n):
            for y in range(n):
                val = raw_board[y][x]
                vals[val] = (False, (x, y))
        return BingoBoard(vals)

    def make_move(self, val):
        if val in self.vals:
            # mark as seen
            seen, pos = self.vals[val]
            self.vals[val] = (True, pos)

    def completed(self):
        # get all seen moves
        # if there are 5 moves where x match, or 5 where y match, return true
        x_pos = Counter()
        y_pos = Counter()
        positions = [self.vals[x][1] for x in self.vals if self.vals[x][0]]
        for p in positions:
            x_pos[p[0]] += 1
            y_pos[p[1]] += 1
        for v in x_pos.values():
            if v > 4:
                return True
        for v in y_pos.values():
            if v > 4:
                return True

    def compute_score(self):
        # add up all unmarked vals
        return sum([int(v) for v in self.vals if not self.vals[v][0]])

    def set_final_score(self):
        if self.final_score >= 0:
            return
        if self.completed():
            self.final_score = self.compute_score()


def create_boards_and_moves(raw_input):
    moves = []
    boards = []
    curr_board = []
    for line in raw_input:
        if not moves and "," in line:
            moves = line.split(",")
            continue
        if line == "":
            if curr_board:
                boards.append(curr_board)
            curr_board = []
            continue
        line = [n for n in line.split(" ") if n]
        curr_board.append(line)
    if curr_board:
        boards.append(curr_board)

    boards = [BingoBoard.Build(b) for b in boards]
    return moves, boards


def evaluate_moves(moves, boards):
    for m in moves:
        for b in boards:
            b.make_move(m)
            if b.completed():
                # compute score for the board
                score = b.compute_score()
                return score * int(m)
    return -1


def evaluate_moves_part2(moves, boards):
    completed = []
    for m in moves:
        for b in boards:
            if len(completed) == len(boards):
                break
            if b in [x[0] for x in completed]:
                continue
            b.make_move(m)
            if b.completed():
                b.set_final_score()
                completed.append((b, m))
    if not completed:
        return -1
    board, move = completed[-1]
    return board.final_score * int(move)


if __name__ == "__main__":
    print("day 4 part 1")
    raw = get_input("test_input")
    test_moves, test_boards = create_boards_and_moves(raw)
    assert evaluate_moves(test_moves, test_boards) == 4512
    raw = get_input("input")
    moves, boards = create_boards_and_moves(raw)
    print(evaluate_moves(moves, boards))

    print("day 4 part 2")
    res = evaluate_moves_part2(test_moves, test_boards)
    assert res == 1924
    print(evaluate_moves_part2(moves, boards))
