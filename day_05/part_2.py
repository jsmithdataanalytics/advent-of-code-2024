import re


def get_incorrectly_ordered_updates(puzzle_input: str) -> list[tuple[list[int], list[tuple[int, int]]]]:
    rules = [(int(string_1), int(string_2)) for string_1, string_2 in re.findall(r'(\d+)\|(\d+)', puzzle_input)]
    updates = [list(map(int, line.strip().split(','))) for line in puzzle_input.split('\n\n')[1].strip().split('\n')]

    incorrectly_ordered_updates = []

    for update in updates:
        correct_order = True

        relevant_rules = [(a, b) for a, b in rules if a in update and b in update]

        for a, b in relevant_rules:

            if update.index(a) > update.index(b):
                correct_order = False
                break

        if not correct_order:
            incorrectly_ordered_updates.append((update, relevant_rules))

    return incorrectly_ordered_updates


def sort(update: list[int], rules: list[tuple[int, int]]) -> list[int]:

    if len(update) == 1:
        return update

    predecessors = {a for a, b in rules}
    last_number = next(n for n in update if n not in predecessors)

    new_update = [n for n in update if n != last_number]
    new_rules = [(a, b) for a, b in rules if b != last_number]

    return sort(new_update, new_rules) + [last_number]


def main(puzzle_input: str) -> int:
    total = 0

    for update, rules in get_incorrectly_ordered_updates(puzzle_input):
        ordered_update = sort(update, rules)
        total += ordered_update[len(ordered_update) // 2]

    return total
