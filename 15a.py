inp = [1,17,0,10,18,11,6]
i = {n:t for t, n in enumerate(inp)}
n = 0
for t in range(len(i), 30000000-1):
    x = t - i.get(n,t)
    i[n] = t
    n = x
    if t == 2020-2:
        print(n)
print(n)
