inp = list(map(int, open('1.in').readlines()))

for i in inp:
    for j in inp:
        for k in inp:
            if i+j+k == 2020:
                print(i*j*k)
        if i+j == 2020:
            print(i*j)

