import re
import sys

sys.path.append('../')
from shared import load_inputs


def task1(instructions: [str]) -> (int, int):
    horizontal, depth = 0, 0
    for instruction in instructions:
        match = re.match('forward (\d+)', instruction)
        if match is not None:
            horizontal += int(match.group(1))
            continue
        match = re.match('down (\d+)', instruction)
        if match is not None:
            depth += int(match.group(1))
            continue
        match = re.match('up (\d+)', instruction)
        if match is not None:
            depth -= int(match.group(1))
            continue
    return horizontal, depth


def task2(instructions: [str]) -> (int, int):
    horizontal, depth, aim = 0, 0, 0
    for instruction in instructions:
        match = re.match('forward (\d+)', instruction)
        if match is not None:
            x = int(match.group(1))
            horizontal += x
            depth += aim * x
            continue
        match = re.match('down (\d+)', instruction)
        if match is not None:
            aim += int(match.group(1))
            continue
        match = re.match('up (\d+)', instruction)
        if match is not None:
            aim -= int(match.group(1))
            continue
    return horizontal, depth


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1_horizontal, task1_depth = task1(puzzle_input)
    print(f'task 1: horizontal:{task1_horizontal}, depth:{task1_depth}, solution:{task1_horizontal * task1_depth}')
    task2_horizontal, task2_depth = task2(puzzle_input)
    print(f'task 2: horizontal:{task2_horizontal}, depth:{task2_depth}, solution:{task2_horizontal * task2_depth}')
