"""Day 9 Puzzle"""

import os
import sys
from functools import reduce

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/09.txt")


class Puzzle09(PuzzleInterface):
    """Defines the day 9 puzzle"""

    def execute(self) -> None:
        """Executes the day 9 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        # self.__part2(data)

    def __part1(self, data):
        """Executes the day 9 puzzle part 1"""

        risk_level = 0

        for i, d in enumerate(data):
            prev_up = sys.maxsize * 2 + 1
            prev_value = sys.maxsize * 2 + 1
            next_value = sys.maxsize * 2 + 1
            next_down = sys.maxsize * 2 + 1

            for pos, h in enumerate(d):
                height = int(h)
                next_value = (
                    int(d[pos + 1]) if pos < len(d) - 1 else sys.maxsize * 2 + 1
                )
                next_down = (
                    int(data[i + 1][pos]) if i < len(data) - 1 else sys.maxsize * 2 + 1
                )
                prev_up = int(data[i - 1][pos]) if i > 0 else sys.maxsize * 2 + 1

                if (
                    height < prev_value
                    and height < next_value
                    and height < prev_up
                    and height < next_down
                ):
                    risk_level += height + 1

                prev_value = height

        print(
            "#09 (part 1) - The sum of the risk levels for all low points is"
            f" {risk_level}"
        )

    def __part2(self, data):
        """Executes the day 9 puzzle part 2"""

        basin_sizes = []

        for i, d in enumerate(data):
            prev_up = sys.maxsize * 2 + 1
            prev_value = sys.maxsize * 2 + 1
            next_value = sys.maxsize * 2 + 1
            next_down = sys.maxsize * 2 + 1

            for pos, h in enumerate(d):
                height = int(h)
                next_value = (
                    int(d[pos + 1]) if pos < len(d) - 1 else sys.maxsize * 2 + 1
                )
                next_down = (
                    int(data[i + 1][pos]) if i < len(data) - 1 else sys.maxsize * 2 + 1
                )
                prev_up = int(data[i - 1][pos]) if i > 0 else sys.maxsize * 2 + 1

                if (
                    height < prev_value
                    and height < next_value
                    and height < prev_up
                    and height < next_down
                ):
                    print(f"Found low point {height} at position {i}, {pos}...")
                    basin_sizes.append(self.__find_basin_size(i, pos, data, height))

            basin_sizes.sort(reverse=True)

            print(
                "#09 (part 2) - The sum of the three largest basin sizes is"
                f" {reduce((lambda a,b: a*b),basin_sizes[:3])}"
            )

    def __find_basin_size(self, row, col, data, low_point):
        size = 0

        print(f"Checking ({row},{col})...")
        if self.__is_valid_index(row, data) is not True:
            return 0
        elif self.__is_valid_index(col, data[row]) is not True:
            return 0

        current_value = int(data[row][col])
        print(f"Current value at ({row},{col}) is {current_value}.")
        if current_value == 9:
            return 0

        if current_value >= low_point:
            size = 1
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if r != row or c != col:
                        size += self.__find_basin_size(r, c, data, low_point)

        return size

    def __is_valid_index(self, index, data):
        return 0 < index < len(data)
