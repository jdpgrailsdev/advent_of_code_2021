"""Day 15 Puzzle"""

import os
import queue

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/15.txt")


class Puzzle15(PuzzleInterface):
    """Defines the day 15 puzzle"""

    def execute(self) -> None:
        """Executes the day 15 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 15 puzzle part 1"""
        graph = self.__build_graph(data)
        width = max(map(lambda k: k[0], graph.keys()))
        height = max(map(lambda k: k[1], graph.keys()))
        risk = self.__find_cost(graph, height, width)
        print(f"#15 (part 1) - The lowest total risk of any path is {risk}")

    def __part2(self, data):
        """Executes the day 15 puzzle part 2"""
        graph = self.__build_graph(data)
        cave = self.__expand_graph(graph, len(data), len(data[0]))
        width = max(map(lambda k: k[0], cave.keys()))
        height = max(map(lambda k: k[1], cave.keys()))
        risk = self.__find_cost(cave, height, width)
        print(f"#15 (part 2) - The lowest total risk of any path is {risk}")

    def __build_graph(self, data):
        graph = {
            (x, y): int(risk)
            for y, line in enumerate(data)
            for x, risk in enumerate(line.strip())
        }
        return graph

    def __expand_graph(self, graph, height, width):
        cave = {}
        grid = 0

        while grid < 25:
            row_adjustment = (grid // 5) * height
            col_adjustment = (grid % 5) * width
            risk_adjustment = (grid % 5) + (grid // 5)
            for k in graph:
                new_key = (k[0] + col_adjustment, k[1] + row_adjustment)
                new_value = graph[k] + risk_adjustment
                if new_value > 9:
                    new_value -= 9
                cave[new_key] = new_value
            grid += 1

        return cave

    def __find_cost(self, graph, height, width):
        q = queue.PriorityQueue()
        q.put((0, (0, 0)))
        risks = {(0, 0): 0}

        while q.empty() is False:
            risk, node = q.get()
            neighbors = self.__get_neighbors(node, graph, height, width)
            for neighbor in neighbors:
                new_risk = risk + graph[neighbor]

                if neighbor[0] == width and neighbor[1] == height:
                    return new_risk

                if neighbor in risks and risks[neighbor] <= new_risk:
                    continue

                risks[neighbor] = new_risk
                q.put((new_risk, neighbor))

    def __get_neighbors(self, node, graph, height, width):
        neighbors = []

        for n in {(1, 0), (0, 1)}:
            new_x = node[0] + n[0]
            new_y = node[1] + n[1]

            if not (new_x > width or new_y > height):
                neighbors.append((new_x, new_y))

        return neighbors
