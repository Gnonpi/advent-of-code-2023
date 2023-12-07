import sys
import re
import copy
from pydantic import BaseModel
from loguru import logger
from advent_interaction import get_problem_input


RE_MAP_NAME = re.compile(r"(?P<source>\w+)-to-(?P<dest>\w+) map:")


class RangeMapping(BaseModel):
    source_range_start: int
    destination_range_start: int
    range_length: int

    def process_number(self, incoming_num: int) -> int:
        if (
            incoming_num < self.source_range_start
            or incoming_num > self.source_range_start + self.range_length
        ):
            return incoming_num
        shift_incoming_num = self.destination_range_start - self.source_range_start
        return incoming_num + shift_incoming_num


class GardenMapping(BaseModel):
    source_name: str
    destination_name: str
    ranges: list[RangeMapping]

    def _go_through_ranges(self, incoming_num: int) -> int:
        for range_map in self.ranges:
            new_num = range_map.process_number(incoming_num)
            # ranges shouldn't overlap
            # and cover the space
            if new_num != incoming_num:
                return new_num
        return incoming_num

    def process_incoming(self, incoming: list[int]) -> tuple[str, list[int]]:
        logger.debug(f"Processing {self}")
        output = []
        for num in incoming:
            output.append(self._go_through_ranges(num))
        return self.destination_name, output


def parse_input(input_string: str) -> tuple[list[int], dict[str, GardenMapping]]:
    block_split = input_string.split("\n\n")
    # seeds
    seed_block = block_split.pop(0).replace("seeds: ", "")
    seed_numbers = [int(num) for num in seed_block.split(" ")]
    # rest
    parsed = dict()
    for block in block_split:
        map_descr, *ranges = block.splitlines()
        matched = RE_MAP_NAME.search(map_descr)
        assert matched is not None
        source_name = matched.groupdict()["source"]
        dest_name = matched.groupdict()["dest"]
        current_ranges = []
        for line in ranges:
            dest_start, source_start, range_length = line.split(" ")
            current_ranges.append(
                RangeMapping(
                    source_range_start=source_start,
                    destination_range_start=dest_start,
                    range_length=range_length,
                )
            )
        parsed[source_name] = GardenMapping(
            source_name=source_name,
            destination_name=dest_name,
            ranges=current_ranges,
        )
    return seed_numbers, parsed


def solve_part_1(input_string: str) -> int:
    seeds, map_garden = parse_input(input_string)
    current_ranges = copy.deepcopy(seeds)
    current_map_name = "seed"
    while current_map_name != "humidity":
        current_map = map_garden[current_map_name]
        dest_map = map_garden[current_map.destination_name]
        next_destination, current_ranges = current_map.process_incoming(current_ranges)
        current_map_name = next_destination
    _, current_ranges = dest_map.process_incoming(current_ranges)
    return min(current_ranges)


def solve_part_2(input_string: str) -> int:
    raise NotImplementedError


def main():
    logger.remove()
    logger.add(sys.stderr, level="INFO")
    input_string = get_problem_input(5)
    solution_part_1 = solve_part_1(input_string)
    logger.info(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    logger.info(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
