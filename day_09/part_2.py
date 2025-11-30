from day_09.part_1 import parse_input


def main(puzzle_input: str) -> int:
    disk = parse_input(puzzle_input)
    files, free_areas = create_index(disk)

    for file_id, file in sorted(files.items(), key=lambda item: item[0], reverse=True):

        for i, free_area in enumerate(free_areas):

            if free_area and free_area[0] < file[0] and len(free_area) >= len(file):
                file = range(free_area[0], free_area[0] + len(file))
                files[file_id] = file

                free_area = range(file[-1] + 1, free_area[-1] + 1)
                free_areas[i] = free_area

                break

    return sum(file_id * i for file_id, file in files.items() for i in file)


def create_index(disk: list[str | int]) -> tuple[dict[int, range], list[range]]:
    files = {}
    free_areas = []

    for i, file_id in enumerate(disk):

        if file_id is None:

            if free_areas and free_areas[-1][-1] == i - 1:
                free_areas[-1] = range(free_areas[-1][0], i + 1)

            else:
                free_areas.append(range(i, i + 1))

        else:
            files[file_id] = range(files[file_id][0], i + 1) if file_id in files else range(i, i + 1)

    return files, free_areas
