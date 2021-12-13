"""Day 12 Puzzle"""

import os

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/12.txt")


class Puzzle12(PuzzleInterface):
    """Defines the day 12 puzzle"""

    def execute(self) -> None:
        """Executes the day 12 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 12 puzzle part 1"""

        paths = self.__build_graph(data)
        available_paths = self.__find_paths("start", paths)
        print(
            "#12 (part 1) - The number of paths through the cave system is"
            f" {len(available_paths)}"
        )

    def __part2(self, data):
        """Executes the day 12 puzzle part 2"""

        paths = self.__build_graph(data)
        available_paths = self.__find_paths_2("start", paths)
        print(
            "#12 (part 2) - The number of paths through the cave system is"
            f" {len(available_paths)}"
        )

    def __build_graph(self, data):
        paths = {}

        for d in data:
            a, b = d.split("-")
            if a not in paths:
                paths[a] = set()
            if b not in paths:
                paths[b] = set()

            paths[a].add(b)
            paths[b].add(a)

        return paths

    def __find_paths(self, path, paths, visited=set(), accumulated_path=[]):
        if path in visited:
            return []
        elif path.islower():
            visited.add(path)

        accumulated_path.append(path)

        if path == "end":
            return [path]

        sub_paths = []
        for p in paths[path]:
            sub_path = self.__find_paths(
                p, paths, visited.copy(), accumulated_path.copy()
            )
            if sub_path:
                sub_paths.extend(sub_path)

        return sub_paths

    def __find_paths_2(self, path, paths, visited={}, accumulated_path=[]):
        if path in visited:
            if path == "start" or path == "end":
                return []
            elif list(visited.values()).__contains__(2):
                return []
            else:
                visited[path] = visited[path] + 1
        elif path.islower():
            visited[path] = 1

        accumulated_path.append(path)

        if path == "end":
            return [path]

        sub_paths = []
        for p in paths[path]:
            sub_path = self.__find_paths_2(
                p, paths, visited.copy(), accumulated_path.copy()
            )
            if sub_path:
                sub_paths.extend(sub_path)

        return sub_paths
