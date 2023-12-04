from collections import defaultdict

from loguru import logger
from pydantic import BaseModel

from advent_interaction import get_problem_input


class GameLine(BaseModel):
    number: int
    left: list[int]
    right: list[int]
    matching: int = 0
    score: int = 0

    def count_winning_numbers(self) -> int:
        set_left = set(self.left)
        set_right = set(self.right)
        return len(set_left & set_right)

    @staticmethod
    def compute_score_from_winning(winning: int) -> int:
        if winning == 0:
            return 0
        return 2 ** (winning - 1)

    def compute_card_score(self) -> int:
        winning = self.count_winning_numbers()
        self.matching = winning
        self.score = GameLine.compute_score_from_winning(winning)
        return self.score


def parse_row(row: str) -> list[int]:
    row_numbers = []
    for number in row.split(" "):
        if number.strip() == "":
            continue
        row_numbers.append(int(number.strip()))
    return row_numbers


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
        result += game_line.compute_card_score()
    return result


def solve_part_2(input_string: str) -> int:
    game_lines = []
    for line in input_string.splitlines():
        if line == "":
            continue
        game_line = parse_line(line)
        game_line.compute_card_score()
        game_lines.append(game_line)

    instance_records: dict[int, int] = defaultdict(int)
    for game_line in game_lines:
        # logger.debug(f"Processing {game_line.number} - {game_line.matching}")
        instance_records[game_line.number] += 1
        # logger.debug(f"Duplicating {instance_records[game_line.number]} times")
        for number_instances in range(instance_records[game_line.number]):
            for shift_matching in range(game_line.matching):
                # logger.debug(f"Increase instance of {game_line.number + shift_matching}")
                instance_records[game_line.number + shift_matching + 1] += 1
    return sum(instance_records.values())


def main():
    input_string = get_problem_input(4)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
