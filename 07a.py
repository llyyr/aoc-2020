import sys
from collections import deque, defaultdict
from functools import cache

hosts = defaultdict(list)
contents = defaultdict(list)
X = 'shiny gold'

for line in sys.stdin:
    host, content = line.split(' bags contain ')
    if 'no other bags' in content:
        continue
    for x in content.split(', '):
        cn, b1, b2, *_ = x.split()
        hosts[b1+' '+b2].append(host)
        contents[host].append((int(cn), b1+' '+b2))

seen = set()
Q = deque([X])
while Q:
    node = Q.popleft()
    if node in seen:
        continue
    seen.add(node)
    for y in hosts[node]:
        Q.append(y)
print(len(seen)-1)

@cache
def count(bag):
    cn = 1
    for n, y in contents[bag]:
        cn += n*count(y)
    return cn
print(count(X)-1)
