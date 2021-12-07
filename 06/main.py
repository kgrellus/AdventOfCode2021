import sys

sys.path.append('../')
from shared import load_inputs


def task1(task_input: [str], days: int) -> int:  # slow way
    fish_swarm = [int(val) for val in task_input[0].split(',')]
    for _ in range(days):
        for i in range(len(fish_swarm)):
            if fish_swarm[i] == 0:
                fish_swarm.append(8)
                fish_swarm[i] = 6
            else:
                fish_swarm[i] = fish_swarm[i] - 1
    return len(fish_swarm)


def task2(task_input: [str], days: int) -> int:  # fast way
    fish_swarm = [int(val) for val in task_input[0].split(',')]
    fish_day_counts = [0 for _ in range(9)]
    for fish in fish_swarm:
        fish_day_counts[fish] += 1
    for i in range(days):
        fish_day_0 = fish_day_counts.pop(0)
        fish_day_counts.append(fish_day_0)
        fish_day_counts[6] += fish_day_0
    return sum(fish_day_counts)


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1_days = 80
    task2_days = 256
    task1 = task1(puzzle_input, task1_days)
    task2 = task2(puzzle_input, task2_days)
    print(f'task 1: fish after {task1_days} days: {task1}')
    print(f'task 2: fish after {task2_days} days: {task2}')
