#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 16:03:13 2022

@author: joaquin
"""


########## CREAR UN ARCHIVO DESDE GFF PARA CONVERTIR A GBK,PROKKA #############

import os
import sys
import csv

original = sys.argv[1] # all.ORFs.fasta
original1 = sys.argv[2] # max.attC.hits
original2 = sys.argv[3]  # pVA126-68.Integron.txt
custom0 = os.path.basename(original2)
custom0a = custom0.split(".Integron.txt")[0]
custom1 = "ivip_%s_results.txt" %(custom0a) 

# Crear el archivo nuevo, con solo el encabezado
header_prokka_tsv = ["ID","START", "END", "STRAND", "NOTES"]
with open('%s'%(custom1), 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_prokka_tsv)

# Lista que contendrá toda la información que será escrita
all_sep = []

# Abrir el archivo de salida de prokka
with open(original, "r") as data_genes:
    for line in data_genes:
        
        if ">" not in line:
            continue
        
        else:
            # Se procesará la línea
            sep = []
            # Se separan las líneas donde haya un doble espacio
            sep = line.strip().split("/t")
            # Se juntarán las líneas con un espacio entremedio,
            # esto eliminará los elementos que son solo un espacio
            sep = " ".join(sep).split()
            # Se borrarán los elementos sobrantes
            del(sep[2:7])
            removables = [sep[0],sep[3],sep[5],sep[7]]         
            for x in removables:
                sep.remove(x)          
            
        all_sep.append(sep)

with open(original1, "r") as data_genes:
    for line in data_genes:
        
        if "#" in line:
            continue
        
        else:
            # Se procesará la línea
            sep1 = []
            # Se separan las líneas donde haya un doble espacio
            sep1 = line.strip().split("/t")
            # Se juntarán las líneas con un espacio entremedio,
            # esto eliminará los elementos que son solo un espacio
            sep1 = " ".join(sep1).split()
            # Se borrarán los elementos sobrantes
            last = int(len(sep1))
            del(sep1[0:2])
            del(sep1[1:5])
            del(sep1[4:last+1])
            sep1.append("-")
            
            if "+" in sep1[3]:
               sep1[3] = "1"
            
            elif "-" in sep1[3]:
                 sep1[3] = "-1"
            
            else:
                continue
             
            
        all_sep.append(sep1)

with open(original2, "r") as data_genes:
    for line in data_genes:
        
        if "Integron_Type" in line:
            continue
        
        else:
            # Se procesará la línea
            sep2 = []
            # Se separan las líneas donde haya un doble espacio
            sep2 = line.strip().split("/t")
            # Se juntarán las líneas con un espacio entremedio,
            # esto eliminará los elementos que son solo un espacio
            sep2 = " ".join(sep2).split()
            last1 = int(len(sep2))
            del(sep2[1:last1+1])
            sep2[0]= "Integron_Type = " + sep2[0]
        all_sep.append(sep2)
        
# Escribir la información en el archivo nuevo
with open('%s'%(custom1), 'a', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerows(all_sep)

############# Agradecimientos especiales a Pabu y Sir Robert ##################