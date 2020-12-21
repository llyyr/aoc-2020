cn = {}
can = {}
MAP = {}

for line in open(0):
    line = line.rstrip()
    Is, As = line[:-1].split(" (contains ")
    Is = Is.split()
    As = As.split(", ")
    for I in Is:
        cn[I] = 1 if I not in cn else cn[I] + 1
    for A in As:
        if A in can:
            can[A] &= set(Is)
        else:
            can[A] = set(Is)

while can:
    A, Is = min(can.items(), key=lambda k: len(k[1]))
    MAP[A] = Is.pop()
    for I in can.values():
        I -= {MAP[A]}
    del can[A]

print(sum(cn[i] for i in cn if i not in MAP.values()))
print(",".join([I for _, I in sorted(MAP.items())]))
