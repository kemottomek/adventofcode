import dataclasses
import os
import string
from collections import deque
from typing import AnyStr, List

working_directory = os.getcwd()


def get_text_file(file_name: string) -> AnyStr:
    with open("day8/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def fill_matrix() -> List[List[int]]:
    matrix: List[List[int]] = []
    read_file: List[str] = get_text_file("input.txt").splitlines()
    for line in read_file:
        matrix.append([int(a) for a in list(line)])
    return matrix


def run_part1() -> None:
    result: int = 0
    matrix: List[List[int]] = fill_matrix()
    idx_row_moved: int = 0
    idx_col_moved: int = 0
    for idx_row in range(len(matrix) - 2):
        idx_row_moved = idx_row + 1
        for idx_col in range(len(matrix[idx_row_moved]) - 2):
            idx_col_moved = idx_col + 1
            #left
            all_left: bool = False
            i: int = 0
            while i < idx_col_moved:
                if matrix[idx_row_moved][i] < matrix[idx_row_moved][idx_col_moved]:
                    all_left = True
                else:
                    all_left = False
                    break
                i += 1
            #if all_left:
            #    print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))


            #right
            all_right: bool = False
            i: int = idx_col_moved + 1
            while i < len(matrix[idx_row_moved]):
                if matrix[idx_row_moved][i] < matrix[idx_row_moved][idx_col_moved]:
                    all_right = True
                else:
                    all_right = False
                    break
                i += 1
            #if all_right:
            #    print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))

            #top
            all_top: bool = False
            i: int = 0
            while i < idx_row_moved:
                if matrix[i][idx_col_moved] < matrix[idx_row_moved][idx_col_moved]:
                    all_top = True
                else:
                    all_top = False
                    break
                i += 1
            #if all_top:
            #    print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))

            #buttom
            all_bottom: bool = False
            i: int = idx_row_moved + 1
            while i < len(matrix[idx_col_moved]):
                if matrix[i][idx_col_moved] < matrix[idx_row_moved][idx_col_moved]:
                    all_bottom = True
                else:
                    all_bottom = False
                    break
                i += 1
            if all_bottom or all_top or all_left or all_right:
                result += 1
                print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))


    result += 2 * (len(matrix) + len(matrix[0])) - 4
    print(result)

def run_part2() -> None:
    result: List[int] = []
    matrix: List[List[int]] = fill_matrix()
    idx_row_moved: int = 0
    idx_col_moved: int = 0
    for idx_row in range(len(matrix) - 2):
        idx_row_moved = idx_row + 1
        for idx_col in range(len(matrix[idx_row_moved]) - 2):
            idx_col_moved = idx_col + 1
            #left
            all_left: int = 0
            i: int = idx_col_moved - 1
            while i >= 0:
                if matrix[idx_row_moved][i] < matrix[idx_row_moved][idx_col_moved]:
                    all_left += 1
                elif matrix[idx_row_moved][i] >= matrix[idx_row_moved][idx_col_moved]:
                    all_left += 1
                    break
                else:
                    pass
                i -= 1
            #if all_left:
            #    print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))


            #right
            all_right: int = 0
            i: int = idx_col_moved + 1
            while i < len(matrix[idx_row_moved]):
                if matrix[idx_row_moved][i] < matrix[idx_row_moved][idx_col_moved]:
                    all_right += 1
                elif matrix[idx_row_moved][i] >= matrix[idx_row_moved][idx_col_moved]:
                    all_right += 1
                    break
                else:
                    pass
                i += 1
            #if all_right:
            #    print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))

            #top
            all_top: int = 0
            i: int = idx_row_moved - 1
            while i >= 0:
                if matrix[i][idx_col_moved] < matrix[idx_row_moved][idx_col_moved]:
                    all_top += 1
                elif matrix[i][idx_col_moved] >= matrix[idx_row_moved][idx_col_moved]:
                    all_top += 1
                    break
                else:
                    pass
                i -= 1
            #if all_top:
            #    print("For element [%s,%s]: value %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved])))

            #buttom
            all_bottom: int = 0
            i: int = idx_row_moved + 1
            while i < len(matrix[idx_col_moved]):
                if matrix[i][idx_col_moved] < matrix[idx_row_moved][idx_col_moved]:
                    all_bottom += 1
                elif matrix[i][idx_col_moved] >= matrix[idx_row_moved][idx_col_moved]:
                    all_bottom += 1
                    break
                else:
                    pass
                i += 1

            result1 = all_bottom * all_top * all_left * all_right
            result.append(result1)
            print("For element [%s,%s]: value %s = %s" % (str(idx_row_moved), str(idx_col_moved), str(matrix[idx_row_moved][idx_col_moved]), str(result1)))


    print(max(result))

def run_day() -> None:
    #run_part1()
    run_part2()
