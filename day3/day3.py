import os
import string
from typing import AnyStr, List

working_directory = os.getcwd()


def letter_prio(character: str) -> int:
    ascii_code: int = ord(character)
    if 97 <= ascii_code <= 122:
        return ascii_code - 96
    elif 65 <= ascii_code <= 90:
        return ascii_code - 38
    else:
        return 0


def get_text_file(file_name: string) -> AnyStr:
    with open("day3/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def run_part1() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    summed: int = 0
    for line in read_file:
        first_half: List[str] = line[:len(line) // 2]
        second_half: List[str] = line[len(line) // 2:]
        common_list: List[str] = set(first_half).intersection(second_half)
        convert_to_prior: List[int] = [letter_prio(x) for x in common_list if x]
        summed += sum(convert_to_prior)
    print(summed)


def run_part2() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    list_length: int = len(read_file)
    tmp_idx: int = 0
    summed: int = 0
    for idx, line in enumerate(read_file):
        if tmp_idx % 3 == 0:
            first_bucket: List[str] = read_file[idx]
            second_bucket: List[str] = read_file[idx+1]
            third_bucket: List[str] = read_file[idx+2]
            common_list: List[str] = set(first_bucket).intersection(second_bucket).intersection(third_bucket)
            convert_to_prior: List[int] = [letter_prio(x) for x in common_list if x]
            summed += sum(convert_to_prior)
        if tmp_idx % 3 == 2:
            tmp_idx = 0
        else:
            tmp_idx += 1
    print(summed)


def run_day3() -> None:
    run_part1()
    run_part2()
