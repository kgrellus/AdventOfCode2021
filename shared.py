import os


def load_inputs(script_pwd):
    print(script_pwd)
    path = os.path.dirname(os.path.realpath(script_pwd))
    with open(f'{path}/example-input', "r") as file:
        example_input = list((line.strip() for line in file.readlines()))
    with open(f'{path}/input', "r") as file:
        puzzle_input = list((line.strip() for line in file.readlines()))
    return example_input, puzzle_input

