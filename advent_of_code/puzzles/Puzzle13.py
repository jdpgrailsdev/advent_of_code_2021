"""Day 13 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface
from collections import defaultdict

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/13.txt")


class Puzzle13(PuzzleInterface):
    """Defines the day 13 puzzle"""

    def execute(self) -> None:
        """Executes the day 13 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 13 puzzle part 1"""
        dots, folds = self.__parse_input(data)
        paper = self.__build_paper(dots)
        direction, location = folds[0].split('=')
        folded = self.__fold(direction, int(location), paper)
        visible_dots = 0

        for point in folded:
            if folded[point] == '#':
                visible_dots += 1

        print(
            f"#13 (part 1) - The number of visible dots after 1 fold is {visible_dots}")

    def __part2(self, data):
        """Executes the day 13 puzzle part 2"""
        dots, folds = self.__parse_input(data)
        paper = self.__build_paper(dots)

        for fold in folds:
            direction, location = fold.split('=')
            paper = self.__fold(direction, int(location), paper.copy())

        max_x = max([key[0] for key in paper.keys()])
        max_y = max([key[1] for key in paper.keys()])

        letters = '\n'
        for y in range(0, max_y+1):
            row = ''
            for x in range(0, max_x+1):
                value = paper[(x, y)]
                row += value
            letters += row + '\n'

        print(
            f"#13 (part 2) - The activate code is: {letters}")

    def __build_paper(self, dots):
        paper = defaultdict(lambda: '.')

        for dot in dots:
            x, y = map(int, dot.split(','))
            paper[x, y] = '#'

        return paper

    def __fold(self, direction, location, paper):
        new_paper = paper.copy()
        for points in paper:
            point = points[0] if direction == 'x' else points[1]
            if point > location:
                value = paper[points]
                if value == '#':
                    translated_x = (location*2) - points[0] if direction == 'x' else points[0]
                    translated_y = (location*2) - points[1] if direction == 'y' else points[1]
                    new_paper[translated_x, translated_y] = value
                    new_paper.pop(points)
            elif point == location:
                new_paper[points] = '.'

        return new_paper

    def __parse_input(self, data):
        dots = []
        folds = []

        for d in data:
            if d.startswith('fold'):
                folds.append(d.replace('fold along ', ''))
            elif len(d) > 0:
                dots.append(d)

        return dots, folds
