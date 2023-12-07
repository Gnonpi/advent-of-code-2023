import pytest

from advent_interaction import get_problem_input
from day_6.solution_day_6 import (
    solve_part_1,
    solve_part_2,
    parse_problem,
    compute_ways_to_win_race,
    parse_part_two,
)

SAMPLE = """Time:      7  15   30
Distance:  9  40  200"""


def test_parse_sample():
    records = parse_problem(SAMPLE)
    assert records == [(7, 9), (15, 40), (30, 200)]


@pytest.mark.parametrize(
    "limit_time, distance, expected",
    [
        (7, 9, 4),
        (15, 40, 8),
        (30, 200, 9),
    ],
)
def test_compute_ways_to_win_race(limit_time, distance, expected):
    assert compute_ways_to_win_race(limit_time, distance) == expected


class TestPart1:
    def test_solve_sample(self):
        expected = 288
        assert solve_part_1(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(6)
        accepted_value = 800280
        assert solve_part_1(input_string) == accepted_value


def test_parse_part_two():
    assert parse_part_two(SAMPLE) == (71530, 940200)


class TestPart2:
    def test_solve_sample(self):
        expected = 71503
        assert solve_part_2(SAMPLE) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(6)
        accepted_value = 45128024
        assert solve_part_2(input_string) == accepted_value
