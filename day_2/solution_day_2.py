from typing import Self

from loguru import logger
from pydantic import BaseModel
from advent_interaction import get_problem_input


class Pull(BaseModel):
    red: int = 0
    green: int = 0
    blue: int = 0

    def is_contained_within(self, other: Self) -> bool:
        return (
            self.red <= other.red
            and self.green <= other.green
            and self.blue <= other.blue
        )

    def merge_fewest(self, other: Self) -> Self:
        return Pull(
            red=max(self.red, other.red),
            green=max(self.green, other.green),
            blue=max(self.blue, other.blue),
        )

    def cube_power(self) -> int:
        return self.red * self.green * self.blue


class Game(BaseModel):
    number: int
    pulls: list[Pull]


def parse_line(line: str) -> Game:
    game_indication, seq_pulls = line.split(":")
    game_number = int(game_indication.replace("Game ", "").strip())
    pulls = []
    for seq_cubes in seq_pulls.split(";"):
        pull = Pull()
        for pulled_cubes in seq_cubes.split(","):
            if "red" in pulled_cubes:
                pull.red = int(pulled_cubes.replace(" red", ""))
            elif "green" in pulled_cubes:
                pull.green = int(pulled_cubes.replace(" green", ""))
            elif "blue" in pulled_cubes:
                pull.blue = int(pulled_cubes.replace(" blue", ""))
            else:
                raise ValueError(f"Unknown color: {pulled_cubes}")
        pulls.append(pull)
    return Game(
        number=game_number,
        pulls=pulls,
    )


def is_game_possible(game: Game, limits: Pull) -> bool:
    for pull in game.pulls:
        if not pull.is_contained_within(limits):
            return False
    return True


def solve_part_1(input_string: str) -> int:
    result = 0
    limits = Pull(red=12, green=13, blue=14)
    for line in input_string.splitlines():
        parsed = parse_line(line)
        if is_game_possible(parsed, limits):
            result += parsed.number
    return result


def fewest_limits_in_game(game: Game) -> Pull:
    current_fewest = Pull()
    for pull in game.pulls:
        if not pull.is_contained_within(current_fewest):
            current_fewest = pull.merge_fewest(current_fewest)
    return current_fewest


def solve_part_2(input_string: str) -> int:
    result = 0
    for line in input_string.splitlines():
        parsed = parse_line(line)
        fewest_cubes = fewest_limits_in_game(parsed)
        result += fewest_cubes.cube_power()
    return result


def main():
    input_string = get_problem_input(2)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
