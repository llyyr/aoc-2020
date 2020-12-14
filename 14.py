from itertools import product

inp = [k.rstrip() for k in open(0)]

def domask(val, mask, X):
    mask = list(mask)
    val = list(format(val, 'b').zfill(36))
    for i in range(36):
        if mask[i] != X:
            val[i] = mask[i]
    val = ''.join(val)
    if 'X' in val:
        x = product((0, 1), repeat=val.count('X'))
        return [int(val.replace('X', '{}').format(*y), 2) for y in x]
    else:
        return int(val, 2)

def solve(inp, p1):
    mem = {}
    mask = None
    for l in inp:
        if l.startswith('mask'):
            mask = l.split(' = ')[1]
        else:
            addr, val = l[4:].replace(']', '').split(' = ')
            addr, val = int(addr), int(val)
            if p1:
                mem[addr] = domask(val, mask, 'X')
            else:
                for addr in domask(addr, mask, '0'):
                    mem[addr] = val
    return sum(mem.values())

print(solve(inp, True))
print(solve(inp, False))
