import sys
from Bio import SeqIO

in_file =  sys.argv[1]
filename  = in_file.split('.')[0]
x=1

with open(in_file,'r') as entrada:
    for record in SeqIO.parse(entrada,'fasta'):
        with open("%s_%s.fasta" %(filename,x),'w') as salida:
            SeqIO.write(record,salida,'fasta')
        x = x + 1
