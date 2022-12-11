import math

def process(filename):
    notes = list()
    stack = list()
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.split()
            if i%7 == 0:
                monkey = list()
            elif i%7 == 1:
                items = list()
                for j in range(2, len(line)):
                    if line[j].find(",") != -1:
                        item = int(line[j][:-1])
                    else:
                        item = int(line[j])
                    items.append(item)
                stack.append(items)
            elif i%7 == 2:
                if line[-1] == "old":
                    operation = [line[-2], "old"]
                else:
                    operation = [line[-2], int(line[-1])]
                monkey.append(operation)
            elif i%7 == 3:
                monkey.append(int(line[-1]))
            elif i%7 == 4:
                monkey.append(int(line[-1]))
            elif i%7 == 5:
                monkey.append(int(line[-1]))
                if i == (len(lines)-1):
                    notes.append(monkey)
            elif i%7 == 6:
                notes.append(monkey)
    f.close()
    return notes, stack

def inner(notes, stack, limit, is_relief):
    activity = [0] * len(notes)
    # "(a mod kn) mod n = a mod n for any integer k. so instead of 
    # storing `a` we store `a mod kn` where k = the product of all 
    # of the other checks"
    modulo = math.prod([i[1] for i in notes])
    for r in range(limit):
        for m in range(len(notes)):
            while stack[m]:
                item = stack[m].pop(0)
                operation = notes[m][0][0]
                value = notes[m][0][1]
                if value == "old":
                    value = item
                if operation == "+":
                    item += value
                elif operation == "*":
                    item *= value
                if is_relief:
                    item //= 3
                else:
                    item %= modulo
                if not item%notes[m][1]:
                    stack[notes[m][2]].append(item)
                else:
                    stack[notes[m][3]].append(item)
                activity[m] += 1
    activity.sort()
    return activity[-1]*activity[-2]

def part1(notes, stack):
    return inner(notes, stack, 20, True)

def part2(notes, stack):
    return inner(notes, stack, 10000, False)

# filename = "small.txt"
filename = "input.txt"
print(part1(*process(filename))) #55944
print(part2(*process(filename))) #