#!/usr/bin/env python3
import re
from scipy import stats
import sys
import multiprocessing as mp
import time
###gobal variables
seq_id = []
protein_search=[]
seq=[]
query=[]
inp=sys.argv[1]
opt=sys.argv[2]
new_list=[]
output=open(opt,'w+')
#tup=()
#sequ_id=0
#e_value=0
###
#def query_exacator(q,line):
#    query=[]
#    querier= re.match("^Query=.*prot.+?[\s|_][0-9]*",line) 
#    if querier:
#        query.append(querier.group())
#    q.put(query)
def main():
    new_query=''
    new_seq_id=''
    tup=()
    e_val = []
    seq_val={}
    with open(inp, 'r') as data:
       for inc in data:
           line= inc.rstrip('\n')
           line= line.lstrip()
           querier= re.match("^Query=.*prot.+?[\s|_][0-9]*",line) 
           if querier:
               new_query=querier.group()
               query.append(querier.group())
           all_seq_id= re.search('^[K,N,D,J,H,G,M,A,F,L][A-Z].*?_prot_.*?\d+',line)
           if all_seq_id:
               new_seq_id=all_seq_id.group()
               seq_id.append(all_seq_id.group())
           e_val0= re.match('0.0*',line)
           e_valgt10 =  re.search('[0-9]e-[1-9]+[0-9]*',line)
           if e_valgt10:
               new_eval=float(e_valgt10.group())
               e_val.append(new_eval)
               tup=(new_seq_id,new_eval)
           elif e_val0:
               neo_eval=float(e_val0.group())
               e_val.append(neo_eval)
               tub = (new_seq_id,neo_eval)
               #print(tup)
               seq_val[new_query]=tup
               #print(seq_val[new_query]) 
               output.write(printing_results(seq_val))


def add_seq_id(self,q,data):
    for inc in data:
        line= inc.rstrip('\n')
        line= line.lstrip()
        all_seq_id=re.search('^[K,N,D,J,H,G,M,A,F,L][A-Z].*?prot.*?_.*?\d+',line)
        if all_seq_id:
            seq_id.append(all_seq_id.group())
    return seq_id

def creating_tups(s,e):
    tups=()
    for increment  in range(0,len(s)):
        for incrementator in range(0,len(e)):
            tups=(s[incremnt],e[incrementator])
    return tups
def printing_results(s_v):
    for key,value in s_v.items():
        return ("%s : %s " % (key, value))

main()

output.close()
#for new_queries in new_query:
#    newest_list.append(new_queries)
#    end3=time.time()
#
#print("%s \n\n" % newest_list)

#print("%s" % new_list)
#end0=end4-start
#finish_time=end2-start1
#finish=end3-start
#print("%f" % (end0))
#print("%f" % (finish))
#print("%f" % (finish_time))
#for sequence_id in seq_idd:
#for key, value in seq_val.items():
#    output.write("%ds \n #ds " %( key,value))
#output.close()
#for queries in query:
#    for sequence_id in seq_id:
#        for e_values in range(0,len(e_val)):
#            if sequence_id not in new_list:
#                new_list.append((sequence_id,e_val[e_values]))
#                seq_val[queries] = frozenset(new_list)
            #print("seq_val = %s : seq_val[queries] = %s " % (seq_val,str(seq_val[queries])))

#            else:)

                
                #print(i + '\n' + str(inc) +  str(seq_id[inc]) + ' : ' + str(e_val[incr]) + '\n'  )


#f =open[(opt,"w+")
#for key,increment in seq_val.items():
#    print('query :  %s' % key)
#    print('hugemouns list : %s ' % str(increment))
#    f.write("queries  %s : %s \n" % (key, str(increment))
#f.close()
#if __name__ == '__main__':
#    continue
 #          if __name__ == '__main__':
 #              ctx=mp.get_context('spawn')
 #              q=ctx.Queue()
 #              p=ctx.Process(target=query_exacator(q,line))
 #              p.start()
 #              print(q.get())
 #              p.join()
