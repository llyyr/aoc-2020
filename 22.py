inp = open(0).read().split('\n\n')
d1 = list(map(int, inp[0].split('\n')[1:]))
d2 = list(map(int, inp[1].split('\n')[1:-1]))

def solve(d1, d2, p2=False):
    states = set()
    while d1 and d2:
        state = (tuple(d1), tuple(d2))
        if state in states:
            break
        states.add(state)
        d1c, d2c = d1.pop(0), d2.pop(0)
        if p2 and len(d1) >= d1c and len(d2) >= d2c:
            d1win, _ = solve(d1[:d1c], d2[:d2c])
        else:
            d1win = d1c > d2c
        if d1win:
            d1 += [d1c, d2c]
        else:
            d2 += [d2c, d1c]
    if d1 or d1win:
        return True, sum(c*i for i,c in enumerate(reversed(d1),1))
    elif d2:
        return False, sum(c*i for i,c in enumerate(reversed(d2),1))

_, p1 = solve(d1[:], d2[:])
print(p1)
_, p2 = solve(d1, d2, True)
print(p2)
