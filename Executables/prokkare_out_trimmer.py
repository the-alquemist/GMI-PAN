#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:31:07 2022

@author: joaquin
"""

########## CREAR UN ARCHIVO DESDE GFF PARA CONVERTIR A GBK,PROKKA #############
import os
import sys
import csv

original = sys.argv[1] #.gff
custom0 = os.path.basename(original)
custom0a = custom0.split(".gff")[0]
custom1 = "prokkare_%s_results.txt" %(custom0a)

# Lista que contendrá toda la información que será escrita
all_sep = []

# Abrir el archivo de salida de prokka
with open(original, "r") as data_genes:
    for line in data_genes:
        
        if "##FASTA" in line:
            break
        
        elif "#" in line:
            continue
        
        else:
            # Se procesará la línea
            sep = []
            ojo = 0
            sep = line.strip().split("\t")
            fileid = sep[0]
            for y in sep:
                if "product=" in y:
                    idy = y.strip().split(";")
                    product = idy[-1]
                elif "rpt_" in y:
                    idy = y.strip().split(";")
                    product = idy[0]
                    ojo = 1
                else:
                    product = ""    
            removables = [sep[1],sep[2],sep[5],sep[7]]         
            for x in removables:
                sep.remove(x)
            sep[0] = product[8:]
            if ojo == 1:
                sep[0] = product[5:]
        all_sep.append(sep)
        
# Crear el archivo nuevo, con solo el encabezado
header_prokka_tsv = ["ID","START", "END", "STRAND", "NOTES"]
with open('%s'%(custom1), 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_prokka_tsv)
        
# Escribir la información en el archivo nuevo
with open('%s'%(custom1), 'a', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerows(all_sep)

############# Agradecimientos especiales a Pabu y Sir Robert ##################          