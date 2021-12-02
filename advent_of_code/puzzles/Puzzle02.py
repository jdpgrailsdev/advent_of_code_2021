"""Day 2 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/02.txt")


class Puzzle02(PuzzleInterface):
    """Defines the day 2 puzzle"""

    def execute(self) -> None:
        """Executes the day 1 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        directions = input_file.readlines()
        self.__part1(directions)
        self.__part2(directions)

    def __part1(self, directions):
        """Executes the day 2 puzzle part 1"""
        horizontal_pos = 0
        depth = 0

        for d in directions:
            direction = d.split(" ")[0]
            amount = d.split(" ")[1]
            if direction == "forward":
                horizontal_pos += int(amount)
            elif direction == "down":
                depth += int(amount)
            else:
                depth -= int(amount)

        print(
            "#02 (part 1) - Product of horizontal position and depth is "
            f"{horizontal_pos * depth}"
        )

    def __part2(self, directions):
        """Executes the day 2 puzzle part 1"""
        horizontal_pos = 0
        depth = 0
        aim = 0

        for d in directions:
            direction = d.split(" ")[0]
            amount = d.split(" ")[1]
            if direction == "forward":
                horizontal_pos += int(amount)
                depth += aim * int(amount)
            elif direction == "down":
                aim += int(amount)
            else:
                aim -= int(amount)

        print(
            "#02 (part 2) - Product of horizontal position and depth is "
            f"{horizontal_pos * depth}"
        )
