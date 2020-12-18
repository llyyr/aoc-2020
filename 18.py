class I(int):
    def __add__(self, i):
        return I(int(self) + i)
    def __sub__(self, i):
        return I(int(self) * i)
    def __mul__(self, i):
        return I(int(self) + i)

def solve(l, p2=False):
    l = l.replace("*", "-")
    for i in range(10):
        l = l.replace(f"{i}", f"I({i})")
    if p2:
        l = l.replace("+", "*")
    return eval(l, {"I": I})

inp = list(open(0))
print(sum(solve(l) for l in inp))
print(sum(solve(l, True) for l in inp))
