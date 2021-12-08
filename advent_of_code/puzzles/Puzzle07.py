"""Day 7 Puzzle"""

import os
import sys

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/07.txt")


class Puzzle07(PuzzleInterface):
    """Defines the day 7 puzzle"""

    def execute(self) -> None:
        """Executes the day 7 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        # self.__part2(data)

    def __part1(self, data):
        """Executes the day 7 puzzle part 1"""

        positions = list(map(int, data[0].split(",")))
        min_position = min(positions)
        max_position = max(positions)

        min_fuel = sys.maxsize * 2 + 1

        for p in range(min_position, max_position + 1):
            fuel = 0
            for pos in positions:
                fuel += abs(pos - p)

            if fuel < min_fuel:
                min_fuel = fuel

        print(f"#07 (part 1) - The cheapest amount of fuel is {min_fuel}")

    def __part2(self, data):
        """Executes the day 7 puzzle part 2"""

        positions = list(map(int, data[0].split(",")))
        min_position = min(positions)
        max_position = max(positions)

        min_fuel = sys.maxsize * 2 + 1

        for p in range(min_position, max_position + 1):
            fuel = 0
            for pos in positions:
                fuel += sum(range(abs(pos - p) + 1))

            if fuel < min_fuel:
                min_fuel = fuel

        print(f"#07 (part 2) - The cheapest amount of fuel is {min_fuel}")
