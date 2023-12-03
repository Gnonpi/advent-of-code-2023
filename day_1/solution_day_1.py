import re

from advent_interaction import get_problem_input

NUMBER_WORDS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
RE_NUMBER_WORDS = {
    word: re.compile(word)
    for word in NUMBER_WORDS
}


def solve_part_1(input_string: str) -> int:
    result = 0
    for line in input_string.splitlines():
        first_number = None
        second_number = None
        for char in line:
            if char.isdigit():
                char_num = int(char)
                if first_number is None:
                    first_number = char_num
                second_number = char_num
        result += first_number * 10 + second_number
    return result


def recognize_words(line: str) -> dict[int, int]:
    words_pos = {}
    for word, re_compiled in RE_NUMBER_WORDS.items():
        for match in re_compiled.finditer(line):
            words_pos[match.start()] = NUMBER_WORDS.index(word) + 1
    return words_pos


def recognize_digits(line: str) -> dict[int, int]:
    digits_pos = {}
    for i, char in enumerate(line):
        if char.isdigit():
            digits_pos[i] = int(char)
    return digits_pos


def compute_line_digits_and_words(line: str) -> int:
    detected_words = recognize_words(line)
    detected_digits = recognize_digits(line)
    fused_detected = detected_words | detected_digits
    first_pos = min(fused_detected.keys())
    last_pos = max(fused_detected.keys())
    first_number = fused_detected[first_pos]
    last_number = fused_detected[last_pos]
    return first_number * 10 + last_number


def solve_part_2(input_string: str) -> int:
    result = 0
    for line in input_string.splitlines():
        result += compute_line_digits_and_words(line)
    return result


def main():
    input_string = get_problem_input(1)
    solution_part_1 = solve_part_1(input_string)
    print(f"Solution part 1: {solution_part_1}")
    solution_part_2 = solve_part_2(input_string)
    print(f"Solution part 2: {solution_part_2}")


if __name__ == "__main__":
    main()
