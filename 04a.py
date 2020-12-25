def inrange(x, lower, upper):
    return x.isdigit() and int(lower) <= int(x) <= int(upper)

def byr(x, lower, upper):
    return inrange(x, lower, upper)

def iyr(x, lower, upper):
    return inrange(x, lower, upper)

def eyr(x, lower, upper):
    return inrange(x, lower, upper)

def hgt(x, lower, upper):
    if x.endswith('in'):
        return inrange(x[:-2], lower[0][:-2], upper[0][:-2])
    elif x.endswith('cm'):
        return inrange(x[:-2], lower[1][:-2], upper[1][:-2])
    else:
        return False

def hcl(x):
    return x.startswith('#') and all(l in set('abcdef0123456789') for l in x[1:])

def ecl(x):
    return x in 'amb blu brn gry grn hzl oth'.split()

def pid(x):
    return x.isdigit() and len(x) == 9

def cid(x):
    pass

passports = open(0).read().split('\n\n')
req = 'byr iyr eyr hgt hcl ecl pid'.split()

p1 = p2 = 0

for passport in passports:
    req_fields = dict(zip(req, list(False for each in req)))
    for fields in passport.split():
        name, value = fields.split(':')
        if name == 'byr':
            req_fields[name] = byr(value, 1920, 2002)
        elif name == 'iyr':
            req_fields[name] = iyr(value, 2010, 2020)
        elif name == 'eyr':
            req_fields[name] = eyr(value, 2020, 2030)
        elif name == 'hgt':
            req_fields[name] = hgt(value, ['59in', '150cm'], ['76in', '193cm'])
        elif name == 'hcl':
            req_fields[name] = hcl(value)
        elif name == 'ecl':
            req_fields[name] = ecl(value)
        elif name == 'pid':
            req_fields[name] = pid(value)
        elif name == 'cid':
            pass

    if set(req) <= set(fields[0:3] for fields in passport.split()):
        p1 += 1
    if all(check for check in req_fields.values()):
        p2 += 1

print(p1, p2)

