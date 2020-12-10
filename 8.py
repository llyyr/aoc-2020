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
        ip += 1
    if ip == len(P) or part1:
        return acc

print(main(P, True))
for i in range(len(P)):
    if P[i].startswith('j'):
        P[i] = P[i].replace('jmp', 'nop')
        x = main(P)
        P[i] = P[i].replace('nop', 'jmp')
    elif P[i].startswith('n'):
        P[i] = P[i].replace('nop', 'jmp')
        x = main(P)
        P[i] = P[i].replace('jmp', 'nop')
    else:
        continue
    if x:
        print(x)
