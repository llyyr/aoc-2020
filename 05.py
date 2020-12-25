inp = {int(l.translate({66:49,70:48,76:48,82:49}), 2) for l in open(0)}
print(max(inp))
print(max({*range(max(inp))}-inp))
