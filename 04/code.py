def part1(filename):
    count = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(",")
            s1 = int(line[0][:line[0].index("-")])
            f1 = int(line[0][line[0].index("-")+1:])
            s2 = int(line[1][:line[1].index("-")])
            f2 = int(line[1][line[1].index("-")+1:])
            if s1 <= s2 <= f2 <=f1 or s2 <= s1 <= f1 <= f2:
                count += 1
    f.close()
    return count

def part2(filename):
    count = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split(",")
            s1 = int(line[0][:line[0].index("-")])
            f1 = int(line[0][line[0].index("-")+1:])
            s2 = int(line[1][:line[1].index("-")])
            f2 = int(line[1][line[1].index("-")+1:])
            if s1 <= f1 < s2 <= f2 or s2 <= f2 < s1 <= s1:
                pass
            else:
                count += 1
    f.close()
    return count
        
filename = "input.txt"
print(part1(filename)) #466
print(part2(filename)) #865