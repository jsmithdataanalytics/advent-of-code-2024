from itertools import product


def main(puzzle_input: str) -> int:
    return solve(puzzle_input, include_third_op=False)


def solve(puzzle_input: str, include_third_op: bool) -> int:
    equations = parse_input(puzzle_input)

    total = 0

    for test_value, numbers in equations:

        if is_solvable(test_value, numbers, include_third_op):
            total += test_value

    return total


def parse_input(puzzle_input: str) -> list[tuple[int, list[int]]]:
    lines = [line.strip() for line in puzzle_input.split('\n') if line.strip()]

    equations = []

    for line in lines:
        lhs, rhs = line.split(':')
        test_value = int(lhs.strip())
        numbers = list(map(int, rhs.strip().split()))

        equations.append((test_value, numbers))

    return equations


def is_solvable(test_value: int, numbers: list[int], include_third_op: bool) -> bool:
    ops = [0, 1, 2] if include_third_op else [0, 1]
    op_sequences = product(ops, repeat=len(numbers) - 1)

    for op_sequence in op_sequences:
        answer = evaluate(numbers, op_sequence)

        if answer == test_value:
            return True

    return False


def evaluate(numbers: list[int], op_sequence: tuple[int]) -> int:
    answer = 0
    op_sequence = [0] + list(op_sequence)

    for number, op in zip(numbers, op_sequence):

        if op == 0:
            answer += number

        elif op == 1:
            answer *= number

        else:
            answer = int(str(answer) + str(number))

    return answer
