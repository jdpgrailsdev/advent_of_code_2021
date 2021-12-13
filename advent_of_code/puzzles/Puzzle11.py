"""Day 11 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/11.txt")


class Puzzle11(PuzzleInterface):
    """Defines the day 11 puzzle"""

    def execute(self) -> None:
        """Executes the day 11 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        data = self.__build_grid(data)

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 11 puzzle part 1"""
        total_flashes = 0
        for i in range(0, 100):
            for r, d in enumerate(data):
                for c, o in enumerate(d):
                    data[r][c] = tuple([o[0] + 1, o[1]])

            total_flashes += self.__flash(data)
            data = self.__reset(data)

        print(
            "#11 (part 1) - The total number of flashes after 100 turns is"
            f" {total_flashes}"
        )

    def __part2(self, data):
        """Executes the day 11 puzzle part 2"""
        flash_count = 0
        step = 0
        octopi_count = len(data) * len(data[0])

        while flash_count != octopi_count:
            step += 1
            for r, d in enumerate(data):
                for c, o in enumerate(d):
                    data[r][c] = tuple([o[0] + 1, o[1]])

            flash_count = self.__flash(data)
            data = self.__reset(data)

        print(f"#11 (part 2) - All octopi flash during step {step}")

    def __build_grid(self, data):
        grid = []

        for d in data:
            row = []
            for o in d:
                row.append(tuple([int(o), False]))

            grid.append(row)

        return grid

    def __flash(self, data):
        flash_count = 0

        for ir, r in enumerate(data):
            for ic, c in enumerate(r):
                if c[0] > 9 and c[1] is False:
                    flash_count += 1
                    data[ir][ic] = tuple([c[0], True])
                    data = self.__update_adjacent(data, ir, ic)

        if flash_count > 0:
            flash_count += self.__flash(data)

        return flash_count

    def __reset(self, data):
        for r, d in enumerate(data):
            for c, o in enumerate(d):
                value = 0 if o[1] is True else o[0]
                data[r][c] = tuple([value, False])

        return data

    def __update_adjacent(self, data, row, col):

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < len(data):
                    if 0 <= c < len(data[0]):
                        if r != row or c != col:
                            d = data[r][c]
                            data[r][c] = tuple([d[0] + 1, d[1]])

        return data
