import os
import re
import sys
from Bio import SeqIO 
def cons_seq(seq):
  n=len(seq[0])
  best_seqs=[[]]
  profile={'M':[0]*n,'A':[0]*n,'C':[0]*n,'D':[0]*n,'E':[0]*n,'F':[0]*n,'G':[0]*n,'H':[0]*n,'I':[0]*n,'K':[0]*n,'L':[0]*n,'N':[0]*n,'P':[0]*n,'Q':[0]*n,'R':[0]*n,'S':[0]*n,'T':[0]*n,'V':[0]*n,'W':[0]*n,'Y':[0]*n,'X':[0]*n}
  for i in range(n):
    d={N:profile[N][i] for N in ['M','A','C','D','E','F','G','H','I','K','L','N','P','Q','R','S','T','V','W','Y','X']}
    m=max(d.values())
    l =[N for N in ['M','A','C','D','E','F','G','H','I','K','L','N','P','Q','R','S','T','V','W','Y','X'] if d[N] == m]
    best_seqs=[ s+[N] for N in l for s in best_seqs ]
  for s in bestseqs:
    return(''.join(s))
      
def main():
  c,co,cou,cuo,coun,cuon,count,counts,countes,cunots,conuts, totalcount=0,0,0,0,0,0,0,0,0,0,0,0
  f=sys.argv[1]
  fi=sys.argv[2]
  seq_rec52_syn,seq_rec55_syn,seq_rec56_syn,seq_rec57_syn,seq_rec52_phen,seq_rec55_phen,seq_rec56_phen,seq_rec57_phen=[],[],[],[],[],[],[],[]
  for seq_record in SeqIO.parse(f,'fasta'):
    if len(seq_record.seq) >= 50 and len(seq_record.seq)<= 60:
       #print(str(seq_record.seq))
       #print(len(seq_record.seq))
       totalcount+=1
       if   len(seq_record.seq) == 50:
         c+=1 # to keep count of  every instance that is begin called 
  #       print(str(seq_record.id))
  #       print(str(seq_record.seq))
  #       print(len(seq_record.seq)) 
       elif len(seq_record.seq) == 51:
         co+=1 # to keep count of  every instance that is begin called 
 #        print(str(seq_record.id))
#         print(str(seq_record.seq))
 #        print(len(seq_record.seq))
       elif len(seq_record.seq) == 52:
         seq_rec52_syn.append(str(seq_record.seq))
         cou=+1 # to keep count of  every instance that is begin called 
       elif len(seq_record.seq) == 53:
         cuo+=1 # to keep count of  every instance that is begin called 
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       elif len(seq_record.seq) == 54:
         coun+=1 # to keep count of  every instance that is begin called 
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       elif len(seq_record.seq) == 55:
         cuon+=1 # to keestr(seq_record.seq)p count of  every instance that is begin called 
         seq_rec55_syn.append(str(seq_record.seq))
       elif len(seq_record.seq) == 56:
         count+=1 # to keep count of  every instance that is begin calle
         seq_rec56_syn.append(str(seq_record.seq))
       elif len(seq_record.seq) == 57:
         seq_rec57_syn.append(str(seq_record.seq))
         counts+=1 # to keep count of  every instance that is begin called 
       elif len(seq_record.seq) == 58:
#        print(str(seq_record.id))
         countes+=1  # to keep count of  every instance that is begin called 
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       elif len(seq_record.seq) == 59:
         cunots+=1 # to keepp count of all instance that are begin called
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       else:
         conuts+=1 # to keep count of  every instance that is begin called 
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
         
  c1,co1,cou1,cuo1,coun1,cuon1,count1,counts1,countes1,cunots1,conuts1,totalcount1=0,0,0,0,0,0,0,0,0,0,0,0
  for seq_record in SeqIO.parse(fi,'fasta'):
    if len(seq_record.seq) >= 50 and len(seq_record.seq)<= 60:
       #print(str(seq_record.seq))
       #print(len(seq_record.seq))
       totalcount1+=1
       if   len(seq_record.seq) == 50:
         c1+=1 # to keep count of  every instance that is begin called 
  #       print(str(seq_record.id))
  #       print(str(seq_record.seq))
  #       print(len(seq_record.seq)) 
       elif len(seq_record.seq) == 51:
         co1+=1 # to keep count of  every instance that is begin called 
 #        print(str(seq_record.id))
#         print(str(seq_record.seq))
 #        print(len(seq_record.seq))
       elif len(seq_record.seq) == 52:
         cou1=+1 # to keep count of  every instance that is begin called 
         seq_rec52_phen.append(str(seq_record.seq))
       elif len(seq_record.seq) == 53:
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
         cuo1+=1 # to keep count of  every instance that is begin called 
       elif len(seq_record.seq) == 54:
         coun1+=1 # to keep count of  every instance that is begin called 
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       elif len(seq_record.seq) == 55:
         cuon1+=1 # to keep count of  every instance that is begin called 
         seq_rec55_phen.append(str(seq_record.seq))
       elif len(seq_record.seq) == 56:
         count1+=1 # to keep count of  every instance that is begin called 
         seq_rec56_phen.append(str(seq_record.seq))
       elif len(seq_record.seq) == 57:
         counts1+=1 # to keep count of  every instance that is begin called 
         seq_rec57_phen.append(str(seq_record.seq))
       elif len(seq_record.seq) == 58:
#        print(str(seq_record.id))
         countes1+=1  # to keep count of  every instance that is begin called 
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       elif len(seq_record.seq) == 59:
         cunots1+=1 # to keepp count of all instance that are begin called
#        print(str(seq_record.id))
#        print(str(seq_record.seq))
#        print(len(seq_record.seq))
       else:
         conuts1+=1 # to keep count of  every instance that is begin called 
#        print(str(seq_record.id))
#        print(str(seq_record.seq))

  sumofcounts1 = c1+co1+cou1+cuo1+coun1+count1+countes1+cunots1+conuts1
  sumofcount   = c+co+cou+cuo+coun+cuon+count+counts+countes+cunots+conuts
  diffofcounts= totalcount-sumofcount
  diffofcounts1=totalcount1-sumofcounts1

  con_seq_52_pen=cons_seq(seq_rec52_phen)
  print(con_seq_52_pen)



  print ("50 : %i\n51 : %i\n52 : %i\n53 : %i\n54 : %i\n55 : %i\n56 : %i\n57 : %i\n58 : %i\n59 : %i\n60 : %i\n total count : %i sum of all counts : %i differenct of total counts - sum of all counts : %i" %(c1,co1,cou1,cuo1,coun1,cuon1,count1,counts1,countes1,cunots1,conuts1,totalcount1,sumofcounts1,diffofcounts1))
  print ("50 : %i\n51 : %i\n52 : %i\n53 : %i\n54 : %i\n55 : %i\n56 : %i\n57 : %i\n58 : %i\n59 : %i\n60 : %i\n total count : %i sum of all counts : %i differenct of total counts - sum of all counts : %i" %(c,co,cou,cuo,coun,cuon,count,counts,countes,cunots,conuts, totalcount,sumofcount,diffofcounts))
'''
  for k in secondmode:
    for v in secondmode[k]:
      print('%s: %s'%(k,v) )
  for k in average:
     for v in average[k]:
      print('%s : %s' %(k,v) )

  for k in truemode1:
    for v in truemode1[k]:
      print("%s : %s" %(k,v) )
  for k in secondmode1:
    for v in secondmode1[k]:
      print('%s: %s'%(k,v) )
  for k in average1:
     for v in average1[k]:
      print('%s : %s' %(k,v) )
'''
if __name__=='__main__':
  main()
