#!/usr/bin/env python
import re
from scipy import stats
import sys
import pprint
seq_id = []
e_val = []
protein_search=[]
seq=[]
inp=sys.argv[1]
query=[]
seq_val={}
with open(inp, 'r') as data:
    for inc in data:
        line= inc.rstrip('\n')
        line= line.lstrip()
        if line.startswith('Query= lcl'):
            query.append(line)
        GU0 = re.match('GU071[0-9]*.1_prot_ADO9[0-9][0-9]*.1.1',line)
        KJ_or_Y= re.match('K[A-Z]0190[0-9]*.1_prot_A[A-Z][A-X][0-9*.1_[1-4]*',line)
        NC_0= re.match("NC_0[0-4][0-9]*.1_prot_YP_[0-9]*.1_[0-9]*",line)
        J_N_or_F=re.match('J[B-P][0-9]7[0-9][0-9]*.1_prot_AF[A-F[0-9]*.1_[0-4]*',line)
        D_or_HQ= re.match("[D-H]Q[1-9]*.[0-4]_prot_A[A-P][C-Z][0-9*.[0-9]*",line)
        if GU0:
            seq_id.append(GU0.group())  
        elif (KJ_or_Y):
            seq_id.append(KJ_or_Y.group())
        elif (NC_0):
            seq_id.append(NC_0.group())
        elif (J_N_or_F):
            seq_id.append(J_N_or_F.group())
        elif (line.startswith('MH10')):
            seq_id.append(line)
        elif (D_or_HQ):
            seq_id.append(D_or_HQ.group())
        newline= re.search('0.0[0-4][0-9]*',line)
        neoin = re.search('[0-9]e-[0-9][0-9]*',line)
        if neoin:
            neoin=float(neoin.group())
            e_val.append(neoin)
        elif newline:
            newline=float(newline.group())
            e_val.append(newline)
        else: 
            seq.append(line)




print(query)
print((str(seq_id) + ':' + str(e_val)))


