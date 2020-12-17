inp = [k.rstrip() for k in open(0)]
act = set()

for x,l in enumerate(inp):
    for y,c in enumerate(l):
        if c=='#':
            act.add((x,y,0,0))

def findn(x,y,z,w):
    for xx in range(-1,2):
        for yy in range(-1,2):
            for zz in range(-1,2):
                for ww in range(-1,2):
                    if xx==yy==zz==ww==0:
                        continue
                    yield (xx+x, yy+y, zz+z, ww+w)

def update():
    newact = set()
    r = []
    for i in range(4):
        r.append(range(min(k[i] for k in act)-1,max(k[i] for k in act)+2))
    xr,yr,zr,wr = r
    for x in xr:
        for y in yr:
            for z in zr:
                for w in wr:
                    n=0
                    for pos in findn(x,y,z,w):
                        if pos in act:
                            n+=1
                    if (x,y,z,w) in act and n in [2,3]:
                        newact.add((x,y,z,w))
                    elif (x,y,z,w) not in act and n==3:
                        newact.add((x,y,z,w))
    return newact

for i in range(6):
    act = update()
    print(len(act))

