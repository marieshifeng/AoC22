from z3 import *

MIN_X = float("inf")
MAX_X = -float("inf")
MIN_Y = float("inf")
MAX_Y = -float("inf")

# Y = 10
Y = 2000000

grid = dict()

###

def update_bounds(thing):
    global MIN_X, MIN_Y, MAX_X, MAX_Y
    if thing[0] < MIN_X:
        MIN_X = thing[0]
    if thing[0] > MAX_X:
        MAX_X = thing[0]
    if thing[1] < MIN_Y:
        MIN_Y = thing[1]
    if thing[1] > MAX_Y:
        MAX_Y = thing[1]

def get_taxi_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

###

def pretty_print_old(sensors, beacons):
    for y in range(MIN_Y, MAX_Y + 1):
        out = ""
        for x in range(MIN_X, MAX_X + 1):
            if grid.get(x) and y in grid[x]:
                if (x, y) in sensors:
                    out += "S "
                elif (x, y) in beacons:
                    out += "B "
                else:
                    out += "# "
            else:
                out += ". " 
        print(out)
    print()

def count_in_row_old(beacons, row):
    count = 0
    for x in range(MIN_X, MAX_X + 1):
        if grid.get(x) and row in grid[x]:
            count += ((x, row) not in beacons)
    return count 

def get_blocked_area_old(sensor, beacon):
    out = set()
    distance = get_taxi_distance(sensor, beacon)
    for x in range(sensor[0] - distance, sensor[0] + distance + 1):
        for y in range(sensor[1] - distance, sensor[1] + distance + 1):
            if get_taxi_distance(sensor, (x, y)) <= distance:
                out.add((x, y))
    return out

def part1_old(filename):
    global grid
    sensors = set()
    beacons = set()
    with open(filename) as f:
        lines = f.read().strip()
        lines = lines.split("\n")
        for i, line in enumerate(lines):
            print(i)
            line = line.split()
            s_x = int((line[2].split("="))[1][:-1])
            s_y = int((line[3].split("="))[1][:-1])
            b_x = int((line[8].split("="))[1][:-1])
            b_y = int((line[9].split("="))[1])
            sensors.add((s_x, s_y))
            beacons.add((b_x, b_y))
            update_bounds((s_x, s_y))
            update_bounds((b_x, b_y))
            grid.setdefault(s_x, set()).add(s_y)
            grid.setdefault(b_x, set()).add(b_y)
            for i, (x, y) in enumerate(get_blocked_area_old((s_x, s_y), (b_x, b_y))):
                grid.setdefault(x, set()).add(y)
                update_bounds((x, y))
    pretty_print_old(sensors, beacons)           
    f.close()
    return count_in_row_old(beacons, Y)

###

def count_in_row(beacons, row):
    count = 0
    for x in range(MIN_X, MAX_X + 1):
        if grid.get(x) and row in grid[x]:
            count += ((x, row) not in beacons)
    return count

def get_blocked_area(sensor, beacon):
    out = set()
    distance = get_taxi_distance(sensor, beacon)
    for x in range(sensor[0] - distance, sensor[0] + distance + 1):
        delta = sensor[0] - x
        delta = abs(delta - distance) if delta > 0 else abs(delta + distance)
        if sensor[1] - delta <= Y < sensor[1] + delta + 1:
            out.add((x, Y))
    return out

def part1(filename):
    global grid
    sensors = set()
    beacons = set()
    with open(filename) as f:
        lines = f.read().strip()
        lines = lines.split("\n")
        for i, line in enumerate(lines):
            print(i)
            line = line.split()
            s_x = int((line[2].split("="))[1][:-1])
            s_y = int((line[3].split("="))[1][:-1])
            b_x = int((line[8].split("="))[1][:-1])
            b_y = int((line[9].split("="))[1])
            sensors.add((s_x, s_y))
            beacons.add((b_x, b_y))
            update_bounds((s_x, s_y))
            update_bounds((b_x, b_y))
            if s_y == Y:
                grid.setdefault(s_x, set()).add(s_y)
            if b_y == Y:
                grid.setdefault(b_x, set()).add(b_y)
            for j, (x, y) in enumerate(get_blocked_area((s_x, s_y), (b_x, b_y))):
                grid.setdefault(x, set()).add(y)
                update_bounds((x, y))
    f.close()
    return count_in_row(beacons, Y)

###

def part2(filename, limit):
    s = z3.Solver()
    x = z3.Int("x")
    y = z3.Int("y")
    s.add(0 <= x)
    s.add(x <= limit)
    s.add(0 <= y)
    s.add(y <= limit)

    def z3_abs(x):
        return z3.If(x >= 0, x, -x)

    with open(filename) as f:
        lines = f.read().strip()
        lines = lines.split("\n")
        for i, line in enumerate(lines):
            print(i)
            line = line.split()
            s_x = int((line[2].split("="))[1][:-1])
            s_y = int((line[3].split("="))[1][:-1])
            b_x = int((line[8].split("="))[1][:-1])
            b_y = int((line[9].split("="))[1])
            m = abs(s_x - b_x) + abs(s_y - b_y)
            s.add(z3_abs(s_x - x) + z3_abs(s_y - y) > m)
    f.close()

    assert s.check()
    out = s.model()
    # print(out)
    return out[x].as_long() * 4000000 + out[y].as_long()

# filename = "small.txt"
filename = "input.txt"
# print(part1_old(filename)) #26 but too slow for input.txt...
print(part1(filename)) #5870800
print()
# print(part2(filename, 20)) #56000011
print(part2(filename, 4000000)) #10908230916597