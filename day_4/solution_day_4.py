from loguru import logger
from pydantic import BaseModel

from advent_interaction import get_problem_input


class GameLine(BaseModel):
    number: int
    left: list[int]
    right: list[int]


def parse_row(row: str) -> list[int]:
    row_numbers = []
    for number in row.split(" "):
        if number.strip() == "":
            continue
        row_numbers.append(int(number.strip()))
    return row_numbers


def count_winning_numbers(game_line: GameLine) -> int:
    set_left = set(game_line.left)
    set_right = set(game_line.right)
    return len(set_left & set_right)


def compute_score_from_winning(winning: int) -> int:
    if winning == 0:
        return 0
    return 2 ** (winning - 1)


def parse_line(line: str) -> GameLine:
    game_indication, numbers = line.split(":")
    game_number = game_indication.replace("Card ", "").strip()
    left_row, right_row = numbers.split("|")
    return GameLine(
        number=game_number,
        left=parse_row(left_row),
        right=parse_row(right_row),
    )


def solve_part_1(input_string: str) -> int:
    result = 0
    for line in input_string.splitlines():
        if line == "":
            continue
        game_line = parse_line(line)
        winning = count_winning_numbers(game_line)
        result += compute_score_from_winning(winning)
    return result


def solve_part_2(input_string: str) -> int:
    raise NotImplementedError


def main():
    input_string = get_problem_input(4)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
