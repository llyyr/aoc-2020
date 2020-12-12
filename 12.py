inp = [(k[0], int(k[1:])) for k in open(0)]

x, y = 0, 0
cur = 'E'
dirs = 'E S W N'.split()

for c, n in inp:
    if c == 'N':
        y += n
    elif c == 'S':
        y -= n
    elif c == 'E':
        x += n
    elif c == 'W':
        x -= n
    elif c == 'L':
        cur = dirs[(dirs.index(cur) + n//90)%4]
    elif c == 'R':
        cur = dirs[(dirs.index(cur) - n//90)%4]
    elif c == 'F':
        if cur == 'E':
            x += n
        if cur == 'W':
            x -=n
        if cur == 'N':
            y +=n
        if cur == 'S':
            y -= n

print(abs(x)+abs(y))

x, y = 0, 0
wx, wy = 10, 1

for c, n in inp:
    if c == 'N':
        wy += n
    elif c == 'S':
        wy -= n
    elif c == 'E':
        wx += n
    elif c == 'W':
        wx -= n
    elif c == 'L':
        while n:
            wx, wy = -wy, wx
            n -= 90
    elif c == 'R':
        while n:
            wx, wy = wy, -wx
            n -= 90
    elif c == 'F':
        x += n*wx
        y += n*wy

print(abs(x)+abs(y))
