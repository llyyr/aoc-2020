grid = list(map(str, (l.rstrip() for l in open(0))))
L, W = len(grid), len(grid[0])

def main(dx, dy):
    seen = posx = 0
    for i in range(0, L, dy):
        seen += grid[i][posx] == '#'
        posx = (posx + dx) % W
    return seen

print(main(3, 1))
print(main(1, 1) * main(3, 1) * main(5, 1) * main(7, 1) * main(1, 2))

