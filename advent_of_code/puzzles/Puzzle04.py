"""Day 4 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/04.txt")


class Puzzle04(PuzzleInterface):
    """Defines the day 4 puzzle"""

    def execute(self) -> None:
        """Executes the day 4 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()
        draw_numbers = data.pop(0).split(",")
        boards = self.__build_boards(data)
        self.__part1(draw_numbers, boards)
        self.__part2(draw_numbers, boards)

    def __part1(self, draw_numbers, boards):
        """Executes the day 4 puzzle part 1"""

        for n in draw_numbers:
            for b in boards:
                for row in b:
                    for i, v in enumerate(row):
                        if int(n) == v[0]:
                            value = list(v)
                            value[1] = True
                            row[i] = tuple(value)

                bingo = self.__test_board(b)
                if bingo is True:
                    unmarked = 0
                    for row in b:
                        for v in row:
                            if v[1] is False:
                                unmarked += v[0]

                    print(f"#04 (part 1) - The final score is {unmarked * int(n)}")
                    return

    def __part2(self, draw_numbers, boards):
        """Executes the day 4 puzzle part 2"""
        winning_boards = []

        for n in draw_numbers:
            for b in boards:
                for row in b:
                    for i, v in enumerate(row):
                        if int(n) == v[0]:
                            value = list(v)
                            value[1] = True
                            row[i] = tuple(value)

                bingo = self.__test_board(b)
                if bingo is True:
                    boards.remove(b)
                    winning_boards.append(tuple([int(n), b]))

        last_board = winning_boards.pop()
        unmarked = 0
        for row in last_board[1]:
            for v in row:
                if v[1] is False:
                    unmarked += v[0]

        print(f"#04 (part 2) - The final score is {unmarked * last_board[0]}")

    def __build_boards(self, data):
        """Builds the bingo board from the input"""
        boards = []
        current_board = []

        for d in data:
            if d == "":
                if len(current_board) > 0:
                    boards.append(current_board)
                current_board = []
            else:
                row = []
                numbers = d.split(" ")
                for n in numbers:
                    if n != "":
                        row.append(tuple([int(n), False]))

                current_board.append(row)

        return boards

    def __test_board(self, board):

        for r in board:
            row_bingo = True
            for v in r:
                if False in v:
                    row_bingo = False

            if row_bingo is True:
                return True

        for col in range(0, len(board[0])):
            col_bingo = True
            for r in board:
                if False in r[col]:
                    col_bingo = False

            if col_bingo is True:
                return True

        return False
