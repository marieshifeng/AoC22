'''
        [J]         [B]     [T]    
        [M] [L]     [Q] [L] [R]    
        [G] [Q]     [W] [S] [B] [L]
[D]     [D] [T]     [M] [G] [V] [P]
[T]     [N] [N] [N] [D] [J] [G] [N]
[W] [H] [H] [S] [C] [N] [R] [W] [D]
[N] [P] [P] [W] [H] [H] [B] [N] [G]
[L] [C] [W] [C] [P] [T] [M] [Z] [W]
 1   2   3   4   5   6   7   8   9 
'''

def inner(filename, is_reverse):
    crates = [
        ['L','N','W','T','D'],
        ['C','P','H'],
        ['W','P','H','N','D','G','M','J'],
        ['C','W','S','N','T','Q','L'],
        ['P','H','C','N'],
        ['T','H','N','D','M','W','Q','B'],
        ['M','B','R','J','G','S','L'],
        ['Z','N','W','G','V','B','R','T'],
        ['W','G','D','N','P','L'],
    ]
    count = 0
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            num_, from_, to_ = int(line[1]), int(line[3])-1, int(line[5])-1
            temp = list()
            for i in range(num_):
                thing = crates[from_].pop()
                temp.append(thing)
            if is_reverse:
                temp.reverse()
            crates[to_].extend(temp)
        out = ""
        for i in range(len(crates)):
            out += crates[i][-1]
    f.close()
    return out

def part1(filename):
    return inner(filename, False)

def part2(filename):
    return inner(filename, True)

filename = "input.txt"
print(part1(filename)) #TWSGQHNHL
print(part2(filename)) #JNRSCDWPP