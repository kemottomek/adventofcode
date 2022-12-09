import dataclasses
import os
import string
from collections import deque
from typing import AnyStr, List, Dict

working_directory = os.getcwd()


def get_text_file(file_name: string) -> AnyStr:
    with open("day9/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def fill_matrix(row, column) -> List[List[str]]:
    matrix: List[List[str]] = []
    for line in range(1, row + 1):
        matrix.append(["." for a in range(1, column + 1)])
    return matrix


def new_coorinates(x: int, y: int, command: str) -> List[List[int]]:
    direction: str = command.split(" ")[0]
    move: int = command.split(" ")[1]
    result: List[List[int]] = []
    for i in range(1, int(move) + 1):
        if "R" == direction:
            result.append([x + int(i), y])
        elif "L" == direction:
            result.append([x - int(i), y])
        elif "U" == direction:
            result.append([x, y + int(i)])
        elif "D" == direction:
            result.append([x, y - int(i)])

    return result


def print_matrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end=" ")
        print("\n")


def print_coordinates(head: List[int], tail: List[int]):
    matrix = fill_matrix(100, 100)
    matrix[len(matrix) - 1 - head[1]][head[0]] = "H"
    matrix[len(matrix) - 1 - tail[1]][tail[0]] = "T"
    print_matrix(matrix)


def run_part1() -> None:
    lines: str = get_text_file("input.txt").splitlines()
    x: int = 100
    y: int = 100
    seq: List[List[int]] = []
    head: tuple(int, int) = (x, y)
    tail: tuple(int, int) = (x, y)
    visited_count: Dict[tuple(int, int), int] = {}
    for line in lines:
        seq = new_coorinates(x, y, line)
        x = seq[len(seq) - 1][0]
        y = seq[len(seq) - 1][1]
        print(seq)
        for coo in seq:
            tmp = head
            head = coo
            # move only if distance > 1
            if (abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2):
                tail = tmp
                visited_count[str(tail)] = visited_count.get(str(tail), 0) + 1

            print("Head: " + str(head) + ", tail: " + str(tail))
            #print_coordinates(head, tail)
    print(visited_count)
    print(len(visited_count.keys()))


def run_part2() -> None:
    pass


def run_day() -> None:
    run_part1()
    run_part2()
