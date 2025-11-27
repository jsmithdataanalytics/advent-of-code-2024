direction_vectors = [(1, 0), (0, -1), (-1, 0), (0, 1)]
direction_chars = 'v<^>'


def main(puzzle_input: str) -> int:
    grid = [list(line.strip()) for line in puzzle_input.strip().split('\n')]
    grid_height, grid_width = len(grid), len(grid[0])

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

    count = 0

    for i, row in enumerate(grid):
        for j, char in enumerate(row):

            if (i, j) != (guard_i, guard_j) and (i, j) not in obstacles:
                new_obstacles = obstacles.copy()
                new_obstacles.add((i, j))

                if does_guard_loop(grid_height, grid_width, new_obstacles, guard_i, guard_j, direction_index):
                    count += 1

    return count


def does_guard_loop(
    grid_height: int,
    grid_width: int,
    obstacles: set[tuple[int, int]],
    guard_i: int,
    guard_j: int,
    direction_index: int,
) -> bool:
    states = set()

    while guard_i in range(grid_height) and guard_j in range(grid_width):
        current_state = (guard_i, guard_j, direction_index)

        if current_state in states:
            return True

        states.add(current_state)

        for step_i, step_j in [direction_vectors[(direction_index + n) % 4] for n in range(4)]:
            guard_i += step_i
            guard_j += step_j

            if (guard_i, guard_j) not in obstacles:
                direction_index = direction_vectors.index((step_i, step_j))
                break

            guard_i -= step_i
            guard_j -= step_j

    return False
