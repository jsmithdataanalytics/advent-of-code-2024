def is_gradual_increase(value_1: int, value_2: int) -> bool:
    return value_1 < value_2 <= value_1 + 3


def is_gradual_decrease(value_1: int, value_2: int) -> bool:
    return value_1 - 3 <= value_2 < value_1


def main(puzzle_input: str) -> int:
    lines = puzzle_input.strip().split('\n')
    reports = [list(map(int, line.strip().split())) for line in lines]

    count = 0

    for report in reports:

        if is_gradual_increase(report[0], report[1]):
            condition = is_gradual_increase

        elif is_gradual_decrease(report[0], report[1]):
            condition = is_gradual_decrease

        else:
            continue

        if all(condition(value_1, value_2) for value_1, value_2 in zip(report, report[1:])):
            count += 1

    return count
