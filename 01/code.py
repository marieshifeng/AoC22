def process(filename):
	elves = list()
	total = 0
	
	with open(filename) as f:
		lines = f.readlines()
		for i,line in enumerate(lines):
			if line == "\n" or i == len(lines)-1:
				elves.append(total)
				total = 0
				continue
			total += int(line.strip())
	f.close()
	return sorted(elves, reverse=True)

def part1(elves):
	return elves[0]

def part2(elves):
	return sum(elves[:3])

# filename = "small.txt"
filename = "input.txt"
elves = process(filename)
print(part1(elves)) #72511
print(part2(elves)) #212117