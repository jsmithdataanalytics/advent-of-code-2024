def main(puzzle_input: str) -> int:
    grid = [list(line.strip()) for line in puzzle_input.strip().split('\n')]
    grid_height, grid_width = len(grid), len(grid[0])
    direction_vectors = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direction_chars = 'v<^>'

    obstacles = set()
    guard_i, guard_j = 0, 0
    direction_index = 0

    for i, row in enumerate(grid):
        for j, char in enumerate(row):

            if char == '#':
                obstacles.add((i, j))

            elif char in direction_chars:
                guard_i, guard_j = i, j
                direction_index = direction_chars.index(char)

    visited = set()

    while guard_i in range(grid_height) and guard_j in range(grid_width):
        visited.add((guard_i, guard_j))

        for step_i, step_j in [direction_vectors[(direction_index + n) % 4] for n in range(4)]:
            guard_i += step_i
            guard_j += step_j

            if (guard_i, guard_j) not in obstacles:
                direction_index = direction_vectors.index((step_i, step_j))
                break

            guard_i -= step_i
            guard_j -= step_j

    return len(visited)
