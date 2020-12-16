from collections import defaultdict

inp = [k.rstrip() for k in open(0)]
ans = 0
nums = set()
nearby = False
other = defaultdict(set)
fields = [set()] * 20

for l in inp:
    if l == 'nearby tickets:':
        nearby = True
        continue
    for args in l.split():
        if '-' in args:
            x, y = map(int, args.split('-'))
            k = l.split(':')[0]
            for i in range(x,y+1):
                nums.add(i)
                other[k].add(i)
            for i in range(20):
                fields[i].add(k)
    if nearby:
        for i in map(int, l.split(',')):
            if i not in nums:
                ans+=i #part1
        x = [int(l) for l in l.split(',')]
        valid=True
        for i in x:
            if i not in nums:
                valid=False
                break
        if not valid:
            continue
        for i in range(20):
            MAP = set()
            for k in other:
                if x[i] in other[k]:
                    MAP.add(k)
            fields[i] = fields[i] & MAP
    elif len(l.split(',')) == 20:
        mine = [int(l) for l in l.split(',')]

print(ans)

ans = 1
MAP = set()
x = {}

for _ in range(20):
    for i in range(20):
        fields[i] -= MAP
        if len(fields[i]) == 1:
            for k in fields[i]:
                x[k] = i
                MAP.add(k)
            break

for y in x:
    ans *= mine[x[y]] if 'dep' in y else 1

print(ans)
