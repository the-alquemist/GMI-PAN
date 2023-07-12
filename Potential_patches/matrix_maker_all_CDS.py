#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:12:45 2022

@author: joaquin
"""
import csv

# Create a matrix #
with open("multifastp_17mar23_cluster.tsv","r") as in_file:
# Create list for each cluster #       
    c1 = []
    file = []
    for line in in_file:
        file_s = []
        n = line.strip().split("\t")
        n1 = n[0]
        n2 = n[1]
        file_s.append(n1)
        file_s.append(n2)
        file.append(file_s)
        if n1 not in c1:
            c1.append(n1)
        else:
            continue

# Eliminate Duplicates #
    filef = []
    for x in file:
        if x not in filef:
            filef.append(x)
            
    c_list = []
    for iteratorA in c1:
        cc = []
        for index,value in enumerate(filef):
            c = tuple(value)
            if iteratorA in value:
                cc.append(c)
                c_list.append(cc)
    c_f_list = []
    for candidate in c_list:
        if candidate not in c_f_list:
            c_f_list.append(candidate)

# Build Matrix #
entrada = ["pVA04-6","pVA04-46","pVA04-58","pVA04-196","pVA126-12","pVA126-42",\
           "pVA126-68","pVA126-175","pVA126-339","pVA172-67","pVA172-90",\
           "pVA32-7","pVA32-58","pVA32-74","pVA32-104","pVA32-200","pVA564-33",\
           "pVA564-37","pVA564-63","pVA564-179","pVA569-6","pVA569-7","pVA569-35",\
           "pVA569-78","pVA591-7","pVA591-9","pVA591-46","pVA591-160","pVA681-5",\
           "pVA681-14","pVA681-36","pVA681-58","pVA681-191","pVA684-2","pVA684-6",\
           "pVA684-8","pVA684-49","pVA684-146","pVA684-388","pVA833-7","pVA833-92",\
           "pVA833-165","pVA833-176"]

plasmid_p_a = []
prefix = "_"
for x in entrada:
    p_a = []
    p_a.append(x)
    x += prefix
    for y in c_f_list:
        n = 0
        for z in y:
            t = 0
            for e in z:
                if x in e:
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
                   
           
header_tsv = ("",) + tuple(c1)
with open("table_all.tsv", 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')        
    tsv_output.writerow(header_tsv)
    for data in plasmid_p_a:
        tsv_output.writerow(data)

with open("cluster_list.txt",'w',newline='') as c_output:
    for a1 in c1:
        c_output.write(a1 + "\n")