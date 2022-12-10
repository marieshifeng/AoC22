def process(filename):
    grid = list()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            if line[0] == "noop":
                grid.append(0)
            else:
                grid.append(int(line[1]))
    f.close()
    return grid

def part1(grid):
    X = 1
    time = 0
    log = [X]
    for x in grid:
        time += 1
        log.append(X)
        if x != 0:
            time += 1
            X += x
            log.append(X)
    return log, sum([log[19]*20, log[59]*60, log[99]*100, log[139]*140, log[179]*180, log[219]*220])

def part2(log):
    out = ""
    position = 0
    for i, x in enumerate(log):
        if x-1 <= position <= x+1:
            out += "#"
        else:
            out += "."
            # out += " "
        if (i+1) % 40 == 0:
            out += "\n"
            position = -1
        position += 1
    return out[0:-2]

# filename = "small.txt"
# medium_answer = "##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######....."
# filename = "medium.txt"
filename = "input.txt"
grid = process(filename)
log, part1 = part1(grid)
print(part1) #11720
# part2 = part2(log)
# assert medium_answer == part2
print(part2(log)) #ERCREPCJ