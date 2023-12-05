from pathlib import Path
from advent_interaction import get_problem_input
from day_5.solution_day_5 import solve_part_1, parse_input


def load_sample() -> str:
    sample_path = Path(__file__).parent / "sample-day-5"
    return open(sample_path).read()

def test_parse_sample():
    seeds, map_mapping = parse_input(load_sample())
    expected_seeds = [79, 14, 55, 13]
    assert seeds == expected_seeds
    assert isinstance(map_mapping, dict)
    expected_keys = {
        "seed", 
        "soil", 
        "fertilizer", 
        "water", 
        "light", 
        "temperature", 
        "humidity", 
        # "location",
    }
    assert set(map_mapping.keys()) == expected_keys
    assert map_mapping["seed"].source_name == "seed"
    assert map_mapping["seed"].destination_name == "soil"
    assert len(map_mapping["seed"].ranges) == 2


def test_process_soil_example():
    seeds, map_mapping = parse_input(load_sample())
    dest, soils = map_mapping["seed"].process_incoming(seeds)
    expected_dest = "soil"
    expected_soils = [81, 14, 57, 13]
    assert dest == expected_dest
    assert soils == expected_soils


def test_process_fertilizer_example():
    seeds, map_mapping = parse_input(load_sample())
    soils = [81, 14, 57, 13]
    dest, fertilizers = map_mapping["soil"].process_incoming(soils)
    expected_dest = "fertilizer"
    expected_fertilizers = [81, 53, 57, 52]
    assert dest == expected_dest
    assert fertilizers == expected_fertilizers


def test_chain_processed():
    seeds, map_mapping = parse_input(load_sample())
    dest, current_nums = map_mapping["seed"].process_incoming(seeds)
    expected = [81, 14, 57, 13]
    assert dest == "soil"
    dest, current_nums = map_mapping[dest].process_incoming(current_nums)
    expected = [81, 53, 57, 52]
    assert dest == "fertilizer"
    dest, current_nums = map_mapping[dest].process_incoming(current_nums)
    expected = [81, 49, 53, 41]
    assert dest == "water"
    dest, current_nums = map_mapping[dest].process_incoming(current_nums)
    expected = [74, 42, 46, 34]
    assert dest == "light"
    dest, current_nums = map_mapping[dest].process_incoming(current_nums)
    expected = [78, 42, 82, 34]
    assert dest == "temperature"
    dest, current_nums = map_mapping[dest].process_incoming(current_nums)
    expected = [78, 43, 82, 35]
    assert dest == "humidity"


class TestPart1:
    def test_solve_sample(self):
        sample = load_sample()
        expected = 35
        assert solve_part_1(sample) == expected

    def test_solve_real_problem(self):
        input_string = get_problem_input(5)
        expected = None
        assert solve_part_1(input_string) == expected

        assert False
