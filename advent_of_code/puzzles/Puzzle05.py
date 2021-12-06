"""Day 5 Puzzle"""

import math
import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/05.txt")


class Puzzle05(PuzzleInterface):
    """Defines the day 5 puzzle"""

    def execute(self) -> None:
        """Executes the day 5 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 5 puzzle part 1"""

        coordinates = self.__build_coordinates(data)
        diagram = self.__build_diagram(coordinates)
        hostile_point_count = self.__count_hostile_points(diagram)

        print(f"#05 (part 1) - The number of hostile points is {hostile_point_count}")

    def __part2(self, data):
        """Executes the day 5 puzzle part 2"""

        coordinates = self.__build_coordinates(data, True)
        diagram = self.__build_diagram(coordinates)
        hostile_point_count = self.__count_hostile_points(diagram)

        print(f"#05 (part 2) - The number of hostile points is {hostile_point_count}")

    def __build_coordinates(self, data, include_diagonal=False):
        coordinates = []

        for d in data:
            entry = d.split(" -> ")
            starting = tuple(map(int, entry[0].split(",")))
            ending = tuple(map(int, entry[1].split(",")))

            x_diff = abs(starting[0] - ending[0])
            y_diff = abs(starting[1] - ending[1])

            if x_diff == 0 or y_diff == 0:
                if x_diff > 0:
                    starting_x = min(starting[0], ending[0])
                    for x in range(0, x_diff + 1):
                        coordinates.append(tuple([starting_x + x, starting[1]]))
                else:
                    starting_y = min(starting[1], ending[1])
                    for y in range(0, y_diff + 1):
                        coordinates.append(tuple([starting[0], starting_y + y]))

            if include_diagonal:
                degrees = math.atan2(x_diff, y_diff) * (180 / math.pi)
                if degrees == 45.0:
                    x_increment = 1 if starting[0] < ending[0] else -1
                    y_increment = 1 if starting[1] < ending[1] else -1
                    x = starting[0]
                    y = starting[1]
                    for i in range(0, x_diff + 1):
                        coordinates.append(tuple([x, y]))
                        x += x_increment
                        y += y_increment

        return coordinates

    def __build_diagram(self, coordinates):

        diagram = {}

        for c in coordinates:
            x = c[0]
            y = c[1]

            if y in diagram:
                counts = diagram[y]
                if x in counts:
                    counts[x] += 1
                else:
                    counts[x] = 1
            else:
                diagram[y] = {x: 1}

        return diagram

    def __count_hostile_points(self, diagram):

        hostile_point_count = 0

        for d in diagram:
            for p in diagram[d]:
                if diagram[d][p] >= 2:
                    hostile_point_count += 1

        return hostile_point_count
