import sys

sys.path.append('../')
from shared import load_inputs


def triangular_number(n: int) -> int:
    return int(abs(n) * (abs(n) + 1) / 2)


def task1(task_input: [str]) -> int:
    crab_positions = [int(val) for val in task_input[0].split(',')]
    min_pos, max_pos = min(crab_positions), max(crab_positions)
    min_sum = max_pos * len(crab_positions)
    for i in range(min_pos, max_pos):
        act_sum = sum([abs(val - i) for val in crab_positions])
        if act_sum < min_sum:
            min_sum = act_sum

    return min_sum


def task2(task_input: [str]) -> int:
    crab_positions = [int(val) for val in task_input[0].split(',')]
    min_pos, max_pos = min(crab_positions), max(crab_positions)
    min_sum = triangular_number(max_pos * len(crab_positions))
    for i in range(min_pos, max_pos):
        act_sum = sum([triangular_number(abs(val - i)) for val in crab_positions])
        if act_sum < min_sum:
            min_sum = act_sum
    return min_sum


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1 = task1(puzzle_input)
    task2 = task2(puzzle_input)
    print(f'task 1: fuel used: {task1}')
    print(f'task 2: fuel used: {task2}')
