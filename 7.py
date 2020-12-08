import sys
from functools import cache

inp = [l.rstrip() for l in sys.stdin]
bags = []
X = 'shiny gold'

@cache
def part1(bag, bags=bags):
    for line in inp:
        i = line.split(' bags contain ')
        j = i[1].split(', ')
        if bag in i[1] and i[0] not in bags:
            bags += [i[0]]
            part1(i[0])
    return len(bags)

@cache
def part2(bag):
    for line in inp:
        i = line.split(' contain ')
        j = i[1].split(', ')
        if bag in i[0]:
            if 'no other bag' in line:
                return 0
            bn = [str(k[2:].strip('.')) for k in j]
            cn = [int(k[0]) for k in j]
            return sum(cn+part2(bn)*cn for bn, cn in zip(bn, cn))

print(part1(X), part2(X))

