from itertools import combinations as cb

l = [int(k) for k in open(0)]
a = 0
X = [0]

for i in range(len(l)):
    X += [X[-1] + l[i]]
    p = False
    if i > 25:
        for x in cb(l[i-25:i], 2):
            if sum(x) == l[i]:
                p = True
                break
        if not p:
            a = l[i]

print(a)

for k in X:
    if a+k in X:
        r=l[X.index(k):X.index(a+k)]
        if len(r) > 1:
            print(min(r)+max(r))
            break
