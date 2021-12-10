"""Day 10 Puzzle"""

import os
import statistics

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/10.txt")

CLOSING_CHARS_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}

ILLEGAL_CHAR_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}

CHUNK_OPEN_CHARS = ["(", "[", "{", "<"]
CHUNK_CLOSE_CHARS = [")", "]", "}", ">"]


class Puzzle10(PuzzleInterface):
    """Defines the day 10 puzzle"""

    def execute(self) -> None:
        """Executes the day 10 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 10 puzzle part 1"""
        syntax_error_score = 0

        for d in data:
            chunks = []
            for c in d:
                if c in CHUNK_OPEN_CHARS:
                    chunks.append(c)
                elif c in CHUNK_CLOSE_CHARS:
                    i = CHUNK_CLOSE_CHARS.index(c)
                    if CHUNK_OPEN_CHARS[i] == chunks[-1]:
                        chunks.pop()
                    else:
                        syntax_error_score += ILLEGAL_CHAR_POINTS[c]
                        break

        print(f"#10 (part 1) - The syntax error score is {syntax_error_score}")

    def __part2(self, data):
        """Executes the day 10 puzzle part 2"""
        completion_scores = []

        for d in data:
            chunks = []
            for c in d:
                if c in CHUNK_OPEN_CHARS:
                    chunks.append(c)
                elif c in CHUNK_CLOSE_CHARS:
                    i = CHUNK_CLOSE_CHARS.index(c)
                    if CHUNK_OPEN_CHARS[i] == chunks[-1]:
                        chunks.pop()
                    else:
                        chunks.clear()
                        break

            if len(chunks) > 0:
                completion_score = 0
                while chunks:
                    char = chunks.pop()
                    close_char = CHUNK_CLOSE_CHARS[CHUNK_OPEN_CHARS.index(char)]
                    completion_score = (completion_score * 5) + CLOSING_CHARS_POINTS[
                        close_char
                    ]
                completion_scores.append(completion_score)

        print(
            "#10 (part 2) - The middle completion score is"
            f" {statistics.median(completion_scores)}"
        )
