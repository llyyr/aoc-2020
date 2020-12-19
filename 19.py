from functools import cache

rs, msgs = open(0).read().split('\n\n')
rs = {r.split(': ')[0]: r.split(': ')[1]  for r in rs.split('\n')}
msgs = msgs.split('\n')

@cache
def solve(msg, r):
    if r == '"a"':
        return msg == "a"
    elif r == '"b"':
        return msg == "b"
    elif ' | ' in r:
        r1, r2 = r.split(' | ')
        return solve(msg, r1) or solve(msg, r2)
    elif ' ' in r:
        r1, r2 = r.split(None, 1)
        for i in range(1, len(msg)):
            if solve(msg[0:i], r1) and solve(msg[i:], r2):
                return True
        else:
            return False
    else:
        return solve(msg, rs[r])

print(sum(1 for msg in msgs if solve(msg, rs['0'])))
solve.cache_clear()
rs['8'] = '42 | 42 8'
rs['11'] = '42 31 | 42 11 31'
print(sum(1 for msg in msgs if solve(msg, rs['0'])))
