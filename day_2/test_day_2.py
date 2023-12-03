import pytest

from advent_interaction import get_problem_input
from day_2.solution_day_2 import (
    solve_part_1,
    parse_line,
    Pull,
    Game,
    is_game_possible,
    solve_part_2,
    fewest_limits_in_game,
)


def test_parse_line():
    line = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"
    expected = Game(
        number=3,
        pulls=[
            Pull(red=20, green=8, blue=6),
            Pull(red=4, green=13, blue=5),
            Pull(red=1, green=5, blue=0),
        ],
    )
    assert parse_line(line) == expected


@pytest.mark.parametrize(
    "line, expected",
    [
        ("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            False,
        ),
    ],
)
def test_possible_game(line, expected):
    game = parse_line(line)
    limits = Pull(red=12, green=13, blue=14)
    assert is_game_possible(game, limits) is expected


class TestPart1:
    def test_sample(self):
        sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        result = solve_part_1(sample)
        assert result == 8

    def test_solve_real_problem(self):
        input_string = get_problem_input(2)
        accepted_value = 2720
        assert solve_part_1(input_string) == accepted_value


@pytest.mark.parametrize(
    "line, expected",
    [
        (
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            Pull(red=4, green=2, blue=6),
        ),
        (
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            Pull(red=20, green=13, blue=6),
        ),
    ],
)
def test_fewest_limits_in_game(line, expected):
    game = parse_line(line)
    assert fewest_limits_in_game(game) == expected


class TestPart2:
    def test_sample(self):
        sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
        result = solve_part_2(sample)
        assert result == 2286

    def test_solve_real_problem(self):
        input_string = get_problem_input(2)
        accepted_value = 71535
        assert solve_part_2(input_string) == accepted_value
