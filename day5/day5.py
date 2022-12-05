import os
import re
import string
from typing import AnyStr, List

working_directory = os.getcwd()


def decode(text: str) -> tuple:
    # move 1 from 2 to 1
    numbers: list[int] = re.findall("[0-9]+", text)
    return int(numbers[0]), int(numbers[1]) - 1, int(numbers[2]) - 1,


def load_init() -> List[List[str]]:
    result: List[List[str]] = \
        [["G", "T", "R", "W"],
         ["G", "C", "H", "P", "M", "S", "V", "W"],
         ["C", "L", "T", "S", "G", "M"],
         ["J", "H", "D", "M", "W", "R", "F"],
         ["P", "Q", "L", "H", "S", "W", "F", "J"],
         ["P", "J", "D", "N", "F", "M", "S"],
         ["Z", "B", "D", "F", "G", "C", "S", "J"],
         ["R", "T", "B"],
         ["H", "N", "W", "L", "C"]
         ]
    return result


def move_by(origin: List[List[str]], element_no: int, from_idx: int, to_idx: int) -> List[List[str]]:
    result: List[List[str]] = origin
    for i in range(element_no):
        result[to_idx].append(result[from_idx].pop())
    return result


def move_by_without_reserve(origin: List[List[str]], element_no: int, from_idx: int, to_idx: int) -> List[List[str]]:
    result: List[List[str]] = origin
    elements: List[str] = []
    for i in range(element_no):
        elements.append(result[from_idx].pop())

    for i in reversed(elements):
        result[to_idx].append(i)
    return result


def get_text_file(file_name: string) -> AnyStr:
    with open("day5/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def print_last_element(origin: List[List[str]]) -> str:
    result: str = ""
    for queue in origin:
        result = result + queue[len(queue)-1]
    return result


def run_part1() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    shuffled_list: List[List[str]] = load_init()
    for idx, line in enumerate(read_file):
        if idx < 10:
            continue
        move_number, from_idx, to_idx = decode(line)
        print("%s, %s, %s" % (str(move_number), str(from_idx), str(to_idx)))
        shuffled_list = move_by(shuffled_list, move_number, from_idx, to_idx)
        print(shuffled_list)
    print(print_last_element(shuffled_list))


def run_part2() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    shuffled_list: List[List[str]] = load_init()
    for idx, line in enumerate(read_file):
        if idx < 10:
            continue
        move_number, from_idx, to_idx = decode(line)
        print("%s, %s, %s" % (str(move_number), str(from_idx), str(to_idx)))
        shuffled_list = move_by_without_reserve(shuffled_list, move_number, from_idx, to_idx)
        print(shuffled_list)
    print(print_last_element(shuffled_list))

def run_day() -> None:
    run_part1()
    run_part2()
