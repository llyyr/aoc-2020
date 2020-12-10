# https://boards.4channel.org/g/thread/79116396#p79116435
from collections import deque

l = list(map(int, open(0)))
pre = 25
p1 = 0
X = 0

p = deque(l[:pre], 25)
for i in l[pre:]:
    for j in p:
        if i-j in p:
            if i!=j*2 or p.count(j)!=1:
                break
    else:
        print(p1 := i)
        break
    p.append(i)

q = deque()
for i in l:
    X += i
    q.append(i)
    while X > p1:
        X -= q.popleft()
    if X == p1 and len(q) > 1:
        print(min(q) + max(q))
        break

