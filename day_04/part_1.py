def create_rows(puzzle_input: str) -> list[list[str]]:
    return [list(line.strip()) for line in puzzle_input.strip().split('\n')]


def main(puzzle_input: str) -> int:
    term = 'XMAS'
    count = 0
    rows = create_rows(puzzle_input)
    starting_positions = [(i, j) for i in range(len(rows)) for j in range(len(rows[0])) if rows[i][j] == term[0]]

    for i, j in starting_positions:
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        candidates = [term[0]] * len(offsets)

        for n, candidate in enumerate(candidates):
            offset_i, offset_j = offsets[n]

            for m in range(1, len(term)):

                if i + m * offset_i not in range(len(rows)) or j + m * offset_j not in range(len(rows[0])):
                    break

                candidate = candidate + rows[i + m * offset_i][j + m * offset_j]

                if not term.startswith(candidate):
                    break

            if candidate == term:
                count += 1

    return count
