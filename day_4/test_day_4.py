import pytest

from advent_interaction import get_problem_input
from day_4.solution_day_4 import (
    solve_part_1,
    parse_line,
    GameLine,
    solve_part_2,
)

SAMPLE = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""
SCORE_PER_LINE = [
    8,
    2,
    2,
    1,
    0,
    0,
]


def test_parse_line():
    line = "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"
    expected = GameLine(
        number=3,
        left=[1, 21, 53, 59, 44],
        right=[69, 82, 63, 72, 16, 21, 14, 1],
    )
    assert parse_line(line) == expected


@pytest.mark.parametrize(
    "line, expected",
    [(line, score) for line, score in zip(SAMPLE.splitlines(), SCORE_PER_LINE)],
)
def test_compute_score_from_line(line, expected):
    game_line = parse_line(line)
    assert game_line.compute_card_score() == expected


class TestPart1:
    def test_solve_sample(self):
        expected = 13
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(4)
        accepted_value = 32001
        assert solve_part_1(input_string) == accepted_value


class TestPart2:
    def test_solve_sample(self):
        expected = 30
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(4)
        accepted_value = 5037841
        assert solve_part_2(input_string) == accepted_value
