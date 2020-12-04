passports = open('4.in').read().split('\n\n')

def main(part2=False):
    total = 0
    for each in passports:
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = True
        for fields in each.split():
            if fields.startswith('byr'):
                byr = True
                if part2 and len(fields[4:]) == 4:
                    if int(fields[4:]) not in range(1920, 2002+1):
                        byr = False
            if fields.startswith('iyr'):
                iyr = True
                if part2 and len(fields[4:]) == 4:
                    if int(fields[4:]) not in range(2010, 2020+1):
                        iyr = False
            if fields.startswith('eyr'):
                eyr = True
                if part2 and len(fields[4:]) == 4:
                    if int(fields[4:]) not in range(2020, 2030+1):
                        eyr = False
            if fields.startswith('hgt'):
                hgt = True
                if part2 and fields[-2:] not in ['cm', 'in']:
                    hgt = False
                if part2 and fields[-2:] == 'in':
                    if int(fields[4:-2]) not in range(59, 76+1):
                        hgt = False
                if part2 and fields[-2:] == 'cm':
                    if int(fields[4:-2]) not in range(150, 193+1):
                        hgt = False
            if fields.startswith('hcl'):
                hcl = True
                if part2 and fields[4:5] != '#' and len(fields[4:]) != 7: #fields[4:].startswith('#'):
                    hcl = False
            if fields.startswith('ecl'):
                ecl = True
                if part2 and fields[4:] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    ecl = False
            if fields.startswith('pid'):
                pid = True
                if part2 and len(fields[4:]) != 9:
                    pid = False
            if fields.startswith('cid'):
                if len(fields[4:]) >= 2:
                    cid = True
        if byr and iyr and eyr and hgt and hcl and ecl and pid and cid:
            total+=1
    return total

print(main())
print(main(True))
