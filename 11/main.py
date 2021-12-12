import sys

sys.path.append('../')
from shared import load_inputs


def task1(task_input: [str], steps: int) -> int:
    octopuses = [[int(val) for val in line] for line in task_input]
    flashes = 0
    for _ in range(steps):
        flashed_points = []
        for i in range(10):
            for j in range(10):
                octopuses[i][j] += 1
                if octopuses[i][j] == 10:
                    octopuses[i][j] = 0
                    flashes += 1
                    flashed_points.append((i, j))
        while len(flashed_points) > 0:
            for (i, j) in flashed_points.copy():
                flashed_points.remove((i, j))
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if 0 <= i + k < 10 and 0 <= j + l < 10 and octopuses[i + k][j + l] != 0 and not (k == 0 and l == 0):
                            octopuses[i + k][j + l] += 1
                            if octopuses[i + k][j+l] == 10:
                                octopuses[i+k][j+l] = 0
                                flashes += 1
                                flashed_points.append((i+k, j+l))
    return flashes


def task2(task_input: [str]) -> int:
    octopuses = [[int(val) for val in line] for line in task_input]
    steps = 0
    while sum([sum([octopus for octopus in line]) for line in octopuses]) != 0:
        flashed_points = []
        for i in range(10):
            for j in range(10):
                octopuses[i][j] += 1
                if octopuses[i][j] == 10:
                    octopuses[i][j] = 0
                    flashed_points.append((i, j))
        while len(flashed_points) > 0:
            for (i, j) in flashed_points.copy():
                flashed_points.remove((i, j))
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if 0 <= i + k < 10 and 0 <= j + l < 10 and octopuses[i + k][j + l] != 0 and not (k == 0 and l == 0):
                            octopuses[i + k][j + l] += 1
                            if octopuses[i + k][j+l] == 10:
                                octopuses[i+k][j+l] = 0
                                flashed_points.append((i+k, j+l))
        steps += 1
    return steps


def main():
    example_input, puzzle_input = load_inputs(__file__)
    steps = 100
    print(f'task 1: total flashes after {steps} steps = {task1(puzzle_input, steps)}')
    print(f'task 2: steps to synced flashes: {task2(puzzle_input)}')


if __name__ == '__main__':
    main()
