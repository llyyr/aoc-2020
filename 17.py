from itertools import product

inp = [k.rstrip() for k in open(0)]
act = set()

for x,l in enumerate(inp):
    for y,c in enumerate(l):
        if c=='#':
            act.add((x,y,0,0))

def findn(x,y,z,w):
    for xx, yy, zz, ww in product([-1,0,1], repeat=4):
        if not xx==yy==zz==ww==0:
            yield (xx+x, yy+y, zz+z, ww+w)

def findr(i, act):
    return range(min(k[i] for k in act)-1, max(k[i] for k in act)+2)

def update(p1, times=6, act=act):
    for i in range(times):
        newact = set()
        for x in findr(0, act):
            for y in findr(1, act):
                for z in findr(2, act):
                    for w in ([0] if p1 else findr(3, act)):
                        n=0
                        for pos in findn(x,y,z,w):
                            if pos in act:
                                n+=1
                        if (x,y,z,w) in act and n in [2,3]:
                            newact.add((x,y,z,w))
                        elif (x,y,z,w) not in act and n==3:
                            newact.add((x,y,z,w))
        act = newact
    return len(act)

print(update(True))
print(update(False))
