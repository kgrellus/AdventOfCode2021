import sys
import numpy as np

sys.path.append('../')
from shared import load_inputs


def extract_value_by_occurrences(str1: str, str2: str, expected_count) -> str:
    lst = str1 + str2
    for char in lst:
        if lst.count(char) == expected_count:
            return char
    raise ValueError


def check_occurrence_of_all_indexes(segments_arr: np.array, indexes: [int], input_chars: str) -> bool:
    return all([char in list(segments_arr[indexes]) for char in input_chars])


def str_to_digit(segments: [str], input_chars: str) -> str:
    a = np.array(segments)
    if check_occurrence_of_all_indexes(a, [[2, 5]], input_chars):
        return '1'
    if check_occurrence_of_all_indexes(a, [[0, 2, 5]], input_chars):
        return '7'
    if check_occurrence_of_all_indexes(a, [[1, 2, 3, 5]], input_chars):
        return '4'
    if check_occurrence_of_all_indexes(a, [[0, 2, 3, 4, 6]], input_chars):
        return '2'
    if check_occurrence_of_all_indexes(a, [[0, 2, 3, 5, 6]], input_chars):
        return '3'
    if check_occurrence_of_all_indexes(a, [[0, 1, 3, 5, 6]], input_chars):
        return '5'
    if check_occurrence_of_all_indexes(a, [[0, 1, 2, 4, 5, 6]], input_chars):
        return '0'
    if check_occurrence_of_all_indexes(a, [[0, 1, 3, 4, 5, 6]], input_chars):
        return '6'
    if check_occurrence_of_all_indexes(a, [[0, 1, 2, 3, 5, 6]], input_chars):
        return '9'
    if check_occurrence_of_all_indexes(a, [[0, 1, 2, 3, 4, 5, 6]], input_chars):
        return '8'

    print(segments, input_chars)
    raise ValueError


def task1(task_input: [str]) -> int:
    digits_entry = [split_line[split_line.index("|") + 1:] for split_line in [line.split(" ") for line in task_input]]
    count_simple_values = sum([len([0 for digit in digits if len(digit) in [2, 4, 3, 7]]) for digits in digits_entry])
    return count_simple_values


def task2(task_input: [str]) -> int:
    digits_entry_pairs = [(split_line[:split_line.index("|")], split_line[split_line.index("|") + 1:]) for split_line in
                          [line.split(" ") for line in task_input]]
    total_sum = 0
    for (signal_patterns, digits) in digits_entry_pairs:
        # be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
        seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g = ['' for _ in range(7)]
        line_str = ''.join(signal_patterns)
        signal_patterns.sort(key=lambda x: len(x))
        seg_a = extract_value_by_occurrences(signal_patterns[0], signal_patterns[1], 1)

        for char in signal_patterns[0]:
            char_count_in_line = line_str.count(char)
            if char_count_in_line == 8:
                seg_c = char
            elif char_count_in_line == 9:
                seg_f = char

        digit_4: str = signal_patterns[2]
        digit_4 = digit_4.replace(seg_c, '')
        digit_4 = digit_4.replace(seg_f, '')
        for char in digit_4:
            char_count_in_line = line_str.count(char)
            if char_count_in_line == 6:
                seg_b = char
            elif char_count_in_line == 7:
                seg_d = char

        line_str = line_str.replace(seg_a, '')
        line_str = line_str.replace(seg_b, '')
        line_str = line_str.replace(seg_c, '')
        line_str = line_str.replace(seg_d, '')
        line_str = line_str.replace(seg_f, '')
        for char in line_str:
            char_count_in_line = line_str.count(char)
            if char_count_in_line == 4:
                seg_e = char
            elif char_count_in_line == 7:
                seg_g = char

        output = ''
        for digit in digits:
            output += str_to_digit([seg_a, seg_b, seg_c, seg_d, seg_e, seg_f, seg_g], digit)
        total_sum += int(output)
    return total_sum


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1 = task1(puzzle_input)
    task2 = task2(puzzle_input)
    print(f'task 1: count of (1,4,7,8): {task1}')
    print(f'task 2: sum of all numbers: {task2}')
