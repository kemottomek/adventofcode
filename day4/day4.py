import os
import string
from typing import AnyStr, List

working_directory = os.getcwd()


def to_reconcile(first_window: str, second_window: str) -> bool:
    begin_idx_1: int = int(first_window.split("-")[0])
    end_idx_1: int = int(first_window.split("-")[1])
    begin_idx_2: int = int(second_window.split("-")[0])
    end_idx_2: int = int(second_window.split("-")[1])
    if begin_idx_1 >= begin_idx_2 and end_idx_1 <= end_idx_2:
        return True
    if begin_idx_2 >= begin_idx_1 and end_idx_2 <= end_idx_1:
        return True
    return False


def to_reconcile_full(first_window: str, second_window: str) -> bool:
    begin_idx_1: int = int(first_window.split("-")[0])
    end_idx_1: int = int(first_window.split("-")[1])
    begin_idx_2: int = int(second_window.split("-")[0])
    end_idx_2: int = int(second_window.split("-")[1])
    if begin_idx_2 <= begin_idx_1 <= end_idx_2:
        return True
    if begin_idx_2 <= end_idx_1 <= end_idx_2:
        return True
    if begin_idx_1 <= begin_idx_2 <= end_idx_1:
        return True
    if begin_idx_1 <= end_idx_2 <= end_idx_1:
        return True
    return False


def get_text_file(file_name: string) -> AnyStr:
    with open("day4/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def run_part1() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    counted: int = 0
    for line in read_file:
        first_elf_range, second_elf_range = line.split(",")
        if to_reconcile(first_elf_range, second_elf_range):
            counted += 1
    print(counted)


def run_part2() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    counted: int = 0
    for line in read_file:
        first_elf_range, second_elf_range = line.split(",")
        if to_reconcile_full(first_elf_range, second_elf_range):
            counted += 1
    print(counted)


def run_day() -> None:
    run_part1()
    run_part2()
