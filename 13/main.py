import re
import sys

sys.path.append('../')
from shared import load_inputs


def parse_input(task_input: [str]) -> ({(int, int)}, [(str, int)], (int, int)):
    split_index = task_input.index('')
    dot_strings = task_input[:split_index]
    instructions_strings = task_input[split_index + 1:]
    instructions = []
    dots = set()

    for line in dot_strings:
        x, y = line.split(',')
        entry = (int(x), int(y))
        dots.add(entry)

    for instruction_line in instructions_strings:
        axis, line = re.match('fold along (\w)=(\d+)', instruction_line).groups()
        instructions.append((axis, int(line)))
    return dots, instructions


def print_board(dots, max_x, max_y):
    board_arr = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (x, y) in dots:
        board_arr[y][x] = '#'
    for line in board_arr:
        print(''.join(line))
    print()


def main():
    example_input, puzzle_input = load_inputs(__file__)
    dots, instructions = parse_input(puzzle_input)
    (max_x, max_y) = max([int(dot[0]) for dot in dots]), max([int(dot[1]) for dot in dots])
    dots_after_folding_once: None or int = None
    for axis, line in instructions:
        if axis == 'y':
            top_dots = set(filter(lambda entry: entry[1] < line, dots))
            bottom_dots = set(filter(lambda entry: entry[1] > line, dots))
            for dot in bottom_dots:
                (x, y) = dot
                top_dots.add((x, max_y - y))
            dots = top_dots
            max_y = int(max_y / 2) - 1
        elif axis == 'x':
            left_dots = set(filter(lambda entry: entry[0] < line, dots))
            right_dots = set(filter(lambda entry: entry[0] > line, dots))
            for dot in right_dots:
                (x, y) = dot
                left_dots.add((max_x - x, y))
            dots = left_dots
            max_x = int(max_x / 2) - 1
        if not dots_after_folding_once:
            dots_after_folding_once = len(dots)

    print(f'task 1: dots after folding once = {dots_after_folding_once}')
    print(f'task 2:')
    print_board(dots, max_x, max_y)


if __name__ == '__main__':
    main()
