def pretty_print(out):
    for r in range(len(out)):
        row = ""
        for c in range(len(out[0])):
            row += (str(out[r][c]) + " ")
        print(row)
    print()
    return

def next_steps(cur, R, C, grid):
    deltas = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    out = list()
    for d in deltas:
        o = (cur[0] + d[0], cur[1] + d[1])
        if 0 <= o[0] < R and 0 <= o[1] < C:
            o_char = "z" if grid[o[0]][o[1]] == "E" else grid[o[0]][o[1]]
            if ord(o_char) - ord(grid[cur[0]][cur[1]]) <= 1:
                out.append(o)
    return out

def process(filename, is_all):
    grid = list()
    s, e = list(), tuple()
    with open(filename) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            row = list()
            for j, char in enumerate(line):
                if char == "\n":
                    continue
                if char == "S" or (is_all and char == "a"):
                    s.append((i, j))
                    char = "a"
                elif char == "E":
                    e = (i, j)
                row.append(char)
            grid.append(row)
    f.close()
    return grid, s, e

def inner(grid, s, e):
    R, C = len(grid), len(grid[0])
    log = [[0] * C for _ in range(R)]
    queue = [s]
    visited = {s}
    while queue:
        cur = queue.pop(0)
        if cur == e:
            return log[e[0]][e[1]]
        for step in next_steps(cur, R, C, grid):
            if step not in visited:
                log[step[0]][step[1]] = log[cur[0]][cur[1]] + 1
                visited.add(step)
                queue.append(step)
            # pretty_print(log)
    return

def outer(grid, starts, end):
    out = list()
    for start in starts:
        o = inner(grid, start, end)
        if o:
            out.append(o)
    return min(out)

# filename = "small.txt"
filename = "input.txt"
print(outer(*process(filename, False))) #425
print(outer(*process(filename, True))) #418