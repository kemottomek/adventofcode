import os

working_directory = os.getcwd()


def run_day1() -> None:
    sumed: int = 0
    sum_max: int = 0
    num_list: int = []
    with open(working_directory + "/day1/input.txt") as file:
        mylist = file.read().splitlines()
        for line in mylist:
            if not line:
                sum_max = max(sumed, sum_max)
                num_list.append(sumed)
                sumed = 0
            else:
                sumed += int(line)
    num_list.sort(reverse=True)
    print("Max result is: %s" % sum_max)
    print(num_list[:3])
    print("Sum of 3 max elements %s " % sum(num_list[:3]))
