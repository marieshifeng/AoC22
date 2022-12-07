# https://treelib.readthedocs.io/en/latest/
from treelib import Node, Tree

LIMIT = 100000
TOTAL = 70000000
UNUSED = 30000000

def process(filename):
    files = None
    pointer = None
    counter = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            token = line[0]
            if token == "$":
                command = line[1]
                if command == "cd":
                    file = line[2]
                    if file == "..":
                        pointer = files[pointer].tag[2]
                    elif file == "/":
                        files = Tree()
                        files.create_node([file, 0, None], file)
                        pointer = file
                    else:
                        identifier = file + pointer
                        if identifier not in files:
                            files.create_node([file, 0, pointer], identifier, parent=pointer)
                        pointer = identifier
                elif command == "ls":
                    continue
            elif token == "dir":
                identifier = line[1] + pointer
                if identifier not in files:
                    files.create_node([line[1], 0, pointer], identifier, parent=pointer)
                else:
                    pass
            else:
                identifier = line[1] + pointer
                if identifier in files:
                    files.update_node(line[1],tag=[line[1], int(line[0]), pointer])
                else:
                    files.create_node([line[1], int(line[0]), pointer], identifier, parent=pointer)
    # files.show()
    f.close()
    return files

def inner(files, out, start, limit):
    total = 0
    children = files.children(start)
    for child in children:
        if child.is_leaf():
            total += child.tag[1]
        else:
            subtree = files.subtree(child.identifier)
            size, out = inner(subtree, out, child.identifier, limit)
            total += size
    if total <= limit:
        out.append(total)
    return total, out

def part1(files):
    total, out = inner(files, [], "/", LIMIT)
    return sum(out)

def part2(files):
    total, out = inner(files, [], "/", float("inf"))
    unused = TOTAL - total
    needed = UNUSED - unused
    out.sort()
    for o in out:
        if o > needed:
            return o

# filename = "small.txt"
filename = "input.txt"
files = process(filename)
print(part1(files)) #1642503
print(part2(files)) #6999588