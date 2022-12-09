import dataclasses
import os
import string
from collections import deque
from typing import AnyStr, List

working_directory = os.getcwd()


@dataclasses.dataclass
class System:
    name: str

@dataclasses.dataclass
class File(System):
    size: int

    def __str__(self):
        return self.name


@dataclasses.dataclass
class Directory(System):
    size: int


class Node:
    def __init__(self, value: System, parent=None):
        self.value = value
        self.children = []
        self.parent = parent

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def find_root(self):
        if self.parent is None:
            return self

        return self.parent.find_root()

    def breadth_first_traversal(self):
        queue = deque([self])
        while queue:
            current_node = queue.popleft()

            print(current_node.value)

            for child in current_node.children:
                queue.append(child)

    def print_tree(self):
        # Print the value of the current node
        print("type=%s, name=%s, size=%s " % (type(self.value), self.value.name, str(self.value.size)))

        # Recursively print the values of each child node
        for child in self.children:
            child.print_tree()


    def find_node_by_path(self, path):
        # if the path is empty, the current node is the node we are looking for
        if not path:
            return self

        # get the next node in the path
        next_node = path.pop(0)

        # search for the next node in the children of the current node
        for child in self.children:
            if child.value == next_node:
                # if the next node is found, search for the remaining nodes in the path in its children
                return self.find_node_by_path(child, path)

        # if the next node is not found, the path is invalid
        return None

    def add_dir_size(self, size: int):
        if type(self.value) is Directory:
            self.value.size += size
            if self.parent is not None:
                self.parent.add_dir_size(size)

    def traverse(self):
        # Yield the value of the current node
        yield self.value

        # Recursively traverse each child node
        for child in self.children:
            yield from child.traverse()

    def level_up(self):
        return self.parent


def get_text_file(file_name: string) -> AnyStr:
    with open("day7/%s" % file_name, 'r') as input_file:
        result = input_file.read()
    return result


def create_tress(line: str, node: Node) -> Node:
    is_dir = "dir" == line[0:3]
    is_cd = "$ cd " == line[0:5]
    is_ls = "$ ls" == line[0:4]
    is_file = line.split(" ")[0].isalnum()
    context_node: Node = node
    if is_dir:
        node.add_child(Node(Directory(name=line.split(" ")[1], size=0)))
    elif is_file:
        node.add_child(Node(File(name=line.split(" ")[1], size=line.split(" ")[0])))
        node.add_dir_size(int(line.split(" ")[0]))
    elif is_cd:
        cd_command_dir = line.removeprefix("$ cd ")
        if cd_command_dir == "..":
            context_node = node.parent
        else:
            context_node = [node for node in node.children if node.value.name == cd_command_dir][0]
    return context_node


def run_part1() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    stream_text: str = read_file
    root_dir: Directory = Directory(name="/", size=0)
    root_node: Node = Node(root_dir)
    context_node: Node = root_node
    for i, line in enumerate(read_file):
        if i > 0:
            context_node = create_tress(line, context_node)
    context_node.find_root().print_tree()
    # Return an iterator for traversing the tree
    iterator = root_node.traverse()

    summed_size = 0
    for value in iterator:
        if type(value) is Directory and value.size < 100000:
            summed_size += value.size
    print("Result is %s" % (str(summed_size)))


def run_part2() -> None:
    read_file: List[str] = get_text_file("input.txt").splitlines()
    stream_text: str = read_file
    root_dir: Directory = Directory(name="/", size=0)
    root_node: Node = Node(root_dir)
    context_node: Node = root_node
    for i, line in enumerate(read_file):
        if i > 0:
            context_node = create_tress(line, context_node)
    context_node.find_root().print_tree()
    max_size: int = 70000000
    at_least: int = 30000000
    currently_used: int = max_size - root_node.value.size
    min_to_delete: int = at_least - currently_used

    iterator = root_node.traverse()
    summed_size: List[int] = []
    for value in iterator:
        if type(value) is Directory and value.size >= min_to_delete:
            print(value)
            summed_size.append(value.size)
    print("Result is %s" % (min(summed_size)))

def run_day() -> None:
    #run_part1()
    run_part2()
