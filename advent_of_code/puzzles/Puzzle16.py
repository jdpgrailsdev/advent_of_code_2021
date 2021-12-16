"""Day 16 Puzzle"""

import math
import os
import sys

from advent_of_code.puzzles.PuzzleInterface import PuzzleInterface

INPUT_FILE_NAME = os.path.join(os.path.dirname(__file__), "../input/16.txt")

DECODER = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class Puzzle16(PuzzleInterface):
    """Defines the day 16 puzzle"""

    def execute(self) -> None:
        """Executes the day 16 puzzle"""
        input_file = open(INPUT_FILE_NAME, "r")
        data = input_file.read().splitlines()

        self.__part1(data)
        self.__part2(data)

    def __part1(self, data):
        """Executes the day 16 puzzle part 1"""
        version_total = self.__process_packet(self.__translate(data[0].strip()))
        print(f"#16 (part 1) - The sum of the version numbers is {version_total}")

    def __part2(self, data):
        """Executes the day 16 puzzle part 2"""
        _, result = self.__process_packet_2(self.__translate(data[0].strip()))
        print(f"#16 (part 1) - The result of the transmission is {result}")

    def __process_packet(self, bits):
        index = 0
        version_total = 0
        version = int(bits[index : index + 3], 2)
        index += 3
        type_id = int(bits[index : index + 3], 2)
        index += 3

        version_total += version

        if type_id == 4:
            more_bits = True
            value = ""
            while more_bits:
                group = bits[index : index + 1]
                index += 1
                value += str(int(bits[index : index + 4], 2))
                index += 4
                if group == "0":
                    more_bits = False
        else:
            length_type = int(bits[index : index + 1])
            index += 1

            if length_type == 0:
                total_length_in_bits = int(bits[index : index + 15], 2)
                index += 15
            else:
                number_of_sub_packets = int(bits[index : index + 11], 2)
                index += 11

        if index < len(bits):
            remaining_bits = bits[index:]
            if remaining_bits != len(remaining_bits) * "0":
                version_total += self.__process_packet(remaining_bits)

        return version_total

    def __process_packet_2(self, bits):
        index = 0
        result = 0

        if len(bits) > 0:
            if bits != len(bits) * "0":
                version = int(bits[index : index + 3], 2)
                index += 3
                type_id = int(bits[index : index + 3], 2)
                index += 3

                if type_id == 4:
                    more_bits = True
                    value = ""
                    while more_bits:
                        group = bits[index : index + 1]
                        index += 1
                        value += str(int(bits[index : index + 4], 2))
                        index += 4
                        if group == "0":
                            more_bits = False
                    result = int(value)
                else:
                    bits_processed, result = self.__process_operator_packet(
                        bits[index:], type_id
                    )
                    index += bits_processed

        return index, result

    def __process_operator_packet(self, bits, type_id):
        index = 0
        length_type = int(bits[index : index + 1])
        index += 1
        result = 0
        total_length_in_bits = 0
        number_of_sub_packets = 0

        if length_type == 0:
            total_length_in_bits = int(bits[index : index + 15], 2)
            index += 15
        else:
            number_of_sub_packets = int(bits[index : index + 11], 2)
            index += 11

        results = []
        if total_length_in_bits > 0:
            bits_processed = 0
            while bits_processed < total_length_in_bits:
                bp, value = self.__process_packet_2(bits[index:])
                bits_processed += bp
                index += bp
                results.append(value)
        else:
            for _ in range(number_of_sub_packets):
                bits_processed, value = self.__process_packet_2(bits[index:])
                results.append(value)
                index += bits_processed

        print(results)

        if type_id == 0:
            result = sum(results)
        elif type_id == 1:
            result = math.prod(results)
        elif type_id == 2:
            result = min(results)
        elif type_id == 3:
            result = max(results)
        elif type_id == 5:
            result = 1 if results[0] > results[1] else 0
        elif type_id == 6:
            result = 1 if results[0] < results[1] else 0
        else:
            result = 1 if results[0] == results[1] else 0

        return index, result

    def __translate(self, data):
        translated = ""
        for d in data:
            translated += DECODER[d]

        return translated
