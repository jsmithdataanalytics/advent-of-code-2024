import re


def main(puzzle_input: str) -> int:
    rules = [(int(string_1), int(string_2)) for string_1, string_2 in re.findall(r'(\d+)\|(\d+)', puzzle_input)]
    updates = [list(map(int, line.strip().split(','))) for line in puzzle_input.split('\n\n')[1].strip().split('\n')]

    assert all(a != b for a, b in rules)

    total = 0

    for update in updates:
        correct_order = True

        assert len(update) % 2 == 1
        assert len(update) == len(set(update))

        relevant_rules = [(a, b) for a, b in rules if a in update and b in update]

        for a, b in relevant_rules:

            if update.index(a) > update.index(b):
                correct_order = False
                break

        if correct_order:
            total += update[len(update) // 2]

    return total
