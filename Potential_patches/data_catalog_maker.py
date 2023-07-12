#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 17:12:20 2022

@author: joaquin
"""

entrada = ["pVA04-6.fa","pVA04-46.fa","pVA04-58.fa","pVA04-196.fa","pVA126-12.fa","pVA126-42.fa",\
           "pVA126-68.fa","pVA126-175.fa","pVA126-339.fa","pVA172-67.fa","pVA172-90.fa",\
           "pVA32-7.fa","pVA32-58.fa","pVA32-74.fa","pVA32-104.fa","pVA32-200.fa","pVA564-33.fa",\
           "pVA564-37.fa","pVA564-63.fa","pVA564-179.fa","pVA569-6.fa","pVA569-7.fa","pVA569-35.fa",\
           "pVA569-78.fa","pVA591-7.fa","pVA591-9.fa","pVA591-46.fa","pVA591-160.fa","pVA681-5.fa",\
           "pVA681-14.fa","pVA681-36.fa","pVA681-58.fa","pVA681-191.fa","pVA684-2.fa","pVA684-6.fa",\
           "pVA684-8.fa","pVA684-49.fa","pVA684-146.fa","pVA684-388.fa","pVA833-7.fa","pVA833-92.fa",\
           "pVA833-165.fa","pVA833-176.fa"]

with open("data_catalog.txt","a",newline='') as data_file:    
    for x in entrada:
        x0 = x.split(".fa")[0]
        data="//\n \
Genome %s\n \
Sequence %s.fa\n \
Annotation 	Contannotate_%s.gff\n" % (x0,x0,x0)
        data_file.write(data)