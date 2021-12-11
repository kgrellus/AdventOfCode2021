import sys

sys.path.append('../')
from shared import load_inputs


def get_closing_character(opening_char: str):
    if opening_char == '(':
        return ')'
    if opening_char == '{':
        return '}'
    if opening_char == '[':
        return ']'
    if opening_char == '<':
        return '>'


def get_syntax_checker_score(closing_char: str):
    if closing_char == ')':
        return 3
    if closing_char == ']':
        return 57
    if closing_char == '}':
        return 1197
    if closing_char == '>':
        return 25137


def get_autocomplete_tool_score(closing_char: str):
    if closing_char == ')':
        return 1
    if closing_char == ']':
        return 2
    if closing_char == '}':
        return 3
    if closing_char == '>':
        return 4


def is_opening_character(char: str):
    return char in '([{<'


def task1(task_input: [str]) -> (int, [str]):
    syntax_checker_score = 0
    incomplete_lines = []
    for line in task_input:
        opened_chunks = []
        line_score = 0
        for char in line:
            if is_opening_character(char):
                opened_chunks.append(char)
            elif len(opened_chunks) > 0 and get_closing_character(opened_chunks[-1]) == char:
                opened_chunks.pop()
            else:
                line_score += get_syntax_checker_score(char)
                break
        if line_score == 0:
            incomplete_lines.append(line)
        else:
            syntax_checker_score += line_score
    return syntax_checker_score, incomplete_lines


def task2(incomplete_lines: [str]) -> int:
    autocomplete_scores = []
    for line in incomplete_lines:
        opened_chunks = []
        for char in line:
            if is_opening_character(char):
                opened_chunks.append(char)
            elif len(opened_chunks) > 0 and get_closing_character(opened_chunks[-1]) == char:
                opened_chunks.pop()
        autocomplete_str = ''.join([get_closing_character(char) for char in reversed(opened_chunks)])
        score = 0
        for char in autocomplete_str:
            score *= 5
            score += get_autocomplete_tool_score(char)
        autocomplete_scores.append(score)
    autocomplete_scores.sort()
    return autocomplete_scores[int(len(autocomplete_scores)/2)]


def main():
    example_input, puzzle_input = load_inputs(__file__)
    task1_score, incomplete_lines = task1(puzzle_input)
    print(f'task 1: total syntax error score = {task1_score}')
    print(f'task 2: auto complete tool middle score: {task2(incomplete_lines)}')


if __name__ == '__main__':
    main()
