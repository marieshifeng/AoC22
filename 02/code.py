def main(filename):
	elves = list()
	total = 0

	A = 'A' #rock
	B = 'B' #paper
	C = 'C' #scissor
	# X = 'X' #1 #rock
	# Y = 'Y' #2 #paper
	# Z = 'Z' #3 #sciss
	# codes = {'X':1, 'Y': 2, 'Z': 3}

	X = 'X' #1 #lose
	Y = 'Y' #2 #draw
	Z = 'Z' #3 #win
	codes = {'X':0, 'Y': 3, 'Z': 6}
	
	with open(filename) as f:
		lines = f.readlines()
		for i,x in enumerate(lines):
			line = x.split()
			# if line[0] == 'A': #rock
			# 	if line[1] == 'X':
			# 		score = 3
			# 	elif line[1] == 'Y':
			# 		score = 6
			# 	else:
			# 		score = 0
			# elif line[0] == 'B': #paper
			# 	if line[1] == 'X':
			# 		score = 0
			# 	elif line[1] == 'Y':
			# 		score = 3
			# 	else:
			# 		score = 6
			# else: #scissor
			# 	if line[1] == 'X':
			# 		score = 6
			# 	elif line[1] == 'Y':
			# 		score = 0
			# 	else:
			# 		score = 3
			if line[0] == 'A': #rock
				if line[1] == 'X': #scissor
					score = 3
				elif line[1] == 'Y': #rock
					score = 1
				else:
					score = 2
			elif line[0] == 'B': #paper
				if line[1] == 'X': #rock
					score = 1
				elif line[1] == 'Y':
					score = 2
				else:
					score = 3
			else: #scissor
				if line[1] == 'X':
					score = 2
				elif line[1] == 'Y':
					score = 3
				else:
					score = 1




			total += codes[line[1]] + score

				


			# if line == "\n" or i == len(lines)-1:
			# 	elves.append(total)
			# 	total = 0
			# 	continue
			# total += int(line.strip())
	f.close()

	# elves = sorted(elves, reverse=True)
	# print(elves[0])
	# print(sum(elves[0:3]))
	print(total)
	return

filename = 'input.txt'
# filename = 'small.txt'
main(filename)