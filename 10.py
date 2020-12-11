from functools import cache
from collections import defaultdict

inp = sorted([int(k) for k in open(0)])
target = inp[-1] + 3
inp += [target]

one = 0
three = 0

for i in range(len(inp)):
    if i == 0:
        last = 0
    else:
        last = inp[i-1]
    if inp[i] - last == 1:
        one += 1
    elif inp[i] - last == 3:
        three += 1

print(one*three)

dp = {}
@cache
def f(i):
    if i == target:
        return 1
    elif i in dp:
        return dp[i]
    else:
        x = 0
        if i+1 in inp:
            x += f(i+1)
        if i+2 in inp:
            x += f(i+2)
        if i+3 in inp:
            x += f(i+3)
        dp[i] = x
        return dp[i]

#print(f(0))

# >>79132891
dp = defaultdict(int)
dp[0] = 1
for x in inp:
    dp[x] += dp[x-1] + dp[x-2] + dp[x-3]
print(dp[target])

