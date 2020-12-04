def inrange(x, lower, upper):
    return x.isdigit() and int(lower) <= int(x) <= int(upper)

def chk_byr(x, lower, upper):
    return inrange(x, lower, upper)

def chk_iyr(x, lower, upper):
    return inrange(x, lower, upper)

def chk_eyr(x, lower, upper):
    return inrange(x, lower, upper)

def chk_hgt(x, lower, upper):
    if x[-2:] == 'in':
        return inrange(x[:-2], lower[0][:-2], upper[0][:-2])
    elif x[-2:] == 'cm':
        return inrange(x[:-2], lower[1][:-2], upper[1][:-2])
    else:
        return False

def chk_hcl(x):
    return x.startswith('#') and all(l in set('abcdef0123456789') for l in x[1:])

def chk_ecl(x):
    return x in 'amb blu brn gry grn hzl oth'.split()

def chk_pid(x):
    return x.isdigit() and len(x) == 9

def chk_cid(x):
    pass

passports = open('4.in').read().split('\n\n')
req = 'byr iyr eyr hgt hcl ecl pid'.split()

p1 = p2 = 0

for passport in passports:
    req_fields = dict(zip(req, list(False for each in req)))
    for fields in passport.split():
        name, value = fields.split(':')
        if name == 'byr':
            req_fields[name] = chk_byr(value, 1920, 2002)
        elif name == 'iyr':
            req_fields[name] = chk_iyr(value, 2010, 2020)
        elif name == 'eyr':
            req_fields[name] = chk_eyr(value, 2020, 2030)
        elif name == 'hgt':
            req_fields[name] = chk_hgt(value, ['59in', '150cm'], ['76in', '193cm'])
        elif name == 'hcl':
            req_fields[name] = chk_hcl(value)
        elif name == 'ecl':
            req_fields[name] = chk_ecl(value)
        elif name == 'pid':
            req_fields[name] = chk_pid(value)
        elif name == 'cid':
            pass

    if set(req) <= set(fields[0:3] for fields in passport.split()):
        p1 += 1
    if all(check for check in req_fields.values()):
        p2 += 1

print(p1, p2)

