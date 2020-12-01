inp = list(map(int, open('1.in').readlines()))

#original ugly solution
#for i in inp:
#    for j in inp:
#        for k in inp:
#            if i+j+k == 2020:
#                print(i*j*k)
#        if i+j == 2020:
#            print(i*j)

#better or something
from math import prod
from itertools import combinations

def main(i):
    for X in combinations(inp, i):
        if sum(X) == 2020:
            print(prod(X))

main(2)
main(3)
