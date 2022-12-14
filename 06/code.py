LEN_SOP = 4
LEN_SOM = 14

def process(filename, len_marker):
    count = 0
    cache = ""
    with open(filename) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            if len(cache) < len_marker:
                cache += c
            else:
                if len(set(cache)) == len_marker:
                    return count
                else:
                    cache = cache[1:] + c
            count += 1
    f.close()
    return count

def part1(filename):
   return process(filename, LEN_SOP)

def part2(filename):
   return process(filename, LEN_SOM)

# filename = "small.txt"
filename = "input.txt"
print(part1(filename)) #1855
print(part2(filename)) #3256