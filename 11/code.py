import math

def process(filename):
    notes, queue = list(), list()
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.split()
            if i%7 == 0:
                monkey = list()
            elif i%7 == 1:
                items = list()
                for j in range(2, len(line)):
                    item = int(line[j][:-1]) if line[j].find(",") != -1 else int(line[j])
                    items.append(item)
                queue.append(items)
            elif i%7 == 2:
                operation = [line[-2], line[-1]] if line[-1] == "old" else [line[-2], int(line[-1])]
                monkey.append(operation)
            elif 3 <= i%7 <= 5:
                monkey.append(int(line[-1]))
                if i == (len(lines) - 1):
                    notes.append(monkey)
            elif i%7 == 6:
                notes.append(monkey)
    f.close()
    return notes, queue

def inner(notes, queue, limit, is_relief):
    activity = [0] * len(notes)
    # "(a mod kn) mod n = a mod n for any integer k. so instead of 
    # storing `a` we store `a mod kn` where k = the product of all 
    # of the other checks"
    # https://en.wikipedia.org/wiki/Modular_arithmetic
    modulo = math.prod([i[1] for i in notes])
    for r in range(limit):
        for m in range(len(notes)):
            while queue[m]:
                item = queue[m].pop(0)
                operation, value = notes[m][0]
                if value == "old":
                    value = item
                if operation == "+":
                    item += value
                elif operation == "*":
                    item *= value
                item = item // 3 if is_relief else item % modulo
                if not item%notes[m][1]:
                    queue[notes[m][2]].append(item)
                else:
                    queue[notes[m][3]].append(item)
                activity[m] += 1
    activity.sort()
    return activity[-1] * activity[-2]

def part1(notes, queue):
    return inner(notes, queue, 20, True)

def part2(notes, queue):
    return inner(notes, queue, 10000, False)

# filename = "small.txt"
filename = "input.txt"
print(part1(*process(filename))) #55944
print(part2(*process(filename))) #15117269860