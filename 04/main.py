import re
import sys

sys.path.append('../')
from shared import load_inputs


class Entry:
    value: int
    marked: bool
    is_winning: bool

    def __init__(self, value: int):
        self.value = value
        self.marked = False
        self.is_winning = False

    def mark(self):
        self.marked = True

    def __repr__(self):
        if self.marked:
            if self.is_winning:
                return f'\033[92m{self.value}\033[0m'
            return f'\033[93m{self.value}\033[0m'
        return f'{self.value}'


class Board:
    board: [[Entry]]

    def __init__(self, string_rows: [str]):
        self.board = []
        for row in string_rows:
            self.board.append([Entry(int(char)) for char in re.split('\s+', row)])

    def __repr__(self) -> str:
        representation = '\n'
        for row in self.board:
            for entry in row:
                if entry.value < 10:
                    representation += ' '
                representation += f'{entry} '
            representation += '\n'
        return representation

    def mark(self, value: int):
        for row in self.board:
            for entry in row:
                if entry.value == value:
                    entry.mark()

    def finished(self) -> bool:
        # if all([self.board[i][i].marked for i in range(0, len(self.board))]):
        #     return True
        # if all([self.board[len(self.board) - 1 - i][i].marked for i in range(0, len(self.board))]):
        #     return True
        for i in range(0, len(self.board)):
            if all([entry.marked for entry in self.board[i]]):
                for entry in self.board[i]:
                    entry.is_winning = True
                return True
            if all([entry.marked for entry in [self.board[j][i] for j in range(0, len(self.board[i]))]]):
                for j in range(0, len(self.board[i])):
                    self.board[j][i].is_winning = True
                return True

        return False

    def unmarked_sum(self) -> int:
        return sum([sum([entry.value for entry in row if not entry.marked]) for row in self.board])


def init_board(task_input: [str]) -> ([int], [Board]):
    number_seq = [int(val) for val in task_input[0].split(',')]
    boards = []
    task_input = task_input[1:]
    task_input = [val for val in task_input if val != '']
    for i in range(0, int(len(task_input) / 5)):
        boards.append(Board(task_input[5 * i:5 * i + 5]))
    return number_seq, boards


def task1(task_input: [str]) -> (int, int):
    number_seq, boards = init_board(task_input)
    for drawn_number in number_seq:
        for board in boards:
            board.mark(drawn_number)
            if board.finished():
                print('first winning board:', board)
                return board.unmarked_sum(), drawn_number
    raise ValueError('no board has won, check inputs!')


def task2(task_input: [str]) -> (int, int):
    number_seq, boards = init_board(task_input)
    winning_board = None
    for drawn_number in number_seq:
        i = 0
        while i < len(boards):
            board = boards[i]
            board.mark(drawn_number)
            if board.finished():
                if len(boards) > 1:
                    boards.remove(board)
                    continue
                else:
                    winning_board = board
            i += 1
        if winning_board:
            print('last winning board:', winning_board)
            return winning_board.unmarked_sum(), drawn_number
    raise ValueError('no board has won, check inputs!')


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1_sum_unmarked_numbers, task1_winning_number = task1(puzzle_input)
    task2_sum_unmarked_numbers, task2_winning_number = task2(puzzle_input)
    print(
        f'task 1: sum of unmarked numbers:{task1_sum_unmarked_numbers}, winning_number:{task1_winning_number}, solution:{task1_sum_unmarked_numbers * task1_winning_number}')
    print()
    print(
        f'task 2: sum of unmarked numbers:{task2_sum_unmarked_numbers}, winning_number:{task2_winning_number}, solution:{task2_sum_unmarked_numbers * task2_winning_number}')
