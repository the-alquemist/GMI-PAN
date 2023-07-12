#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 17:17:19 2022

@author: joaquin
"""

entrada = ["Contannotate_pVA04-6.gff","Contannotate_pVA04-46.gff",\
           "Contannotate_pVA04-58.gff","Contannotate_pVA04-196.gff",\
           "Contannotate_pVA126-12.gff","Contannotate_pVA126-42.gff",\
           "Contannotate_pVA126-68.gff","Contannotate_pVA126-175.gff",\
           "Contannotate_pVA126-339.gff","Contannotate_pVA172-67.gff",\
           "Contannotate_pVA172-90.gff","Contannotate_pVA32-7.gff",\
           "Contannotate_pVA32-58.gff","Contannotate_pVA32-74.gff",\
           "Contannotate_pVA32-104.gff","Contannotate_pVA32-200.gff",\
           "Contannotate_pVA564-33.gff","Contannotate_pVA564-37.gff",\
           "Contannotate_pVA564-63.gff","Contannotate_pVA564-179.gff",\
           "Contannotate_pVA569-6.gff","Contannotate_pVA569-7.gff",\
           "Contannotate_pVA569-35.gff","Contannotate_pVA569-78.gff",\
           "Contannotate_pVA591-7.gff","Contannotate_pVA591-9.gff",\
           "Contannotate_pVA591-46.gff","Contannotate_pVA591-160.gff",\
           "Contannotate_pVA681-5.gff","Contannotate_pVA681-14.gff",\
           "Contannotate_pVA681-36.gff","Contannotate_pVA681-58.gff",\
            "Contannotate_pVA681-191.gff","Contannotate_pVA684-2.gff",\
            "Contannotate_pVA684-6.gff","Contannotate_pVA684-8.gff",\
            "Contannotate_pVA684-49.gff","Contannotate_pVA684-146.gff",\
            "Contannotate_pVA684-388.gff","Contannotate_pVA833-7.gff",\
            "Contannotate_pVA833-92.gff","Contannotate_pVA833-165.gff",\
            "Contannotate_pVA833-176.gff"]

entrada2 = ["pVA04-6.fa","pVA04-46.fa","pVA04-58.fa","pVA04-196.fa","pVA126-12.fa","pVA126-42.fa",\
           "pVA126-68.fa","pVA126-175.fa","pVA126-339.fa","pVA172-67.fa","pVA172-90.fa",\
           "pVA32-7.fa","pVA32-58.fa","pVA32-74.fa","pVA32-104.fa","pVA32-200.fa","pVA564-33.fa",\
           "pVA564-37.fa","pVA564-63.fa","pVA564-179.fa","pVA569-6.fa","pVA569-7.fa","pVA569-35.fa",\
           "pVA569-78.fa","pVA591-7.fa","pVA591-9.fa","pVA591-46.fa","pVA591-160.fa","pVA681-5.fa",\
           "pVA681-14.fa","pVA681-36.fa","pVA681-58.fa","pVA681-191.fa","pVA684-2.fa","pVA684-6.fa",\
           "pVA684-8.fa","pVA684-49.fa","pVA684-146.fa","pVA684-388.fa","pVA833-7.fa","pVA833-92.fa",\
           "pVA833-165.fa","pVA833-176.fa"]

for x in entrada:
    x0 = x.split(".gff")[0]
    x1 = x0.split("Contannotate_")[1]
    for y in entrada2:
        y0 = y.split(".fa")[0]
        if x1 == y0:
            with open(y,"r") as annot_file:
                with open(x,'a',newline='') as annot_file2:
                    annot_file2.write("##FASTA\n")
                    for line in annot_file:
                        annot_file2.write(line)                
                        
