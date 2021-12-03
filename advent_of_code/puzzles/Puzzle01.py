"""Day 1 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/01.txt")


class Puzzle01(PuzzleInterface):
    """Defines the day 1 puzzle"""

    def execute(self) -> None:
        """Executes the day 1 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        measurements = input_file.readlines()
        self.__part1(measurements)
        self.__part2(measurements)

    def __part1(self, measurements):
        """Executes the day 1 puzzle part 1"""
        previous = None
        current = None
        increase_count = 0

        for m in measurements:
            current = int(m.strip())
            if previous is not None:
                if previous < current:
                    increase_count += 1

            previous = current

        print(
            "#01 (part 1) - Number of measurements increased from previous is"
            f" {increase_count}."
        )

    def __part2(self, measurements):
        """Executes the day 1 puzzle part 2"""
        previous = None
        current = None
        increase_count = 0
        sliding_window = [0] * 3
        for m in measurements:
            sliding_window.pop(0)
            sliding_window.append(int(m.strip()))
            current = sum(sliding_window)

            if previous is not None:
                if previous < current:
                    increase_count += 1

            if 0 not in sliding_window:
                previous = current

        print(
            "#01 (part 2) - Number of sliding windows increased from previous is"
            f" {increase_count}."
        )
