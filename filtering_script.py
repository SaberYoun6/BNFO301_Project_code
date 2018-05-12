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
            e_val.append(line)
            print(type(line))
            print(type(e_val))
            print(e_val)
            print(line)
            print(line)
                
