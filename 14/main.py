import re
import sys
import time

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
    unfinished_atoms: {Atom}

    def __init__(self, polymer_str):
        self.atoms = [Atom(char) for char in polymer_str]
        self.insertions = []
        self.atom_counts = {}
        self.unfinished_atoms = set()
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
        tic = time.perf_counter()
        self.insertions.sort(key=lambda x: x[0], reverse=True)
        toc = time.perf_counter()
        print(f"Sorting took {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        for index, atom in self.insertions:
            self.atoms.insert(index, atom)
        toc = time.perf_counter()
        print(f"Inserting took {toc - tic:0.4f} seconds")
        self.insertions = []

    def finish2(self):
        tic = time.perf_counter()
        toc = time.perf_counter()
        print(f"Sorting took {toc - tic:0.4f} seconds")
        tic = time.perf_counter()
        for atom in self.marked_atoms:
            atom.is
        toc = time.perf_counter()
        print(f"Inserting took {toc - tic:0.4f} seconds")
        self.insertions = []


def task1(task_input: [str]) -> int:
    polymer = Polymer(task_input[0])
    changes = task_input[2:]
    for i in range(40):
        print("index:", i)
        for change in changes:
            sequence, atom = re.match('(\w+) -> (\w)', change).groups()
            polymer.insert(sequence, atom)
        polymer.finish()
        # print(polymer)
    print(polymer.atom_counts)
    min_atoms, max_atoms = min(polymer.atom_counts.values()), max(polymer.atom_counts.values())
    return max_atoms - min_atoms


def task2(task_input: [str]) -> int:
    return 0


def main():
    example_input, puzzle_input = load_inputs(__file__)
    print(f'task 1: {task1(puzzle_input)}')
    print(f'task 2: {task2(example_input)}')


if __name__ == '__main__':
    main()
