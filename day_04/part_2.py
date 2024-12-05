from day_04.part_1 import create_rows


def main(puzzle_input: str) -> int:
    count = 0
    rows = create_rows(puzzle_input)
    starting_positions = [(i, j) for i in range(len(rows)) for j in range(len(rows[0])) if rows[i][j] == 'A']

    for i, j in starting_positions:
        too_close_to_edge = False

        offsets_1 = [(-1, -1), (1, 1)]
        offsets_2 = [(1, -1), (-1, 1)]

        for offsets in [offsets_1, offsets_2]:
            for offset_i, offset_j in offsets:

                if i + offset_i not in range(len(rows)) or j + offset_j not in range(len(rows[0])):
                    too_close_to_edge = True

        if too_close_to_edge:
            continue

        word_1 = {rows[i + offset_i][j + offset_j] for offset_i, offset_j in offsets_1}
        word_2 = {rows[i + offset_i][j + offset_j] for offset_i, offset_j in offsets_2}

        if word_1 == word_2 == {'S', 'M'}:
            count += 1

    return count
