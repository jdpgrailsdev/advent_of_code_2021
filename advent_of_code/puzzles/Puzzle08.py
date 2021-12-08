"""Day 8 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/08.txt")


class Puzzle08(PuzzleInterface):
    """Defines the day 8 puzzle"""

    def execute(self) -> None:
        """Executes the day 8 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 8 puzzle part 1"""

        output_value_count = 0

        for d in data:
            signal_pattern, output_value = d.split(" | ")
            output_value_count += self.__find_unique_count(output_value)

        print(
            f"#08 (part 1) - The digits 1,4,7 and 8 appear {output_value_count} times."
        )

    def __part2(self, data):
        """Executes the day 8 puzzle part 2"""

        digit_map = {
            42: "0",
            17: "1",
            34: "2",
            39: "3",
            30: "4",
            37: "5",
            41: "6",
            25: "7",
            49: "8",
            45: "9",
        }

        output_sum = 0

        for d in data:
            signal_pattern, output_value = d.split(" | ")
            codec = self.__build_codec(signal_pattern)

            digits = ""
            for value in output_value.split(" "):
                value_score = 0
                for c in value:
                    value_score += codec[c]
                digits += digit_map[value_score]

            output_sum += int(digits)

        print(f"#08 (part 2) - The sum of the output values is {output_sum}.")

    def __build_codec(self, patterns):
        codec = {}

        for pattern in patterns:
            for p in pattern.split(" "):
                for c in p:
                    if c in codec:
                        codec[c] += 1
                    else:
                        codec[c] = 1

        return codec

    def __find_unique_count(self, value):
        total = 0

        for v in value.split(" "):
            unique_count = len(set(v))
            if (
                unique_count == 2
                or unique_count == 3
                or unique_count == 4
                or unique_count == 7
            ):
                total += 1

        return total
