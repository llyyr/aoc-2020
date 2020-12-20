inp = open(0).read().split('\n\n')
MONSTER = """                  #
#    ##    ##    ###
 #  #  #  #  #  #
"""

tiles = {}
for tile in inp:
    if tile:
        cur = tile.splitlines()
        num = int(cur[0][-5:-1])
        tiles[num] = cur[1:]

mxy = []
for y, l in enumerate(MONSTER.splitlines()):
    for x, c in enumerate(l):
        if c == '#':
            mxy.append((x,y))

orient = {}
for num, tile in tiles.items():
    for j in range(8):
        orient[(num,j)] = tile
        tile = list(reversed(tile)) if j%2==0 else [''.join(c) for c in zip(*tile)]

mw, mh = max(x for x,y in mxy)+1, max(y for x,y in mxy)+1
k = int(len(tiles)**0.5)

def solve(X=[]):
    if len(X)==k**2:
        img = []
        for i in range(k):
            l = [[r[1:-1] for r in tile[1:-1]] for tile in [orient[p] for p in X[i*k:(i+1)*k]]]
            for rs in zip(*l):
                img.append(''.join(rs))
        all_mxy = set()
        for r in range(len(img)-mh):
            for c in range(len(img[0])-mw):
                if all(img[r+y][c+x]=='#' for x,y in mxy):
                    all_mxy.update((c+x,r+y) for x,y in mxy)
        if all_mxy:
            print(X[0][0]*X[k-1][0]*X[k*(k-1)][0]*X[k**2-1][0])
            print(sum(int(c=='#') for c in ''.join(img))-len(all_mxy))
            exit()

    r,c = len(X)//k, len(X)%k
    for num in tiles.keys():
        if num in [i for i,j in X]:
            continue
        for j in range(8):
            if r>0 and orient[X[len(X)-k]][-1] != orient[(num,j)][0]:
                continue
            elif c>0 and not all(p[-1] == q[0] for p,q in zip(orient[X[-1]],orient[(num,j)])):
                continue
            Y = X.copy()
            Y.append((num,j))
            solve(Y)
solve()
