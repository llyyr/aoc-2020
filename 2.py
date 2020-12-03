part1 = part2 = 0

for line in open('2.in'):
    X, Y, Z = line.split(); Y = Y[0]
    A, B = map(int, X.split('-'))
    if Z.count(Y) in range(A, B + 1):
        part1 += 1
    if [Z[A - 1], Z[B - 1]].count(Y) == 1:
        part2 += 1

print(part1, part2)