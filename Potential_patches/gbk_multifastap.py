#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:01:15 2022

@author: joaquin
"""

from Bio import SeqIO

inputx = ["Contannotate_pVA04-6.gbk","Contannotate_pVA04-46.gbk",\
           "Contannotate_pVA04-58.gbk","Contannotate_pVA04-196.gbk",\
           "Contannotate_pVA126-12.gbk","Contannotate_pVA126-42.gbk",\
           "Contannotate_pVA126-68.gbk","Contannotate_pVA126-175.gbk",\
           "Contannotate_pVA126-339.gbk","Contannotate_pVA172-67.gbk",\
           "Contannotate_pVA172-90.gbk","Contannotate_pVA32-7.gbk",\
           "Contannotate_pVA32-58.gbk","Contannotate_pVA32-74.gbk",\
           "Contannotate_pVA32-104.gbk","Contannotate_pVA32-200.gbk",\
           "Contannotate_pVA564-33.gbk","Contannotate_pVA564-37.gbk",\
           "Contannotate_pVA564-63.gbk","Contannotate_pVA564-179.gbk",\
           "Contannotate_pVA569-6.gbk","Contannotate_pVA569-7.gbk",\
           "Contannotate_pVA569-35.gbk","Contannotate_pVA569-78.gbk",\
           "Contannotate_pVA591-7.gbk","Contannotate_pVA591-9.gbk",\
           "Contannotate_pVA591-46.gbk","Contannotate_pVA591-160.gbk",\
           "Contannotate_pVA681-5.gbk","Contannotate_pVA681-14.gbk",\
           "Contannotate_pVA681-36.gbk","Contannotate_pVA681-58.gbk",\
            "Contannotate_pVA681-191.gbk","Contannotate_pVA684-2.gbk",\
            "Contannotate_pVA684-6.gbk","Contannotate_pVA684-8.gbk",\
            "Contannotate_pVA684-49.gbk","Contannotate_pVA684-146.gbk",\
            "Contannotate_pVA684-388.gbk","Contannotate_pVA833-7.gbk",\
            "Contannotate_pVA833-92.gbk","Contannotate_pVA833-165.gbk",\
            "Contannotate_pVA833-176.gbk"]
#Aca va el recuperador#
feature_data_bank=[] 
for gb_file in inputx:    
    for gb_record in SeqIO.parse(open(gb_file,"r"),"genbank"):
        fs = gb_record.features
        for feature in fs:
            local_feature_stat = []
            name = ''
            start = 0
            end = 0
            seq = ''
            if feature.type=="CDS":
                plasmid = gb_record.name
                name = feature.qualifiers['product']
                start = feature.location.start.numerator
                end = feature.location.end.numerator
                strand = feature.location.strand
                if strand == 1:
                    seq = gb_record.seq[start:end].translate(table=11)
                elif strand == -1:
                    seq = gb_record.seq[start:end].reverse_complement().translate(table=11)
                start = start + 1
                local_feature_stat=(plasmid,name,start,end,str(seq))
            else:
                continue
            feature_data_bank.append(local_feature_stat)

#Aca printeamos los datos en un texto plano#            
with open("multifastp.fa","a") as multifastap:
    protein_fasta_list = []
    for index,value in enumerate(feature_data_bank):
        protein_fasta = ""
        header = ">"
        plasmid = value[0]
        connector = "_"
        start = value[2]
        end = value[3]
        jump  = "\n"
        seq = value[4]
        protein_fasta = header + plasmid + connector + str(start) + connector + str(end) + jump + seq + jump
        protein_fasta_list.append(protein_fasta)
        multifastap.write(protein_fasta)  
                    
with open("multifastp.fa","w") as ahorasi:
    pfls = protein_fasta_list
    ndpfl = []
    for x in pfls:
        if x not in ndpfl:
            ndpfl.append(x)
        else:
            continue
    for y in ndpfl:
        ahorasi.write(y)