#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:25:53 2023

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
for gb_file in inputx:    
    for gb_record in SeqIO.parse(open(gb_file,"r"),"genbank"):
        fs = gb_record.features
        for feature in fs:
            if feature.type=="CDS":
                start = feature.location.start.numerator
                end = feature.location.end.numerator
                strand = feature.location.strand
                if strand == 1:
                    seq = gb_record.seq[start:end].translate(table=11)
                elif strand == -1:
                    seq = gb_record.seq[start:end].reverse_complement().translate(table=11)
                feature.qualifiers['translation'] = seq
                SeqIO.write(gb_record,gb_file,"genbank")