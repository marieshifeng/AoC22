def main(filename):
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

	elves = sorted(elves, reverse=True)
	print(elves[0])
	print(sum(elves[0:3]))
	return

filename = 'input.txt'
# filename = 'small.txt'
main(filename)