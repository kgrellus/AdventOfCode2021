import re
import sys
import time
from collections import defaultdict


sys.path.append('../')
from shared import load_inputs


class Atom:
    ignore: bool
    char: str

    def __init__(self, char):
        self.char = char
        self.ignore = False

    def __repr__(self):
        if self.ignore:
            return f'\033[93m{self.char}\033[0m'
        return self.char

    def __str__(self):
        if self.ignore:
            return f'\033[93m{self.char}\033[0m'
        return self.char


class Polymer:
    atoms: [Atom]
    atom_counts: dict
    insertions: []

    def __init__(self, polymer_str):
        self.atoms = [Atom(char) for char in polymer_str]
        self.insertions = []
        self.atom_counts = {}
        for atom in self.atoms:
            self.update_atom_count(atom.char)

    def __repr__(self):
        return ''.join([str(atom) for atom in self.atoms])

    def __str__(self):
        return ''.join([str(atom) for atom in self.atoms])

    def get_chain_str(self):
        return ''.join([atom.char for atom in self.atoms])

    def insert(self, sequence: str, atom: str):
        atom_str = self.get_chain_str()
        index = 0
        while index < len(atom_str):
            index = atom_str.find(sequence, index)
            if index != -1:
                self.insertions.append((index + 1, Atom(atom)))
                self.update_atom_count(atom)
                index += 1
            else:
                break

    def update_atom_count(self, atom: str):
        self.atom_counts[atom] = self.atom_counts[atom] + 1 if atom in self.atom_counts else 1

    def finish(self):
        self.insertions.sort(key=lambda x: x[0], reverse=True)
        for index, atom in self.insertions:
            self.atoms.insert(index, atom)
        self.insertions = []


def task1(task_input: [str]) -> int:
    polymer = Polymer(task_input[0])
    changes = task_input[2:]
    for _ in range(10):
        for change in changes:
            sequence, atom = re.match('(\w+) -> (\w)', change).groups()
            polymer.insert(sequence, atom)
        polymer.finish()
    min_atoms, max_atoms = min(polymer.atom_counts.values()), max(polymer.atom_counts.values())
    return max_atoms - min_atoms


def task2(task_input: [str]) -> int:
    polymer_str = task_input[0]
    changes_str = task_input[2:]
    changes = []
    for change in changes_str:
        changes.append(re.match('(\w+) -> (\w)', change).groups())
    adjacent_atoms = defaultdict(lambda: 0, {})
    for i in range(len(polymer_str) - 1):
        key = polymer_str[i] + polymer_str[i + 1]
        adjacent_atoms[key] += 1
    for _ in range(40):
        new_adjacent_atoms = defaultdict(lambda: 0, {})
        for sequence, atom in changes:
            if sequence in adjacent_atoms:
                a = sequence[0] + atom
                b = atom + sequence[1]
                new_adjacent_atoms[a] += adjacent_atoms[sequence]
                new_adjacent_atoms[b] += adjacent_atoms[sequence]
                adjacent_atoms.pop(sequence)
        adjacent_atoms = new_adjacent_atoms
    atom_counts = defaultdict(lambda: 0, {})
    atom_counts[polymer_str[0]] = 1
    atom_counts[polymer_str[-1]] = 1
    for sequence in adjacent_atoms:
        atom_counts[sequence[0]] += adjacent_atoms[sequence]
        atom_counts[sequence[1]] += adjacent_atoms[sequence]
    for key in atom_counts:
        atom_counts[key] = int(atom_counts[key]/2)  # because every character is in 2 sequences (left and right)
    min_atoms, max_atoms = min(atom_counts.values()), max(atom_counts.values())
    return max_atoms - min_atoms


def main():
    example_input, puzzle_input = load_inputs(__file__)
    tic = time.perf_counter()
    task1_solution = task1(puzzle_input)
    toc = time.perf_counter()
    print(f'task 1: with slow calculation (after 10 steps) = {task1_solution} after {toc - tic:0.4f} seconds')
    tic = time.perf_counter()
    task2_solution = task2(puzzle_input)
    toc = time.perf_counter()
    print(f'task 2: with fast calculation (after 40 steps) = {task2_solution} after {toc - tic:0.4f} seconds')


if __name__ == '__main__':
    main()
