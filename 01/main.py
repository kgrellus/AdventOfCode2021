import sys

sys.path.append('../')
from shared import load_inputs


def task1(task_input: [str]) -> int:
    depths = [int(line) for line in task_input]
    increases = 0
    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            increases += 1
    return increases


def task2(task_input: [str]) -> int:
    depths = [int(line) for line in task_input]
    increases = 0
    for i in range(0, len(depths) - 2):
        window = sum(depths[i:i + 3])
        next_window = sum(depths[i + 1:i + 4])
        if next_window > window:
            increases += 1
    return increases


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    print(f'task 1 (number of increases): {task1(puzzle_input)}')
    print(f'task 2 (number of increases of windows): {task2(puzzle_input)}')
