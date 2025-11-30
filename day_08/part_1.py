from dataclasses import dataclass
from itertools import product
from math import gcd


@dataclass
class Antenna:
    i: int
    j: int
    frequency: str


def main(puzzle_input: str) -> int:
    return solve(puzzle_input, use_new_model=False)


def solve(puzzle_input: str, use_new_model: bool) -> int:

    map_size_i, map_size_j, antennas = parse_input(puzzle_input)

    antinodes = set()

    for a, b in product(antennas, antennas):

        if a == b:
            continue

        if a.frequency == b.frequency:

            if use_new_model:
                step_i, step_j = b.i - a.i, b.j - a.j
                divisor = gcd(step_i, step_j)
                step_i, step_j = step_i / divisor, step_j / divisor

                antinode_i, antinode_j = (a.i, a.j)

                while antinode_i in range(map_size_i) and antinode_j in range(map_size_j):
                    antinodes.add((antinode_i, antinode_j))
                    antinode_i, antinode_j = antinode_i + step_i, antinode_j + step_j

            else:
                antinode_i, antinode_j = (a.i + 2 * (b.i - a.i), a.j + 2 * (b.j - a.j))

                if antinode_i in range(map_size_i) and antinode_j in range(map_size_j):
                    antinodes.add((antinode_i, antinode_j))

    return len(antinodes)


def parse_input(puzzle_input: str) -> tuple[int, int, list[Antenna]]:
    lines = puzzle_input.strip().split('\n')
    rows = [list(line) for line in lines]

    antennas = []

    for i, row in enumerate(rows):
        for j, char in enumerate(row):

            if char != '.':
                antennas.append(Antenna(i=i, j=j, frequency=char))

    return len(rows), len(rows[0]), antennas
