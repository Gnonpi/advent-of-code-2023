from advent_interaction import get_problem_input
from day_3.solution_day_3 import (
    solve_part_1,
    solve_part_2,
    parse_grid,
    number_positions_in_line,
    adjacents_to_number,
    find_numbers_around_gear_line,
    NumberPosition,
    coords_around_gear_position,
    filter_numbers_adjacent_to,
)

sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

mini_sample = """467
..*
.*3
"""


def test_parse_grid():
    expected = [
        "467",
        "..*",
        ".*3",
    ]
    assert parse_grid(mini_sample) == expected


def test_number_positions_in_line():
    line = "..35..633."
    positions = number_positions_in_line(line)
    assert positions == [
        (35, 2, 4),
        (633, 6, 9),
    ]


def test_adjacents_to_number():
    adjacents = adjacents_to_number(parse_grid(sample), 0, 0, 3)
    assert adjacents == {".", "*"}

    adjacents = adjacents_to_number(parse_grid(sample), 4, 0, 3)
    assert adjacents == {".", "*"}


class TestPart1:
    def test_solve_sample(self):
        expected = 4361
        assert solve_part_1(sample) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(3)
        accepted_value = 522726
        assert solve_part_1(input_string) == accepted_value


def test_find_numbers_around_gear_line():
    number_positions = find_numbers_around_gear_line(parse_grid(sample), 1)
    expected = [
        NumberPosition(value=467, line_no=0, start=0, end=3),
        NumberPosition(value=114, line_no=0, start=5, end=8),
        NumberPosition(value=35, line_no=2, start=2, end=4),
        NumberPosition(value=633, line_no=2, start=6, end=9),
    ]
    assert number_positions == expected


def test_coords_around_gear_position():
    coords = coords_around_gear_position(parse_grid(sample), 4, 1)
    assert len(coords) == 8
    expected = {
        (3, 0),
        (4, 0),
        (5, 0),
        (3, 1),
        (5, 1),
        (3, 2),
        (4, 2),
        (5, 2),
    }
    assert coords == expected


def test_filter_numbers_adjacent_to():
    number_positions = find_numbers_around_gear_line(parse_grid(sample), 1)
    filtered_numbers = filter_numbers_adjacent_to(
        parse_grid(sample), 3, 1, number_positions
    )
    expected = [number for number in number_positions if number.value in {467, 35}]
    assert filtered_numbers == expected


class TestPart2:
    def test_solve_sample(self):
        expected = 467835
        assert solve_part_2(sample) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(3)
        accepted_value = 81721933
        assert solve_part_2(input_string) == accepted_value
