file_path = 'input.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

    # seperate file into list
    seperate_lines = []
    for line in lines:
        if line.endswith('\n'):
            seperate_lines.append(line[:-2])

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
    total = 0

    for line in seperate_lines:
        
        digits = [char for char in line if char.isdigit()]

        if len(digits) >= 2:
            first_last_combined = int(digits[0] + digits[-1])

            total += first_last_combined


    print(total)
