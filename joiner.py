#!/usr/bin/env python


FILENAME_JOIN = 'out_joined.csv'

# it is only ~40 items, can just store them in memory
fixed_codes, fixed_lines = [], {}
for line in open('out_compex.txt','rb'):
    if not 'Not found' in line:
        code = line.split(',')[0]
        fixed_codes.append(code)
        fixed_lines[code] = line

with open(FILENAME_JOIN,'wb') as file_join:
    for line in open('out.csv','rb'):
        newline = line
        if 'Not found' in line:
            code = line.split(',')[0]
            if  code in fixed_codes:
                print 'Fixed code: %s' % code
                newline = fixed_lines[code]
        file_join.write(newline)









