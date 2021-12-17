"""Day 17 Puzzle"""

import os
import re

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/17.txt")


class Puzzle17(PuzzleInterface):
    """Defines the day 17 puzzle"""

    def execute(self) -> None:
        """Executes the day 17 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 17 puzzle part 1"""
        target_x_area, target_y_area = self.__parse_target_area(data[0])
        _, _, max_height = self.__find_y_height(target_x_area, target_y_area)
        print(f"#17 (part 1) - The highest y position is {max_height}")

    def __part2(self, data):
        """Executes the day 17 puzzle part 2"""
        target_x_area, target_y_area = self.__parse_target_area(data[0])
        velocities = self.__find_initial_velocities(target_x_area, target_y_area)
        print(f"#17 (part 2) - The initial number of velocities is {len(velocities)}")

    def __parse_target_area(self, data):
        _, area = data.split(":")
        x_range, y_range = area.split(", ")

        return tuple(
            list(map(int, re.search("x=(.*)", x_range).group(1).split("..")))
        ), tuple(list(map(int, re.search("y=(.*)", y_range).group(1).split(".."))))

    def __find_x_velocity(self, target_x_area):
        velocity = 0
        x_change = 0

        while not target_x_area[0] <= x_change <= target_x_area[1]:
            velocity += 1
            x_change += velocity

        return velocity

    def __find_y_height(self, target_x_area, target_y_area):
        x_velocity = self.__find_x_velocity(target_x_area)
        y_velocity = abs(target_y_area[0]) - 1
        y_height = y_velocity * (abs(target_y_area[0])) // 2
        return x_velocity, y_velocity, y_height

    def __find_initial_velocities(self, target_x_area, target_y_area):
        velocities = set()

        min_x_velocity = self.__find_x_velocity(target_x_area)
        max_x_velocity = target_x_area[1]
        min_y_velocity = target_y_area[0]
        max_y_velocity = abs(target_y_area[0]) - 1

        for x in range(min_x_velocity, max_x_velocity + 1):
            for y in range(min_y_velocity, max_y_velocity + 1):
                x_velocity = x
                y_velocity = y
                current_x = 0
                current_y = 0
                while current_x <= target_x_area[1] and current_y >= target_y_area[0]:
                    if current_x >= target_x_area[0] and current_y <= target_y_area[1]:
                        velocities.add((x, y))
                        break

                    current_x += x_velocity
                    current_y += y_velocity

                    x_velocity -= min(1, x_velocity)
                    y_velocity -= 1

        return velocities
