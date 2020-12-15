inp = list(map(int, '1,17,0,10,18,11,6'.split(',')))
t = {}
idx = len(inp)+1
num = 0

for i, n in enumerate(inp):
    t[n] = i+1

while True:
    if t.get(num) == None:
        t[num] = idx
        num = 0
    else:
        x = idx-t.get(num)
        t.update({num:idx})
        num = x
    idx+=1
    if idx == 2020:
        print(num)
    elif idx == 30000000:
        print(num)
        break
