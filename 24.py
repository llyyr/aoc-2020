from collections import Counter

inp = [k.rstrip() for k in open(0)]
DIRS = {
    'e': (2,0),
    'w': (-2,0),
    'se': (1,-1),
    'ne': (1,1),
    'sw': (-1,-1),
    'nw': (-1,1)
}

def mapxy(l):
    c,x,y = 0,0,0
    while c < len(l):
        instr = l[c]
        if instr in ['n','s']:
            instr = l[c:c+2]
            c+=2
        else:
            c+=1
        dx,dy = DIRS[instr]
        x+=dx
        y+=dy
    return x,y

cn = Counter(map(mapxy, inp))
ans = {i for i,v in cn.items() if v%2}
print(len(ans))

for _ in range(100):
    cn = Counter(i for x,y in ans for i in [(x+dx, y+dy) for dx,dy in DIRS.values()])
    ans = {i for i,v in cn.items() if v==2 or (v==1 and i in ans)}
print(len(ans))
