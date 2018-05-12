#!/usr/bin/env python
import re
from scipy import stats
import sys
seq_id = []
e_val = []
protein_search=[]
seq=[]
inp=sys.argv[1]

with open(inp, 'r') as data:
    for inc in data:
        line= inc.rstrip('\n')
        line= line.lstrip()
        if (line.startswith('>')):
            seq_id.append(line)  
        elif (re.search('0.0[0-4][0-9]*',line)):
            neoin = re.search('[0-9]e-[0-9]*',line)
            #neoin = re.match('[0-9]e-[0-9]*',line)
            print(neoin)
            print(type(neoin))
            e_val.append(neoin)
            #print(type(line))
            print(type(e_val))
            print(e_val)
           #print(line)
