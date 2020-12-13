inp = [k.strip() for k in open(0)]

def part1(inp):
    time = earliest = int(inp[0])
    busses = [int(k) if k != 'x' else k for k in inp[1].split(',')]

    while True:
        for bus in busses:
            if bus == 'x':
                continue
            if time % bus == 0:
                ans = (time - earliest) * bus
                return ans
        time += 1


def part2(inp):
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 0
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    def crt(a, b, m, n):
        return ((a * n * mul_inv(n, m)) + (b * m * mul_inv(m, n))) % (m * n)

    a, m = 0, 1
    for i, bus in enumerate(inp[1].split(",")):
        if bus == "x":
            continue
        bus = int(bus)
        a = crt(a, bus-i, m, bus)
        m *= bus
    return a


print(part1(inp))
print(part2(inp))
