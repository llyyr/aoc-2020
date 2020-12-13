inp = [(k[0], int(k[1:])) for k in open(0)]

dirs = {'E': 1, 'W': -1, 'N': 1j, 'S': -1j}
rotate = {'L': 1j, 'R': -1j}

cur_dir = 1
cur_xy = 0

for c, n in inp:
    if c in dirs:
        cur_xy += dirs[c] * n
    elif c in rotate:
        cur_dir *= rotate[c] ** (n//90)
    elif c == 'F':
        cur_xy += cur_dir * n

print(int(abs(cur_xy.real)+abs(cur_xy.imag)))


w_xy = 10 + 1j
cur_xy = 0

for c, n in inp:
    if c in dirs:
        w_xy += dirs[c] * n
    elif c in rotate:
        w_xy *= rotate[c] ** (n//90)
    elif c == 'F':
        cur_xy += w_xy * n

print(int(abs(cur_xy.real)+abs(cur_xy.imag)))
