def part1(filename):
	total = 0
	with open(filename) as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			first, second = set(line[:(len(line)//2)]), set(line[(len(line)//2):])
			both = first.intersection(second).pop()
			if both.isupper():
			    val = (ord(both) - ord('A') + 27)
			else:
			    val = (ord(both) - ord('a') + 1)
			total += val
	f.close()
	return total

def part2(filename):
	total = 0
	counter = 0
	cache = list()

	with open(filename) as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			cache.append(set(line))
	f.close()

	while counter < len(cache):
	    letter = cache[counter] & cache[counter+1] & cache[counter+2]
	    letter = letter.pop()
	    counter += 3
	    if letter.isupper():
	        val = ord(letter) - ord('A') + 27
	    else:
	        val = ord(letter) - ord('a') + 1
	    total += val
	return total

filename = "input.txt"
print(part1(filename)) #7821
print(part2(filename)) #2752