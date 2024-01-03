file_path = 'input.txt'

text_to_num = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

def replace_number_with_word(string):
    for word, number in text_to_num.items():
        string = string.replace(str(number), word)
    return string


def string_to_number(string):
    substring_with_indices = []

    for word in text_to_num.keys():
        index = string.find(word)

        while index != -1:
            substring_with_indices.append((word, index))
            index = string.find(word, index + 1)

    substring_with_indices.sort(key=lambda x: x[1])

    substrings_translated = [text_to_num[word] for word, _ in substring_with_indices]
    return substrings_translated


def solution():
    second_sum_of_digit = 0

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            string = replace_number_with_word(line)
            digit = string_to_number(string)

            first_digit = digit[0]
            last_digit = digit[-1]
            final_digit = first_digit * 10 + last_digit

            second_sum_of_digit += final_digit

    return second_sum_of_digit


solution()
