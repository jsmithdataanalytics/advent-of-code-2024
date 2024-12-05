import re


def main(puzzle_input: str) -> int:
    mul_instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', puzzle_input)

    return sum(int(value_1) * int(value_2) for value_1, value_2 in mul_instructions)
