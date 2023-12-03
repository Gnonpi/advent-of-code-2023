import pytest

from advent_interaction import get_problem_input
from day_1.solution_day_1 import solve_part_1, solve_part_2, recognize_digits, recognize_words, \
    compute_line_digits_and_words


class TestPartOne:
    def test_solve_sample(self):
        sample = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
        assert solve_part_1(sample) == 142

    def test_solve_real_problem(self):
        input_string = get_problem_input(1)
        accepted_value = 55607
        assert solve_part_1(input_string) == accepted_value


class TestPartTwo:
    @pytest.mark.parametrize("line, expected", [
        ("two1nine", {0: 2, 4: 9}),
        ("4nineeightseven2", {1: 9, 5: 8, 10: 7}),
        ("7pqrstsixteen", {6: 6}),
        ("twone", {0: 2, 2: 1}),
    ])
    def test_recognize_words(self, line, expected):
        assert recognize_words(line) == expected

    @pytest.mark.parametrize("line, expected", [
        ("two1nine", {3: 1}),
        ("4nineeightseven2", {0: 4, 15: 2}),
    ])
    def test_recognize_digits(self, line, expected):
        assert recognize_digits(line) == expected

    @pytest.mark.parametrize("line, expected", [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
        # from input
        ("896", 86),
        ("4twoseven7tjmklbl", 47),
        ("twone", 21),
    ])
    def test_compute_line(self, line, expected):
        assert compute_line_digits_and_words(line) == expected

    def test_solve_sample(self):
        sample = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
        assert solve_part_2(sample) == 281

    def test_solve_real_problem(self):
        input_string = get_problem_input(1)
        accepted_value = 55291
        assert solve_part_2(input_string) == accepted_value
