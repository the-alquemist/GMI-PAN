#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:12:45 2022

@author: joaquin?
"""
import csv

# Check antibiotic .txt list and store data #
carbapenem_list = []
with open("multifastp_d.fa","r") as in2_file:
    for b1 in in2_file:
        if ">" in b1:
            row = b1.strip().split(">")
            rowname = row[1]
            carbapenem_list.append(rowname)
# #
# Tiene todas las tuplas
file = []
# Tiene todos los primeros del par
c1 = []
# elimina duplicados
filef = []
a_c_list = []
a_cc_list = []
a_cc_list_f = []

with open("multifastp_17mar23_cluster.tsv","r") as in_file:
# Separate each cluster and its content (file), c1 is a only cluster list #       
    for line in in_file:
        n = line.strip().split("\t")
        file.append([n[0],n[1]])
        if n[0] not in c1:
            c1.append(n[0])
        else:
            continue
# Eliminate Duplicates, for some reason there are duplicates in the original file #
    for x in file:
        if x not in filef:
            filef.append(x)
# filef is not the final list because even when the content is not repeated, the cluster name is #            
    for index,value in enumerate(filef):
        for annotation in carbapenem_list:
            if value[0] in annotation or value[1] in annotation:
                if value not in a_c_list:
                    a_c_list.append(value)
                else:
                    continue
            else:
                continue

# Unique clusters from a_c_list? #
for wa in a_c_list:
    if wa[0] not in a_cc_list:
        a_cc_list.append(wa[0])
    else:
        continue
for we in a_cc_list:
    local = []
    for wi in a_c_list:
        if we in wi:
            local.append(wi[1])
            if local not in a_cc_list_f:
                a_cc_list_f.append(local)
        else:
            continue
                                      
# Build Matrix #
entrada = ["pVA04-6","pVA04-46","pVA04-58","pVA04-196","pVA126-12","pVA126-42",\
           "pVA126-68","pVA126-175","pVA126-339","pVA172-67","pVA172-90",\
           "pVA32-58","pVA32-74","pVA32-200",\
           "pVA564-37","pVA564-63","pVA564-179","pVA569-6", "pVA569-35",\
           "pVA569-78","pVA591-46","pVA591-160",\
           "pVA681-14","pVA681-58","pVA681-191",\
           "pVA684-49","pVA684-146","pVA684-388","pVA833-7","pVA833-92",\
           "pVA833-165","pVA833-176"]
    
# Not included because they have nothing: pVA684-8,pVA684-6,pVA684-2,pVA681-36,
# pVA591-9, pVA591-7, pVA32-104, pVA681-14

#Not included because they didnt cluster pVA681-5, pVA32-7, pVA569-7

plasmid_p_a = []
prefix = "_"
for x in entrada:
    p_a = []
    p_a.append(x)
    x += prefix
    for y in a_cc_list_f:
        n = 0
        t = 0
        for z in y:
            if x in z:
                t = 1
            else:
                continue
        if t==0:
            p_a.append(n)
        elif t == 1:
            n = 1
            p_a.append(n)
        else:
            continue
    plasmid_p_a.append(p_a)                   
           
header_tsv = ("Contig",) + tuple(a_cc_list)
with open("table_only_resistance.tsv", 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')        
    tsv_output.writerow(header_tsv)
    for data in plasmid_p_a:
        tsv_output.writerow(data)
