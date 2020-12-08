import sys

P = [l.rstrip() for l in sys.stdin]

def main(P, part1=False):
    ip = 0
    acc = 0
    seen = set()
    while ip < len(P) and ip not in seen:
        seen.add(ip)
        op, n = P[ip].split()
        n = int(n)
        if op == 'acc':
            acc += n
        elif op == 'jmp':
            ip += n-1
        elif op == 'nop':
            pass
        ip += 1
    if ip == len(P):
        return acc
    if part1:
        return acc

print(main(P, True))

for i in range(len(P)):
    newP = P.copy()
    if newP[i].startswith('jmp'):
        newP[i] = newP[i].replace('jmp', 'nop')
    elif newP[i].startswith('nop'):
        newP[i] = newP[i].replace('nop', 'jmp')
    else:
        continue
    x = main(newP)
    if x:
        print(x)
