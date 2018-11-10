import sys



header=[]
proteins=[]
hePro={}
flist=[]
w_file= open(sys.argv[1],"w")
with open("final.fasta.txt", "r") as f:
    seqs=''
    for l in f:
        if l.startswith(">"):
           head=l.rstrip("\n")
        else:
           seqs=l.replace('\n','')
        header.append("".join(head))
        proteins.append(''.join(seqs))
for num in range(len(proteins)):
    if proteins[num] not in flist:
        hePro[header[num]]=proteins[num]
        flist.append(proteins[num])



for k,v in hePro.items():    
    print("printing to a file")
    print("%s \n %s" %(k,v))
    w_file.write("%s \n%s \n"%(k,v))
    print("done writing to file")
    

              
