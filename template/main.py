import sys

sys.path.append('../')
from shared import load_inputs


def task1(task_input: [str]) -> int:
    return 0


def task2(task_input: [str]) -> int:
    return 0


def main():
    example_input, puzzle_input = load_inputs(__file__)
    print(f'task 1: {task1(example_input)}')
    print(f'task 2: {task2(example_input)}')


if __name__ == '__main__':
    main()
