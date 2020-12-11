from itertools import product
import ujson

inp = [list(l.rstrip()) for l in open(0)]
C = len(inp[0])
R = len(inp)


def cn_occ(x, y, l, p2):
    cn = 0
    for dx, dy in product([-1,0,1], repeat=2):
        if dx == 0 and dy == 0:
            continue
        cur_x = x + dx
        cur_y = y + dy
        while p2 and 0<=cur_x<R and 0<=cur_y<C and l[cur_x][cur_y] == '.':
            cur_x += dx
            cur_y += dy
        if 0<=cur_x<R and 0<=cur_y<C and l[cur_x][cur_y] == '#':
            cn += 1
    return cn

def main(l, p2):
    while True:
        new_l = ujson.loads(ujson.dumps(l))
        diff = False
        for x, y in product(range(R), range(C)):
            cn = cn_occ(x, y, l, p2)
            if l[x][y] == 'L' and cn == 0:
                new_l[x][y] = '#'
                diff = True
            elif l[x][y] == '#' and cn >= (5 if p2 else 4):
                new_l[x][y] = 'L'
                diff = True
        if not diff:
            break
        l = new_l.copy()
    return sum(R.count('#') for R in l)

print(main(inp, False))
print(main(inp, True))
