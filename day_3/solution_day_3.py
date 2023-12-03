import re

from loguru import logger
from pydantic import BaseModel

from advent_interaction import get_problem_input

RE_NUMBER_IN_LINE = re.compile(r"\d+")
RE_GEAR_IN_LINE = re.compile(r"\*")


class NumberPosition(BaseModel):
    value: int
    line_no: int
    start: int
    end: int

    def match_set_of_coords(self, coords: set[tuple[int, int]]) -> bool:
        for x, y in coords:
            if self.match_coords(x, y):
                return True
        return False

    def match_coords(self, x: int, y: int) -> bool:
        return self.line_no == y and (self.start <= x < self.end)


def parse_grid(input_string: str) -> list[str]:
    return input_string.splitlines()


def list_contain_symbol(adjacents: set[str]) -> bool:
    for char in adjacents:
        if char != "." and not char.isdigit():
            return True
    return False


def number_positions_in_line(line: str) -> list[tuple[int, int, int]]:
    result = []
    for match in RE_NUMBER_IN_LINE.finditer(line):
        result.append((int(match.group(0)), match.start(), match.end()))
    return result


def adjacents_to_number(
    grid: list[str], line_no: int, number_pos_start: int, number_pos_end: int
) -> set[str]:
    start_lookup = max(number_pos_start - 1, 0)
    end_lookup = min(number_pos_end + 1, len(grid[0]))
    adjacents = set()
    if line_no - 1 >= 0:
        line_above = grid[line_no - 1][start_lookup:end_lookup]
        adjacents.update({char for char in line_above})
    if line_no + 1 < len(grid):
        line_below = grid[line_no + 1][start_lookup:end_lookup]
        adjacents.update({char for char in line_below})

    if number_pos_start > 0:
        adjacents.add(grid[line_no][start_lookup])
    if number_pos_end < len(grid[0]):
        adjacents.add(grid[line_no][end_lookup - 1])
    return adjacents


def solve_part_1(input_string: str) -> int:
    grid = parse_grid(input_string)
    result = 0
    for line_no, line in enumerate(grid):
        number_positions = number_positions_in_line(line)
        for value, number_pos_start, number_pos_end in number_positions:
            adjacents = adjacents_to_number(
                grid, line_no, number_pos_start, number_pos_end
            )
            if list_contain_symbol(adjacents):
                result += value
    return result


def gear_positions_in_line(line: str) -> list[int]:
    result = []
    for match in RE_GEAR_IN_LINE.finditer(line):
        result.append(match.start())
    return result


def find_numbers_around_gear_line(
    grid: list[str], line_no: int
) -> list[NumberPosition]:
    line = grid[line_no]
    examined_lines = [(line_no, line)]
    if line_no - 1 >= 0:
        examined_lines.append((line_no - 1, grid[line_no - 1]))
    if line_no + 1 < len(grid):
        examined_lines.append((line_no + 1, grid[line_no + 1]))

    number_positions = []
    for examined_line_no, examined_line in examined_lines:
        for value, number_pos_start, number_pos_end in number_positions_in_line(
            examined_line
        ):
            number_positions.append(
                NumberPosition(
                    value=value,
                    line_no=examined_line_no,
                    start=number_pos_start,
                    end=number_pos_end,
                )
            )
    return number_positions


def coords_around_gear_position(
    grid: list[str], gear_x: int, gear_y: int
) -> set[tuple[int, int]]:
    min_x = max(0, gear_x - 1)
    max_x = min(len(grid[0]), gear_x + 1)
    min_y = max(0, gear_y - 1)
    max_y = min(len(grid), gear_y + 1)
    adjacent_pos = set()
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if (x, y) != (gear_x, gear_y):
                adjacent_pos.add((x, y))
    return adjacent_pos


def filter_numbers_adjacent_to(
    grid: list[str], gear_x: int, gear_y: int, number_positions: list[NumberPosition]
) -> list[NumberPosition]:
    assert grid[gear_y][gear_x] == "*"
    adjacent_coords = coords_around_gear_position(grid, gear_x, gear_y)
    filtered = []
    for number_pos in number_positions:
        if number_pos.match_set_of_coords(adjacent_coords):
            filtered.append(number_pos)
    return filtered


def solve_part_2(input_string: str) -> int:
    grid = parse_grid(input_string)
    result = 0
    for line_no, line in enumerate(grid):
        for gear_pos in gear_positions_in_line(line):
            number_in_lines = find_numbers_around_gear_line(grid, line_no)
            adjacent_numbers = filter_numbers_adjacent_to(
                grid, gear_pos, line_no, number_in_lines
            )
            if len(adjacent_numbers) == 2:
                result += adjacent_numbers[0].value * adjacent_numbers[1].value
    return result


def main():
    input_string = get_problem_input(3)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
