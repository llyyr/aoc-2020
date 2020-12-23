inp = '394618527'

def p1(c):
    c = list(map(int, c))
    l = len(c)
    for _ in range(100):
        Xs = [c.pop(1), c.pop(1), c.pop(1)]
        d = c[0]-1 or l
        while d in Xs:
            d = d-1 or l
        for i in Xs[::-1]:
            c.insert(c.index(d)+1, i)
        c.append(c.pop(0))
    c = c[c.index(1)+1:] + c[:c.index(1)]
    return ''.join(str(i) for i in c)

def p2(c):
    c = list(map(int, c))
    l = int(1e6)
    LL = [0] * (l+1)
    for i in range(len(c)-1):
        LL[c[i]] = c[i+1]
    prev = c[-1]
    for i in range(10, l+1):
        LL[prev] = i
        prev = i
    LL[l] = c[0]
    cur = c[0]
    for _ in range(int(1e7)):
        Xs = [LL[cur]]
        while len(Xs) < 3:
            Xs.append(LL[Xs[-1]])
        LL[cur] = LL[Xs[-1]]
        d = cur-1 or l
        while d in Xs:
            d = d-1 or l
        LL[Xs[-1]] = LL[d]
        LL[d] = Xs[0]
        cur = LL[cur]
    return LL[1] * LL[LL[1]]

print(p1(inp))
print(p2(inp))
