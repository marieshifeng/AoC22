def part1(filename):
	elves = list()
	total = 0

	A = 'A' #rock
	B = 'B' #paper
	C = 'C' #scissors	
	X = 'X' #rock
	Y = 'Y' #paper
	Z = 'Z' #scissors
	codes = {'X':1, 'Y': 2, 'Z': 3}
	
	with open(filename) as f:
		lines = f.readlines()
		for i,x in enumerate(lines):
			line = x.split()
			if line[0] == 'A':
				if line[1] == 'X':
					score = 3
				elif line[1] == 'Y':
					score = 6
				else:
					score = 0
			elif line[0] == 'B':
				if line[1] == 'X':
					score = 0
				elif line[1] == 'Y':
					score = 3
				else:
					score = 6
			else:
				if line[1] == 'X':
					score = 6
				elif line[1] == 'Y':
					score = 0
				else:
					score = 3
			total += codes[line[1]] + score
	f.close()
	return total

def part2(filename):
	elves = list()
	total = 0

	A = 'A' #rock
	B = 'B' #paper
	C = 'C' #scissors
	X = 'X' #lose
	Y = 'Y' #draw
	Z = 'Z' #win
	codes = {'X':0, 'Y': 3, 'Z': 6}
	
	with open(filename) as f:
		lines = f.readlines()
		for i,x in enumerate(lines):
			line = x.split()
			if line[0] == 'A':
				if line[1] == 'X':
					score = 3
				elif line[1] == 'Y':
					score = 1
				else:
					score = 2
			elif line[0] == 'B':
				if line[1] == 'X':
					score = 1
				elif line[1] == 'Y':
					score = 2
				else:
					score = 3
			else:
				if line[1] == 'X':
					score = 2
				elif line[1] == 'Y':
					score = 3
				else:
					score = 1
			total += codes[line[1]] + score
	f.close()
	return total

# filename = "small.txt"
filename = "input.txt"
print(part1(filename)) #10718
print(part2(filename)) #14652