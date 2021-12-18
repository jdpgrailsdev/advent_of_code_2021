"""Day 18 Puzzle"""

import math
import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/18.txt")


class Node:
    """Defines a node in a tree"""

    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert_left(self, left):
        self.left = left

    def insert_right(self, right):
        self.right = right

    def print(self):
        if self.value:
            print(self.value)
        else:
            print("root")
        if self.left:
            print("left ->")
            self.left.print()
        if self.right:
            print("right ->")
            self.right.print()


class Puzzle18(PuzzleInterface):
    """Defines the day 18 puzzle"""

    def execute(self) -> None:
        """Executes the day 18 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 18 puzzle part 1"""

        data = [
            "[1,2]",
            "[[1,2],3]",
            "[9,[8,7]]",
            "[[1,9],[8,5]]",
            "[[[[1,2],[3,4]],[[5,6],[7,8]]],9]",
            "[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]",
            "[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]",
        ]

        data = tuple(map(eval, data))

        for d in data:
            tree = self.__build_tree(d, Node(None))
            # result = self.__visit(tree, tree)
            # result.print()
            # print()

            # n.print()
            # print()

    def __part2(self, data):
        """Executes the day 18 puzzle part 2"""

    def __build_tree(self, data, root):
        for i, d in enumerate(data):
            if isinstance(d, list):
                new_node = self.__build_tree(d, Node("["))
                if root.left is None:
                    root.insert_left(new_node)
                else:
                    root.insert_right(new_node)
            else:
                new_node = Node(d)
                if i == 0:
                    root.insert_left(new_node)
                else:
                    root.insert_right(new_node)

        return root

    def __visit(self, node, previous, level=0):
        if node.value == "[":
            level += 1

        if level == 3 and node.value != "[":
            previous_value = (
                previous.value if previous.value and previous.value != "[" else 0
            )
            next_value = (
                node.right.value
                if node.right and node.right.value and node.right.value != "["
                else 0
            )
            node = self.__explode(node.left, previous_value, next_value)

        if node.value and node.value != "[" and node.value >= 10:
            node = self.__split(node.value)

        if node.left:
            node = self.__visit(node.left, node, level)

        if node.right:
            node = self.__visit(node.right, node, level)

        return node

    def __explode(self, node, previous, next):
        left_value = node.left.value + previous if previous > 0 else 0
        right_value = node.right.value + next if next > 0 else 0
        node = Node("[")
        node.insert_left(Node(left_value))
        node.insert_right(Node(right_value))
        return node

    def __split(self, regular_number):
        left_value = math.floor(regular_number / 2)
        right_value = math.ciel(regular_number / 2)
        node = Node("[")
        node.insert_left(Node(left_value))
        node.insert_right(Node(right_value))
        return node
