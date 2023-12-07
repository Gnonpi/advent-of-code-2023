import math

from loguru import logger

from advent_interaction import get_problem_input, Tools


def parse_problem(input_string: str) -> list[tuple[int, int]]:
    lines = input_string.splitlines()
    _, times = Tools.read_line_header_and_numbers(lines[0])
    _, distances = Tools.read_line_header_and_numbers(lines[1])
    return list(zip(times, distances))


def compute_ways_to_win_race(limit_time: int, distance: int) -> int:
    """
    (h * (l - h)) >= d
    2nd degree polynom: (-1) * h**2 + l * h - d >= 0
    delta = l**2 - 4*d
    root = (-l -+ sqrt(delta)) / 2*(-1)
    """
    delta = limit_time**2 - 4 * distance
    if delta < 0:
        return 0
    elif delta == 1:
        return 1
    else:
        # since h >= 0, and our h2 is negative
        # curve is always opened downward
        first_root = (-1 * limit_time + math.sqrt(delta)) / -2
        second_root = (-1 * limit_time - math.sqrt(delta)) / -2
        if math.modf(first_root)[0] == 0:
            first_root_int = int(first_root + 1)
        else:
            first_root_int = math.ceil(first_root)
        if math.modf(second_root)[0] == 0:
            second_root_int = int(second_root - 1)
        else:
            second_root_int = math.floor(second_root)
        logger.debug(f"{first_root=} ; {first_root_int=}")
        logger.debug(f"{second_root=} ; {second_root_int=}")
        return second_root_int - first_root_int + 1


def solve_part_1(input_string: str) -> int:
    records = parse_problem(input_string)
    result = 1
    for record in records:
        ways = compute_ways_to_win_race(record[0], record[1])
        result *= ways
    return result


def parse_part_two(input_string: str) -> tuple[int, int]:
    lines = input_string.splitlines()
    total_time = int(lines[0].replace("Time: ", "").strip().replace(" ", ""))
    total_distance = int(lines[1].replace("Distance:", "").strip().replace(" ", ""))
    return total_time, total_distance


def solve_part_2(input_string: str) -> int:
    limit_time, distance = parse_part_two(input_string)
    return compute_ways_to_win_race(limit_time, distance)


def main():
    input_string = get_problem_input(6)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
