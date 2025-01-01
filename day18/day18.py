with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

dim = len(lines)

for i in range(dim):
    lines[i] = '.' + lines[i] + '.'

dim += 2
lines.insert(0, '.' * dim)
lines.append('.' * dim)

grid = [['.'] * dim for i in range(dim)]
for i in range(dim):
    for j in range(dim):
        grid[i][j] = lines[i][j]

def get_neighbors(i, j):
    return [
        grid[i + 1][j],
        grid[i + 1][j + 1],
        grid[i + 1][j - 1],
        grid[i][j + 1],
        grid[i][j - 1],
        grid[i - 1][j],
        grid[i - 1][j + 1],
        grid[i - 1][j - 1],
    ]

def print_grid(grid):
    print('\n')
    for line in grid:
        print("".join(line))
    print('\n')

for _ in range(100):
    new_grid = [['.'] * dim for _ in range(dim)]

    for i in range(1, dim - 1):
        for j in range(1, dim - 1):
            on = len([n for n in get_neighbors(i, j) if n == '#'])
            if grid[i][j] == '#':
                if on == 2 or on == 3:
                    new_grid[i][j] = '#'
                else:
                    new_grid[i][j] = '.'

            elif grid[i][j] == '.':
                if on == 3:
                    new_grid[i][j] = '#'
                else:
                    new_grid[i][j] = '.'
    grid = new_grid
    print_grid(grid)

answer = 0

for i in range(dim):
    for j in range(dim):
        if grid[i][j] == '#':
            answer += 1

print(answer)