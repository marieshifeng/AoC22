import math

def process(filename):
    grid = list()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            row = [line[0], int(line[1])]
            grid.append(row)
    f.close()
    return grid

def move_tail(head, tail):
    if head == tail or (abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1) \
                    or (head[0] == tail[0] and abs(head[1] - tail[1]) == 1) \
                    or (head[1] == tail[1] and abs(head[0] - tail[0]) == 1):
        return tail, False
    elif head[0] == tail[0]: # same row
        new_tail = tail[1] + int(math.copysign(1, head[1] - tail[1]))
        tail = (tail[0], new_tail)
    elif head[1] == tail[1]: # same column
        new_tail = tail[0] + int(math.copysign(1, head[0] - tail[0]))
        tail = (new_tail, tail[1])
    else:
        if head[0] > tail[0] and head[1] > tail[1]: #UR
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] > tail[0] and head[1] < tail[1]: #DR
            tail = (tail[0] + 1, tail[1] - 1)
        elif head[0] < tail[0] and head[1] > tail[1]: #UL
            tail = (tail[0] - 1, tail[1] + 1)
        elif head[0] < tail[0] and head[1] < tail[1]: #DR
            tail = (tail[0] - 1, tail[1] - 1)
    return tail, True

def inner(grid, knots):
    cur_head = [(0,0)] * knots
    tails = {cur_head[knots - 1]}
    flag = True
    for i in grid:
        direction, steps = i[0], i[1]
        for j in range(steps):
            k = 0
            while k < knots:
                if k == 0:
                    if direction == "R":
                        cur_head[k] = (cur_head[k][0]+1, cur_head[k][1])
                    elif direction == "L":
                        cur_head[k] = (cur_head[k][0]-1, cur_head[k][1])
                    elif direction == "U":
                        cur_head[k] = (cur_head[k][0], cur_head[k][1]+1)
                    elif direction == "D":
                        cur_head[k] = (cur_head[k][0], cur_head[k][1]-1)
                else:
                    cur_head[k], flag = move_tail(cur_head[k-1], cur_head[k])
                    if k == knots - 1:
                        tails.add(cur_head[k])
                        print(tails)
                    if not flag:
                        k = knots
                k += 1
    return len(tails)

def part1(grid):
    return inner(grid, 2)

def part2(grid):
    return inner(grid, 10)

# filename = "small.txt"
# filename = "medium.txt"
filename = "input.txt"
grid = process(filename)
print(part1(grid)) #6175
print(part2(grid)) #2578