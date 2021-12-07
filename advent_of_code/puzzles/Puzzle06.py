"""Day 6 Puzzle"""

import math
import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/06.txt")


class Puzzle06(PuzzleInterface):
    """Defines the day 6 puzzle"""

    def execute(self) -> None:
        """Executes the day 6 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 6 puzzle part 1"""

        ages = list(map(int, data[0].split(',')))
        days = 80

        new_ages = self.__compute_ages(ages, days)
        print(f"#06 (part 1) - The number of lanternfish after {days} days is {len(new_ages)}")

    def __part2(self, data):
        """Executes the day 6 puzzle part 2"""

        ages = list(map(int, data[0].split(',')))
        original_days = 80
        new_ages = self.__compute_ages(ages, original_days)
        growth_rate = (len(new_ages) - len(ages))/len(ages)
        print(growth_rate)
        growth = len(ages) * int(math.pow(growth_rate, days//original_days))
        print(f"#06 (part 2) - The number of lanternfish after {days} days is {growth}")


    def __compute_ages(self, ages, days):
        new_ages = []
        new_fish = []

        for age in ages:
            if age == 0:
                new_ages.append(6)
                new_fish.append(8)
            else:
                age -= 1
                new_ages.append(age)

        new_ages.extend(new_fish)

        if days > 1:
            return self.__compute_ages(new_ages, days - 1)
        else:
            return new_ages
