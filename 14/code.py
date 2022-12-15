MIN_X = float("inf")
MAX_X = -float("inf")
MIN_Y = float("inf")
MAX_Y = -float("inf")
START = (500,0)

def pretty_print(rocks, sands = dict()):
    for y in range(MIN_Y, MAX_Y + 1):
        out = ""
        for x in range(MIN_X, MAX_X + 1):
            if y in rocks[x]:
                if (x, y) == START:
                    out += "+ "
                else:
                    out += "# "
            elif sands.get(x) and y in sands[x]:
                out += "o "
            else:
                out += ". "
        print(out)
    print()

def get_path(start, end):
    out = list()
    if start[0] == end[0]:
        delta = 1 if start[1] < end[1] else -1
        for i in range(start[1], end[1] + delta, delta):
            out.append((start[0], i))
    elif start[1] == end[1]:
        delta = 1 if start[0] < end[0] else -1
        for i in range(start[0], end[0] + delta, delta):
            out.append((i, start[1]))
    return out

def update_bounds(rock):
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    if rock[0] < MIN_X:
        MIN_X = rock[0]
    if rock[0] > MAX_X:
        MAX_X = rock[0]
    if rock[1] < MIN_Y:
        MIN_Y = rock[1]
    if rock[1] > MAX_Y:
        MAX_Y = rock[1]

def process(filename):
    rocks = {START[0]:{START[1]}}
    update_bounds(START)
    with open(filename) as f:
        lines = f.read().strip()
        lines = lines.split("\n")
        for line in lines:
            line = line.split("->")
            for start, end in zip(line, line[1:]):
                start = start.strip().split(",")
                end = end.strip().split(",")
                for step in get_path((int(start[0]), int(start[1])), (int(end[0]), int(end[1]))):
                    rocks.setdefault(step[0], set()).add(step[1])
                    update_bounds(step)
    # pretty_print(rocks)           
    f.close()
    return rocks

def is_blocked(rocks, sands, grain):
    return (rocks.get(grain[0]) and grain[1] in rocks[grain[0]]) or (sands.get(grain[0]) and grain[1] in sands[grain[0]])

def is_in_bounds(grain):
    return (grain[0] >= MIN_X and grain[1] <= MAX_Y) or (grain[0] <= MAX_X and grain[1] <= MAX_Y)

def part1(rocks):
    sands = dict()
    count = 0
    prev_, cur_ = (-1, -1), START
    while is_in_bounds(cur_) and prev_ != START:
        prev_ = (-1, -1)
        cur_ = START
        while cur_ != prev_ and is_in_bounds(cur_):
            if not is_blocked(rocks, sands, (cur_[0], cur_[1] + 1)):
                cur_, prev_ = (cur_[0], cur_[1] + 1), cur_
            elif not is_blocked(rocks, sands, (cur_[0] - 1, cur_[1] + 1)):
                cur_, prev_ = (cur_[0] - 1, cur_[1] + 1), cur_
            elif not is_blocked(rocks, sands, (cur_[0] + 1, cur_[1] + 1)):
                cur_, prev_ = (cur_[0] + 1, cur_[1] + 1), cur_
            else:
                sands.setdefault(cur_[0], set()).add(cur_[1])
                prev_ = cur_
                count += 1
    # pretty_print(rocks, sands)
    return count

def part2(rocks):
    global MAX_Y
    MAX_Y += 2
    start = (START[0] - (MAX_Y * 2)//2 , MAX_Y)
    end = (START[0] + (MAX_Y * 2)//2 , MAX_Y)
    for step in get_path(start, end):
        rocks.setdefault(step[0], set()).add(step[1])
        update_bounds(step)
    return part1(rocks)

# filename = "small.txt"
filename = "input.txt"
rocks = process(filename)
print(part1(rocks)) #674
print(part2(rocks)) #24958