inp = open('6.in').read().split('\n\n')
p1 = p2 = 0
for l in inp:
    c = [set(q) for q in l.split()]
    p1 += len(set.union(*c))
    p2 += len(set.intersection(*c))

print(p1, p2)

print(*map(sum, zip(*(map(len, [set.union(*c), set.intersection(*c)]) for c in ([*map(set, i.split())] for i in open('6.in').read().split('\n\n'))))))
