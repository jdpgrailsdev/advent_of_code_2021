"""Day 19 Puzzle"""

import os
import re

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/19.txt")
MIN_OVERLAP = 12
TOTAL_BEACONS = 79
MAX_DISTANCE = 1000


class Puzzle19(PuzzleInterface):
    """Defines the day 19 puzzle"""

    def execute(self) -> None:
        """Executes the day 19 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 19 puzzle part 1"""
        scanner_reports = self.__build_scanner_reports(data)
        known_scanners = [(0, 0, 0)]
        known_beacons = scanner_reports[0]
        unknown_scanners = {k: scanner_reports[k] for k in scanner_reports.keys() if k != 0}
        #self.align(known_beacons, known_scanners, unknown_scanners)
        print(f"#19 (part 1) - The number of beacons is {len(known_beacons)}")

    def __part2(self, data):
        """Executes the day 19 puzzle part 2"""

    def __build_scanner_reports(self, data):
        reports = {}
        scanner_key = None

        for d in data:
            group = re.search("--- scanner (\\d+) ---", d)
            if group:
                scanner_key = int(group[1])
            elif d.strip():
                if scanner_key not in reports:
                    reports[scanner_key] = []

                reports[scanner_key].append(tuple(map(int, d.split(','))))

        return reports

    def align(self, known_beacons, known_scanners, unknown_scanners):
        not_done = True
        while unknown_scanners and not_done:
            not_done = True
            for scanner in unknown_scanners:
                report = unknown_scanners[scanner]
                beacons, position = self.orient(known_beacons, report)
                if beacons:
                    unknown_scanners.remove(scanner)
                    known_beacons |= beacons
                    known_scanners.append(position)
                    not_done = False

    def orient(self, beacons, report):
        for x_adjustment in {-1, 0, 1}:
            for y_adjustment in {-1, 0, 1}:
                for z_adjustment in {-1, 0, 1}:
                    adjusted = [self.adjust(x_adjustment, y_adjustment, z_adjustment, r) for r in
                                report]
                    common_beacons, position = self.compare(beacons, adjusted)
                    if common_beacons:
                        return common_beacons, position

        return None, None

    def adjust(self, x_adjustment, y_adjustment, z_adjustment, report):
        return (report[0] * x_adjustment if x_adjustment != 0 else report[0],
                report[1] * y_adjustment if y_adjustment != 0 else report[1],
                report[2] * z_adjustment if z_adjustment != 0 else report[2])

    def compare(self, beacons, adjusted):
        for axis in range(3):
            sorted_beacons = sorted(beacons, key=lambda position: position[axis])
            adjusted.sort(key=lambda position: position[axis])
            beacon_diffs = self.relative(beacons)
            adjusted_diffs = self.relative(adjusted)
            print(f"beacon = {beacon_diffs}, adjusted={adjusted_diffs}")
            intersection = set(beacon_diffs) & set(adjusted_diffs)
            if intersection:
                difference = intersection.pop()
                bx, by, bz = sorted_beacons[beacons.index(difference)]
                ax, ay, az = adjusted[adjusted_diffs.index(difference)]
                cx, cy, cz = (ax - bx, ay - by, az - bz)
                relocated = {(x - cx, y - cy, z - cz) for (x, y, z) in adjusted}
                matched_beacons = beacons & relocated
                if len(matched_beacons) >= MIN_OVERLAP:
                    return relocated, (cx, cy, cz)

        return None, None

    def relative(self, readings):
        return [(pos1[0] - pos0[0], pos1[1] - pos0[1], pos1[2] - pos0[2])
                for pos0, pos1 in zip(readings, readings[1:])]
