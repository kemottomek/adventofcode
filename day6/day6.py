import os
import re
import string
from typing import AnyStr, List

working_directory = os.getcwd()


def get_text_file(file_name: string) -> AnyStr:
    with open("day6/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def run_part1() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    stream_text: str = read_file[0]
    for i in range(len(stream_text) - 3):
        window: List[str] = stream_text[i:i+4]
        if len(set(window)) == 4:
            print("Found unique: "+window)
            print(i+4)
            break


def run_part2() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    stream_text: str = read_file[0]
    for i in range(len(stream_text) - 13):
        window: List[str] = stream_text[i:i+14]
        if len(set(window)) == 14:
            print("Found unique: "+window)
            print(i+14)
            break

def run_day() -> None:
    run_part1()
    run_part2()
