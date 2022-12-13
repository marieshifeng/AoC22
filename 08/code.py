def process(filename):
    grid = list()
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            row = list()
            for char in line:
                if char != "\n":
                    row.append(char)
            grid.append(row)
    f.close()
    return grid

def is_visible(grid, r, c):
    left = True
    for r_ in range(r):
        if grid[r_][c] >= grid[r][c]:
            left = False
            break
    right = True
    for r_ in range(r + 1, len(grid)):
        if grid[r_][c] >= grid[r][c]:
            right = False
            break
    up = True
    for c_ in range(c):
        if grid[r][c_] >= grid[r][c]:
            up = False
            break
    down = True
    for c_ in range(c + 1, len(grid[0])):
        if grid[r][c_] >= grid[r][c]:
            down = False
            break
    return (left | right | up | down)

def num_trees_seen(grid, r, c):
    left = 0
    for r_ in range(r - 1, -1, -1):
        left +=1
        if grid[r_][c] >= grid[r][c]:
            break
    right = 0
    for r_ in range(r + 1, len(grid)):
        right += 1
        if grid[r_][c] >= grid[r][c]:
            break
    up = 0
    for c_ in range(c - 1, -1, -1):
        up += 1
        if grid[r][c_] >= grid[r][c]:
            break
    down = 0
    for c_ in range(c + 1, len(grid[0])):
        down += 1
        if grid[r][c_] >= grid[r][c]:
            break
    return (left * right * up * down)

def part1(grid):
    count = len(grid) * 2 + (len(grid[0]) - 2) * 2
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            if is_visible(grid, r, c):
                count += 1
    return count

def part2(files):
    out = list()
    for r in range(1, len(grid) - 1):
        for c in range(1, len(grid[0]) - 1):
            out.append(num_trees_seen(grid, r, c))
    return max(out)

filename = "small.txt"
# filename = "input.txt"
grid = process(filename)
print(part1(grid)) #1695
print(part2(grid)) #287040