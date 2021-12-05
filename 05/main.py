import re
import sys

sys.path.append('../')
from shared import load_inputs


def sum_points_with_overlaps(task_input: [str], ignore_diagonals: bool):
    vent_dict = dict()
    for line in task_input:
        [x1, y1, x2, y2] = [int(val) for val in re.match('(\d+),(\d+) -> (\d+),(\d+)', line).groups()]
        if not (x1 == x2 or y1 == y2):  # diagonal lines
            if not ignore_diagonals:
                if x2 >= x1:
                    if y2 >= y1:
                        for i in range(0, x2 - x1 + 1):
                            increase_vent_val(vent_dict, x1 + i, y1 + i)
                    else:
                        for i in range(0, x2 - x1 + 1):
                            increase_vent_val(vent_dict, x1 + i, y1 - i)
                else:
                    if y2 >= y1:
                        for i in range(0, x1 - x2 + 1):
                            increase_vent_val(vent_dict, x1 - i, y1 + i)
                    else:
                        for i in range(0, x1 - x2 + 1):
                            increase_vent_val(vent_dict, x1 - i, y1 - i)
            continue
        for x in range(x1, x2 + 1) if x2 >= x1 else range(x2, x1 + 1):  # straight lines
            for y in range(y1, y2 + 1) if y2 >= y1 else range(y2, y1 + 1):
                increase_vent_val(vent_dict, x, y)
    return sum(1 for line_count in vent_dict.values() if line_count > 1)


def increase_vent_val(vent_dict, x, y):
    key = f'{x},{y}'
    vent_dict[key] = vent_dict[key] + 1 if key in vent_dict else 1


def task1(task_input: [str]) -> int:
    return sum_points_with_overlaps(task_input, True)


def task2(task_input: [str]) -> int:
    return sum_points_with_overlaps(task_input, False)


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1 = task1(puzzle_input)
    task2 = task2(puzzle_input)
    print(f'task 1 points with at least 2 overlaps: {task1}')
    print(f'task 2 points with at least 2 overlaps: {task2}')
