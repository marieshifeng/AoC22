KNOTS = 10

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
    if head == tail:
        return tail, False
    elif head[0] == tail[0]: # same row
        new_tail = head[1] - tail[1]
        if abs(new_tail) == 1:
            return tail, False
        elif new_tail > 0:
            new_tail = tail[1] + 1
        else:
            new_tail = tail[1] - 1
        tail = (tail[0], new_tail)
    elif head[1] == tail[1]: # same column
        new_tail = head[0] - tail[0]
        if abs(new_tail) == 1:
            return tail, False
        elif new_tail > 0:
            new_tail = tail[0] + 1
        else:
            new_tail = tail[0] - 1
        tail = (new_tail, tail[1])
    else:
        if abs(head[0] - tail[0]) == 1 and abs(head[1] - tail[1]) == 1:
            return tail, False
        elif head[0] > tail[0] and head[1] > tail[1]: #UR
            tail = (tail[0] + 1, tail[1] + 1)
        elif head[0] > tail[0] and head[1] < tail[1]: #DR
            tail = (tail[0] + 1, tail[1] - 1)
        elif head[0] < tail[0] and head[1] > tail[1]: #UL
            tail = (tail[0] - 1, tail[1] + 1)
        elif head[0] < tail[0] and head[1] < tail[1]: #DR
            tail = (tail[0] - 1, tail[1] - 1)
    return tail, True

def part1(grid):
    cur_head = (0,0)
    cur_tail = (0,0)
    tail_positions = {cur_tail}
    for i in grid:
        direction, steps = i[0], i[1]
        for j in range(steps):
            if direction == "R":
                cur_head = (cur_head[0]+1, cur_head[1])
            elif direction == "L":
                cur_head = (cur_head[0]-1, cur_head[1])
            elif direction == "U":
                cur_head = (cur_head[0], cur_head[1]+1)
            elif direction == "D":
                cur_head = (cur_head[0], cur_head[1]-1)
            cur_tail, _ = move_tail(cur_head, cur_tail)
            tail_positions.add(cur_tail)
    return len(tail_positions)

def part2(grid):
    cur_head = [(0,0)] * KNOTS
    tail_positions = {cur_head[KNOTS - 1]}
    flag = True
    for i in grid:
        direction, steps = i[0], i[1]
        for j in range(steps):
            k = 0
            while k < KNOTS:
                if k == 0:
                    if direction == "R":
                        cur_head[k] = (cur_head[k][0]+1, cur_head[k][1])
                    elif direction == "L":
                        cur_head[k] = (cur_head[k][0]-1, cur_head[k][1])
                    elif direction == "U":
                        cur_head[k] = (cur_head[k][0], cur_head[k][1]+1)
                    elif direction == "D":
                        cur_head[k] = (cur_head[k][0], cur_head[k][1]-1)
                    k += 1
                else:
                    cur_head[k], flag = move_tail(cur_head[k-1], cur_head[k])
                    if k == KNOTS - 1:
                        tail_positions.add(cur_head[k]) ###
                    if not flag:
                        k = KNOTS
                    else:
                        k += 1
    return len(tail_positions)

# filename = "small.txt"
filename = "medium.txt"
# filename = "input.txt"
grid = process(filename)
print(part1(grid)) #6175
print(part2(grid)) #2578