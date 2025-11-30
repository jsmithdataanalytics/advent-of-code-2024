
def main(puzzle_input: str) -> int:
    disk = parse_input(puzzle_input)
    num_free_spaces = disk.count(None)
    num_used_spaces = len(disk) - num_free_spaces

    while True:

        while disk[-1] is None:
            disk.pop()

        if len(disk) == num_used_spaces:
            break

        disk[disk.index(None)] = disk.pop()

    return sum(i * n for i, n in enumerate(disk))


def parse_input(puzzle_input: str) -> list[int | None]:
    compressed = list(map(int, puzzle_input.strip()))
    decompressed = []
    file_id = 0

    for i, num in enumerate(compressed):

        if i % 2 == 0:
            decompressed.extend([file_id] * num)
            file_id += 1

        else:
            decompressed.extend([None] * num)

    return decompressed
