#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:42:42 2022

@author: joaquin
"""
import csv

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

allsep = []    
    
featurest = 0
antibioticrest = 0
penemt = 0
t4sst = 0
sst = 0
tnt = 0
coppert = 0
metalrest = 0
integront = 0
hpt = 0
phaget = 0

for x in entrada:
    sep = []
    with open(x,"r") as annot_file:
        features = 0
        antibioticres = 0
        penem = 0
        t4ss = 0
        ss = 0
        tn = 0
        copper = 0
        metalres = 0
        integron = 0
        hp = 0
        phage = 0
        for feature in annot_file:
            if "feature" in feature:
                featurest = featurest + 1
                features = features + 1
            if "IVIP" in feature or "integron" in feature or "Integron" in feature:
                integront = integront + 1
                integron = integron + 1
            if "antibiotic" in feature or "pump" in feature or "drug" in feature:
                antibioticrest = antibioticrest + 1
                antibioticres = antibioticres + 1
            if "penem" in feature or "carbapene" in feature or "lactamase" in feature:
                penemt = penemt + 1
                penem = penem + 1
            if "Type IV" in feature or "t4ss" in feature or "T4SS" in feature:
                t4sst = t4sst + 1
                t4ss = t4ss + 1
            if "secretion" in feature:
                sst = sst + 1
                ss = ss + 1
            if "transposase" in feature or "Transposase" in feature or "Resolvase" in feature or "resolvase" in feature:
                tnt = tnt + 1
                tn = tn + 1
            if "METDB" in feature or "Arsenic" in feature or "arsenic" in feature or "mercur" in feature or "Mercur" in feature or "Tellurium" in feature or "tellurium" in feature:
                metalrest = metalrest + 1
                metalres = metalres + 1
            if "copper" in feature or "Copper" in feature:
                coppert = coppert + 1
                copper = copper + 1
            if "phage" in feature or "Phage" in feature or "PHAGE" in feature:
                phage = phage + 1
                phaget = phaget + 1
            if "hypothetical protein" in feature:
                hpt = hpt + 1
                hp = hp + 1
        name0 = x.split(".gff")[0]
        name1 = name0.split("Contannotate_")[1]
        sep.append(name1)
        sep.append(antibioticres)
        sep.append(penem)
        sep.append(integron)
        sep.append(ss)
        sep.append(t4ss)
        sep.append(tn)
        sep.append(metalres)
        sep.append(copper)
        sep.append(phage)
        sep.append(hp)
        sep.append(features)
        allsep.append(sep)

sept = []
sept.append("Total")
sept.append(antibioticrest)
sept.append(penemt)
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

        
header_tsv = ["ID","Antibiotic Resistance", "B-Lactamase","Integron", "SS", "T4SS", "Transposon", "Metal Resistance", "Copper Resistance","Phage","Hypotethical Protein", "Features"]
with open("Raw_Statistical_Review_A", 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_tsv)
    tsv_output.writerows(allsep)