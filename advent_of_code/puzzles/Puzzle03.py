"""Day 3 Puzzle"""

import os
from collections import Counter

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/03.txt")


class Puzzle03(PuzzleInterface):
    """Defines the day 3 puzzle"""

    def execute(self) -> None:
        """Executes the day 3 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        reports = input_file.read().splitlines()
        self.__part1(reports)
        self.__part2(reports)

    def __part1(self, reports):
        """Executes the day 3 puzzle part 1"""
        diagnostic = self.__process_report(reports)
        gamma_string = ""
        epsilon_string = ""

        for key in diagnostic:
            bits = diagnostic[key]
            bit_counter = Counter(bits)
            gamma_string += str(bit_counter.most_common(1)[0][0])
            epsilon_string += str(bit_counter.most_common()[-1][0])

        epsilon_rate = int(epsilon_string, 2)
        gamma_rate = int(gamma_string, 2)
        print(
            "#03 (part 1) - The power consumption of the submarine is "
            f"{gamma_rate * epsilon_rate}"
        )

    def __part2(self, reports):
        """Executes the day 3 puzzle part 2"""

        oxygen_generator_rating = self.__find_oxygen_rating(reports.copy(), 0)
        co2_scrubber_rating = self.__find_co2_rating(reports.copy(), 0)

        print(
            "#03 (part 2) - The life support rating of the submarine is "
            f"{oxygen_generator_rating * co2_scrubber_rating}"
        )

    def __process_report(self, reports):
        """Processes the diagnostic report"""
        diagnostic = {}

        for d in reports:
            index = 0

            while index < len(d):
                value = d[index]
                if len(value) > 0:
                    bit = int(value)

                    if index in diagnostic:
                        diagnostic[index].append(bit)
                    else:
                        diagnostic[index] = [bit]

                index += 1

        return diagnostic

    def __filter_reports(self, reports, index, bit):
        """Filters the report to only those entries that have the provided bit at the provided index"""
        filtered_reports = []

        for r in reports:
            if r[index] == bit:
                filtered_reports.append(r)

        return filtered_reports

    def __find_oxygen_rating(self, reports, index):
        """Finds the oxygen rating"""
        bits = []

        for d in reports:
            bits.append(d[index])

        most_common_bit = "1" if bits.count("1") >= bits.count("0") else "0"

        reports = self.__filter_reports(reports, index, most_common_bit)

        if len(reports) == 1:
            return int(reports[0], 2)
        else:
            return self.__find_oxygen_rating(reports, index + 1)

    def __find_co2_rating(self, reports, index):
        """Finds the CO2 rating"""
        bits = []

        for d in reports:
            bits.append(d[index])

        least_common_bit = "0" if bits.count("0") <= bits.count("1") else "1"

        reports = self.__filter_reports(reports, index, least_common_bit)

        if len(reports) == 1:
            return int(reports[0], 2)
        else:
            return self.__find_co2_rating(reports, index + 1)
