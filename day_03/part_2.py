import re


def main(puzzle_input: str) -> int:
    enabled = True
    total = 0
    instructions = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", puzzle_input)

    for instruction in instructions:

        if instruction == 'do()':
            enabled = True

        elif instruction == "don't()":
            enabled = False

        elif enabled:
            value_1, value_2 = re.findall(r'\d+', instruction)
            total += int(value_1) * int(value_2)

    return total
