import re
import sys

sys.path.append('../')
from shared import load_inputs


class Cave:
    name: str
    is_small: bool
    visits: int
    neighbours: set

    def __init__(self, name: str):
        self.name = name
        self.is_small = name.islower()
        self.visits = 0
        self.neighbours = set()

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        if self.cannot_be_visited_anymore():
            return f'{self.name} (finished)'
        return f'{self.name}'

    def cannot_be_visited_anymore(self):
        return self.is_small and self.visits >= 1


def prepare_caves(task_input):
    caves: {Cave} = set()
    edges = []
    for line in task_input:
        a, b = re.match('(\w+)-(\w+)', line).groups()
        edges.append((a, b))
        caves = caves | {Cave(a), Cave(b)}
    for edge_from, edge_to in edges:
        from_cave = next(x for x in caves if x.name == edge_from)
        to_cave = next(x for x in caves if x.name == edge_to)
        from_cave.neighbours.add(to_cave)
        to_cave.neighbours.add(from_cave)
    return caves


def get_recursive_paths(cave: Cave, double_visit_used: bool):
    if cave.name == 'end':
        return 1
    if cave.name == 'start' and cave.cannot_be_visited_anymore():
        return 0
    if cave.cannot_be_visited_anymore() and double_visit_used:
        return 0
    paths = 0
    if cave.cannot_be_visited_anymore() and not double_visit_used:
        cave.visits += 1
        for neighbour in cave.neighbours:
            paths += get_recursive_paths(neighbour, True)
        cave.visits -= 1
    else:
        cave.visits += 1
        for neighbour in cave.neighbours:
            paths += get_recursive_paths(neighbour, double_visit_used)
        cave.visits -= 1
    return paths


def main():
    example_input, puzzle_input = load_inputs(__file__)
    caves = prepare_caves(puzzle_input)
    start_cave = next(x for x in caves if x.name == 'start')
    print(f'task 1: paths through caves = {get_recursive_paths(start_cave, True)}')
    print(f'task 2: paths through caves = {get_recursive_paths(start_cave, False)}')


if __name__ == '__main__':
    main()
