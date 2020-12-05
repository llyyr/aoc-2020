inp = open('5.in').read().split()

p1 = 0
seats = []

for line in inp:
    line = line.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    row = int(line[:7], 2)
    column  = int(line[7:], 2)
    p1 = max(p1, row * 8+column)
    seats.append(row * 8+column)

print(p1)


for i in range(max(seats)):
    if i-1 in seats and i+1 in seats and i not in seats:
        print(i)

