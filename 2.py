inp = list(map(str, open('2.in').readlines()))

part1 = 0
part2 = 0

for line in inp:
    count, letter, pwd = line.split(' ')
    countmin, countmax = count.split('-')
    countmin, countmax = int(countmin), int(countmax)
    letter = letter.strip(':')
    if pwd.count(letter) in range(countmin,countmax+ 1):
        part1+=1
    if (pwd[countmin-1] == letter)^(pwd[countmax-1] == letter):
        part2+=1
print(part1, part2)

