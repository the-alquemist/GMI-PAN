#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:42:42 2022

@author: joaquin
"""
import csv

entrada = ["pVA04-6.txt","pVA04-46.txt","pVA04-58.txt","pVA04-196.txt","pVA126-12.txt","pVA126-42.txt",\
           "pVA126-68.txt","pVA126-175.txt","pVA126-339.txt","pVA172-67.txt","pVA172-90.txt",\
           "pVA32-7.txt","pVA32-58.txt","pVA32-74.txt","pVA32-104.txt","pVA32-200.txt","pVA564-33.txt",\
           "pVA564-37.txt","pVA564-63.txt","pVA564-179.txt","pVA569-6.txt","pVA569-7.txt","pVA569-35.txt",\
           "pVA569-78.txt","pVA591-7.txt","pVA591-9.txt","pVA591-46.txt","pVA591-160.txt","pVA681-5.txt",\
           "pVA681-14.txt","pVA681-36.txt","pVA681-58.txt","pVA681-191.txt","pVA684-2.txt","pVA684-6.txt",\
           "pVA684-8.txt","pVA684-49.txt","pVA684-146.txt","pVA684-388.txt","pVA833-7.txt","pVA833-92.txt",\
           "pVA833-165.txt","pVA833-176.txt"]
allsep = []
featurest = 0
integront = 0
antibiotict = 0
lactamt = 0
sst = 0
t4sst = 0
tnt = 0
metalrest = 0
coppert = 0
hpt = 0
phaget = 0
for x in entrada:
    sep = []
    with open(x,"r") as annot_file:
        antibiotic = 0
        integron = 0
        lactam = 0
        ss = 0
        t4ss = 0
        tn = 0
        metalres = 0
        copper = 0
        hp = 0
        featurex = 0
        phage = 0
        for feature in annot_file:
            featurest = featurest + 1
            featurex = featurex + 1
            if "antibiotic" in feature or "pump" in feature or "drug" in feature:
                antibiotic = antibiotic + 1
                antibiotict = antibiotict + 1
            if "lactamase" in feature or "penem" in feature or "carbapene" in feature:
                lactam = lactam +1
                lactamt = lactamt + 1
            if "integron" in feature:
                integron = integron + 1
                integront = integront + 1
            if "secretion" in feature:
                ss = ss + 1
                sst = sst + 1
            if "T4SS" in feature or "t4ss" in feature or "Type IV" in feature or "type IV" in feature:
                t4ss = t4ss + 1
                t4sst = t4sst + 1
            if "tranposon" in feature or "transposase" in feature or "Transposase" in feature or "Resolvase" in feature or "resolvase" in feature:
                tn = tn + 1
                tnt = tnt + 1
            if "METDB" in feature or "Arsenic" in feature or "arsenic" in feature or "mercur" in feature or "Mercur" in feature or "Tellurium" in feature or "tellurium" in feature:
                metalres = metalres + 1
                metalrest = metalrest + 1
            if "copper" in feature or "Copper" in feature:
                copper = copper + 1
                coppert = coppert + 1
            if "phage" in feature or "Phage" in feature or "PHAGE" in feature:
                phage = phage + 1
                phaget = phaget + 1
            if "hypothetical protein" in feature:
                hp = hp + 1
                hpt = hpt + 1
        name0 = x.split(".txt")[0]
        sep.append(name0)
        sep.append(antibiotic)
        sep.append(lactam)
        sep.append(integron)
        sep.append(ss)
        sep.append(t4ss)
        sep.append(tn)
        sep.append(metalres)
        sep.append(copper)
        sep.append(phage)
        sep.append(hp)
        sep.append(featurex)
        allsep.append(sep)

sept = []
sept.append("Total")
sept.append(antibiotict)
sept.append(lactamt)
sept.append(integront)
sept.append(sst)
sept.append(t4sst)
sept.append(tnt)
sept.append(metalrest)
sept.append(coppert)
sept.append(phaget)
sept.append(hpt)
sept.append(featurest)       
allsep.append(sept)

        
header_tsv = ["ID","Antibiotic Resistance", "B-Lactamase","Integron", "SS", "T4SS", "Transposon", "Metal Resistance", "Copper Resistance","Phage","Hypothetical proteins","Features"]
with open("Raw_Statistical_Review_M", 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_tsv)
    tsv_output.writerows(allsep)