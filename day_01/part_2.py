def main(puzzle_input: str) -> int:
    nums = list(map(int, puzzle_input.strip().split()))

    list_1 = sorted(num for i, num in enumerate(nums) if i % 2 == 0)
    list_2 = sorted(num for i, num in enumerate(nums) if i % 2 != 0)

    return sum(num * list_2.count(num) for num in list_1)
