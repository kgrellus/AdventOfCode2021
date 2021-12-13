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


def get_dimensions(dots):
    return max([int(dot[0]) for dot in dots]), max([int(dot[1]) for dot in dots])


def task1(task_input: [str]) -> int:
    dots, instructions = parse_input(task_input)
    (max_x, max_y) = get_dimensions(dots)
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
            print(max_x)
            max_x = int(max_x / 2) - 1
            print(max_x)
        print_board(dots, max_x, max_y)
    return len(dots)


def print_board(dots, max_x, max_y):
    map_ = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for (x, y) in dots:
        map_[y][x] = '#'
    for line in map_:
        print(''.join(line))
    print()


def main():
    example_input, puzzle_input = load_inputs(__file__)

    dots, instructions = parse_input(puzzle_input)
    (max_x, max_y) = get_dimensions(dots)
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

    print(f'task 1: dots after folding {len(dots)}')
    print(f'task 2: read from console:\n')
    print_board(dots, max_x, max_y)


if __name__ == '__main__':
    main()
