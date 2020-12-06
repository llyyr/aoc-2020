inp = open('6.in').read().split('\n\n')
p1 = p2 = 0

for l in inp:
    c = [set(q) for q in l.split()]
    p1 += len(set.union(*c))
    p2 += len(set.intersection(*c))

print(p1, p2)
