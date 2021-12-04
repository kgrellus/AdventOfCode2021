from shared import load_inputs


def binary_string_to_int(binary_string: str) -> int:
    int_value = 0
    for index, char in enumerate(reversed(binary_string)):
        if char == '1':
            int_value += pow(2, index)
    return int_value


def task1(task_input: [str]) -> (int, int):
    total_binaries = len(task_input)
    one_counts = [0 for _ in task_input[0]]
    for binary in task_input:
        for index, bit in enumerate(binary):
            if bit == '1':
                one_counts[index] += 1
    gamma_str, epsilon_str = '', ''
    for one_count in one_counts:
        if one_count > total_binaries / 2:
            gamma_str += '1'
            epsilon_str += '0'
        else:
            gamma_str += '0'
            epsilon_str += '1'
    gamma, epsilon = binary_string_to_int(gamma_str), binary_string_to_int(epsilon_str)
    return gamma, epsilon


def task2(task_input: [str]) -> (int, int):
    relevant_binaries_oxygen, relevant_binaries_co2 = task_input, task_input
    considered_bit = 0
    while len(relevant_binaries_oxygen) > 1 or len(relevant_binaries_co2) > 1:
        one_counts_oxygen, one_counts_co2 = 0, 0
        for binary in relevant_binaries_oxygen:
            if binary[considered_bit] == '1':
                one_counts_oxygen += 1
        for binary in relevant_binaries_co2:
            if binary[considered_bit] == '1':
                one_counts_co2 += 1
        if len(relevant_binaries_oxygen) > 1:
            zero_counts_oxygen = len(relevant_binaries_oxygen) - one_counts_oxygen
            correct_char_oxygen = '1' if one_counts_oxygen >= zero_counts_oxygen else '0'
            relevant_binaries_oxygen = list(filter(lambda binary_str: binary_str[considered_bit] == correct_char_oxygen, relevant_binaries_oxygen))
        if len(relevant_binaries_co2) > 1:
            zero_counts_co2 = len(relevant_binaries_co2) - one_counts_co2
            correct_char_co2 = '0' if zero_counts_co2 <= one_counts_co2 else '1'
            relevant_binaries_co2 = list(filter(lambda binary_str: binary_str[considered_bit] == correct_char_co2, relevant_binaries_co2))
        considered_bit += 1

    oxygen_gen_rating = binary_string_to_int(relevant_binaries_oxygen[0])
    co2_scrub_rating = binary_string_to_int(relevant_binaries_co2[0])
    return oxygen_gen_rating, co2_scrub_rating


if __name__ == '__main__':
    example_input, puzzle_input = load_inputs(__file__)
    task1_gamma, task1_epsilon = task1(puzzle_input)
    print(f'task 1: epsilon:{task1_epsilon}, gamma:{task1_gamma}, solution:{task1_epsilon * task1_gamma}')
    task2_oxygen, task2_co2 = task2(puzzle_input)
    print(f'task 2: oxygen generator rating:{task2_oxygen}, CO2 scrubber rating:{task2_co2}, solution:{task2_co2 * task2_oxygen}')
