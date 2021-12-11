import sys
import math

sys.path.append('../')
from shared import load_inputs


def prepare_heightmap(task_input: [str]) -> [[int]]:
    heightmap = []
    for line in task_input:
        heightmap.append([int(num) for num in line])
    return heightmap


def size_of_branch(visited_points: [(int, int)], start_point: (int, int), heightmap: [[int]]):
    col, row = start_point
    if not 0 <= col < max_col or not 0 <= row < max_row:
        return 0
    if (col, row) in visited_points:
        return 0
    if heightmap[col][row] == 9:
        return 0
    visited_points.append((col, row))
    return 1 + size_of_branch(visited_points, (col + 1, row), heightmap) + \
           size_of_branch(visited_points, (col - 1, row), heightmap) + \
           size_of_branch(visited_points, (col, row + 1), heightmap) + \
           size_of_branch(visited_points, (col, row - 1), heightmap)


def task1(heightmap: [[int]]) -> (int, [(int, int)]):
    risk = 0
    points = []
    for col in range(max_col):
        for row in range(max_row):
            point = heightmap[col][row]
            # print(f'({col},{row}) = {point}')
            if (col == 0 or point < heightmap[col - 1][row]) and (
                    col == max_col - 1 or point < heightmap[col + 1][row]) and (
                    row == 0 or point < heightmap[col][row - 1]) and (
                    row == max_row - 1 or point < heightmap[col][row + 1]):
                points.append((col, row))
                risk += 1 + point
    return risk, points


def task2(heightmap: [[int]], starting_points: [(int, int)]) -> int:
    basin_sizes = []
    for starting_point in starting_points:
        basin_sizes.append(size_of_branch([], starting_point, heightmap))

    basin_sizes.sort()

    return math.prod(basin_sizes[-3:])


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    map_ = prepare_heightmap(puzzle_input)
    max_col, max_row = len(map_), len(map_[0])
    task1, low_points = task1(map_)
    task2 = task2(map_, low_points)
    print(f'task 1: risk = {task1}')
    print(f'task 2: 3 biggest basin sizes multiplied: {task2}')
