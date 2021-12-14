"""Day 14 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/14.txt")


class Puzzle14(PuzzleInterface):
    """Defines the day 14 puzzle"""

    def execute(self) -> None:
        """Executes the day 14 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 14 puzzle part 1"""

        template, rules = self.__load_data(data)

        for i in range(0, 10):
            template = self.__insert(template, rules)

        char_min, char_max = self.__find_min_max_character(template)

        print(
            f"#14 (part 1) - The difference between the frequency of the most and least occurring polymer is {char_max - char_min}"
        )

    def __part2(self, data):
        """Executes the day 14 puzzle part 2"""

        template, rules = self.__load_data(data)
        pairs = {}

        for i, t in enumerate(template):
            if i < len(template) - 1:
                pair = t + template[i+1]
                if pair in pairs:
                    pairs[pair] += 1
                else:
                    pairs[pair] = 1

        for i in range(0, 40):
            pairs = self.__generate_pairs(pairs, rules)

        char_min, char_max = min(pairs, key=pairs.get), max(pairs, key=pairs.get)
        min_count, max_count = pairs[char_min], pairs[char_max]

        print(
            f"#14 (part 2) - The difference between the frequency of the most and least occurring polymer is {max_count - min_count}"
        )

    def __load_data(self, data):
        template = data[0]
        rules = {}

        for d in data[2:]:
            pair, polymer = d.split(' -> ')
            rules[pair] = polymer

        return template, rules

    def __insert(self, template, rules):
        polymers = []

        for i, t in enumerate(template):
            if i < len(template) - 1:
                pair = t + template[i+1]
                polymers.append(pair[0])
                if pair in rules:
                    polymers.append(rules[pair])

        polymers.append(template[-1])

        return ''.join(polymers)

    def __generate_pairs(self, pairs, rules):
        new_pairs = {}

        for pair in pairs:
            if pair in rules:
                polymer = rules[pair]
                new_pair_left = pair[0] + polymer
                if new_pair_left in new_pairs:
                    new_pairs[new_pair_left] += 1
                else:
                    new_pairs[new_pair_left] = 1

                new_pair_right = polymer + pair[1]
                if new_pair_right in new_pairs:
                    new_pairs[new_pair_right] += 1
                else:
                    new_pairs[new_pair_right] = 1
            else:
                if pair in new_pairs:
                    new_pairs[pair] += 1
                else:
                    new_pairs[pair] = 1

        return new_pairs

    def __find_min_max_character(self, polymers):
        freq = {}

        for p in polymers:
            if p in freq:
                freq[p] += 1
            else:
                freq[p] = 1

        char_min, char_max = min(freq, key=freq.get), max(freq, key=freq.get)
        return freq[char_min], freq[char_max]