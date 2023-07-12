#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:24:49 2023

@author: joaquin
"""
#RGI PATCHER#
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
    
inputx2 = ["RGI_pVA04-6.txt","RGI_pVA04-46.txt",\
           "RGI_pVA04-58.txt","RGI_pVA04-196.txt",\
           "RGI_pVA126-12.txt","RGI_pVA126-42.txt",\
           "RGI_pVA126-68.txt","RGI_pVA126-175.txt",\
           "RGI_pVA126-339.txt","RGI_pVA172-67.txt",\
           "RGI_pVA172-90.txt","RGI_pVA32-7.txt",\
           "RGI_pVA32-58.txt","RGI_pVA32-74.txt",\
           "RGI_pVA32-104.txt","RGI_pVA32-200.txt",\
           "RGI_pVA564-33.txt","RGI_pVA564-37.txt",\
           "RGI_pVA564-63.txt","RGI_pVA564-179.txt",\
           "RGI_pVA569-6.txt","RGI_pVA569-7.txt",\
           "RGI_pVA569-35.txt","RGI_pVA569-78.txt",\
           "RGI_pVA591-7.txt","RGI_pVA591-9.txt",\
           "RGI_pVA591-46.txt","RGI_pVA591-160.txt",\
           "RGI_pVA681-5.txt","RGI_pVA681-14.txt",\
           "RGI_pVA681-36.txt","RGI_pVA681-58.txt",\
            "RGI_pVA681-191.txt","RGI_pVA684-2.txt",\
            "RGI_pVA684-6.txt","RGI_pVA684-8.txt",\
            "RGI_pVA684-49.txt","RGI_pVA684-146.txt",\
            "RGI_pVA684-388.txt","RGI_pVA833-7.txt",\
            "RGI_pVA833-92.txt","RGI_pVA833-165.txt",\
            "RGI_pVA833-176.txt"]
    
#Aca va el recuperador#
feature_data_bank=[]
wa = []
waa = []
for gb_file in inputx:    
    for gb_record in SeqIO.parse(open(gb_file,"r"),"genbank"):
        fs = gb_record.features
        for feature in fs:
            rgi = feature.qualifiers['note']
            if "This feature was annotated with RGI" in rgi[0]:
                we = ()
                gb_file_pre = gb_file.split("_")[1]
                gb_file_prefix = gb_file_pre.split(".")[0]
                rgi_ref = "RGI_" + gb_file_prefix + ".txt"
                diff = int(feature.strand)
                diff_s = int(feature.location.start.numerator) + 1
                diff_e = int(feature.location.end.numerator)
                with open(rgi_ref,"r") as ref_file:
                    for line in ref_file:
                        coordinate = "# " + str(diff_s) + " # " + str(diff_e) + " #"
                        if coordinate in line:
                            line_start = int(line.split("# ")[1])
                            line_end = int(line.split("# ")[2])
                            line_strand = int(line.split("# ")[3])
                            we=(diff,line_strand,gb_file_prefix,coordinate)
                if we[0]!= we[1]:
                    wa.append(we)
                    feature.strand = we[1]
                    SeqIO.write(gb_record,gb_file,"genbank")
                waa.append(we)               
                feature_data_bank.append(rgi)