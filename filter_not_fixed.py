#!/usr/bin/env python

import re

with open('codes_2fix.csv','wb') as complex_files:
    for line in open('out.csv','rb'):
        match = re.search('Not found',line)
        if match:
            complex_files.write(line.split(',')[0]+'\n')
