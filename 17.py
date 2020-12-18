from itertools import product

act = set()
for x, l in enumerate(k.rstrip() for k in open(0)):
    for y, c in enumerate(l):
        if c == '#':
            act.add((x,y,0,0))

def findn(x, y, z, w):
    for xx, yy, zz, ww in product([-1,0,1], repeat=4):
        if not xx==yy==zz==ww==0:
            yield (xx+x, yy+y, zz+z, ww+w)

def findr(i, act):
    return range(min(k[i] for k in act)-1, max(k[i] for k in act)+2)

def update(p1, t=6, act=act):
    for i in range(t):
        newact = set()
        for x in findr(0, act):
            for y in findr(1, act):
                for z in findr(2, act):
                    for w in ([0] if p1 else findr(3, act)):
                        pos = (x,y,z,w)
                        n=0
                        for k in findn(*pos):
                            if k in act:
                                n+=1
                        if pos in act and 2<=n<=3:
                            newact.add(pos)
                        elif pos not in act and n==3:
                            newact.add(pos)
        act = newact
    return len(act)

print(update(True))
print(update(False))
