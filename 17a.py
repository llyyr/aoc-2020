inp = [k.rstrip() for k in open(0)]
act = set()

for x, line in enumerate(inp):
    for y, c in enumerate(line):
        if c == '#':
            act.add((x, y, 0))

def neighbors(x, y, z):
    for xx in range(-1, 2):
        for yy in range(-1, 2):
            for zz in range(-1, 2):
                if xx == yy == zz == 0:
                    continue
                yield (xx + x, yy + y, zz + z)

def update():
    r = []
    for i in range(3):
        r.append(range(min(k[i] for k in act)-1, max(k[i] for k in act)+2))
    newact = set()
    xr,yr,zr = r
    for x in xr:
        for y in yr:
            for z in zr:
                nbr=0
                for pos in neighbors(x,y,z):
                    if pos in act:
                        nbr+=1
                if (x,y,z) in act and nbr in [2,3]:
                    newact.add((x,y,z))
                elif (x,y,z) not in act and nbr==3:
                    newact.add((x,y,z))
    return newact

for i in range(6):
    act = update()
    print(len(act))

