import functools

def pretty_print(out):
    for o in out:
        print(o)
    print()

def is_right_order(l, r):
    if type(l) is int and type(r) is int:
        if l < r:
            return -1
        elif l > r:
            return 1
        elif l == r:
            return 0
    elif type(l) is int:
        l = [l]
    elif type(r) is int:
        r = [r]
    n, m = len(l), len(r)
    for ll, rr in zip(l, r):
        x = is_right_order(ll, rr)
        if x != 0:
            return x
    if n < m:
        return -1
    elif n == m:
        return 0
    else:
        return 1

def part1(filename):
    out = list()
    with open(filename) as f:
        lines = f.read().strip()
        lines = lines.split("\n\n")
        packets_pairs = []
        packets_all = []
        for x in lines:
            l, r = x.split("\n")
            packets_pairs.append((eval(l),eval(r)))
            packets_all.append(eval(l))
            packets_all.append(eval(r))
        for i, (l, r) in enumerate(packets_pairs):
            if is_right_order(l, r) == -1:
                out.append(i + 1)
    f.close()
    return packets_all, sum(out)

DIVIDER1 = [[2]]
DIVIDER2 = [[6]]

def part2(packets):
    packets.append(DIVIDER1)
    packets.append(DIVIDER2)
    # pretty_print(packets)
    packets = sorted(packets, key=functools.cmp_to_key(is_right_order))
    # for i in range(len(packets)):
    #     for j in range(len(packets)-1):
    #         if is_right_order(packets[j], packets[j+1]) > 0:
    #             packets[j], packets[j+1] = packets[j+1], packets[j]
    # pretty_print(packets)
    return (packets.index(DIVIDER1) + 1) * (packets.index(DIVIDER2) + 1)

# filename = "small.txt"
filename = "input.txt"
packets, part1 = part1(filename)
print(part1) #5390
print(part2(packets)) #19261