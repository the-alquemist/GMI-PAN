#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 21:25:59 2022

@author: joaquin
"""

########## CREAR UN ARCHIVO DESDE TSV PARA CONVERTIR A GBK,PROKKA #############

import sys
import csv

original = sys.argv[1] # .tsv

# Lista que contendrá toda la información que será escrita
all_sep = []

# Abrir el archivo de salida de prokka
with open(original, "r") as data_genes:
    for line in data_genes:
        
        if "Database" in line:
            continue
                
        else:
            # Se procesará la línea
            sep = []
            # Se separan las líneas donde haya un doble espacio
            sep = line.strip().split("\t")
            # Se juntarán las líneas con un espacio entremedio,
            # esto eliminará los elementos que son solo un espacio
            Id=sep[1]
            Note = sep[-1]
            Pos = sep[5]
            Post = Pos.strip().split("..")
            start = Post[0]
            end = Post[1]
            ctg = sep[4]
            contigt = ctg.strip().split(" ")
            contig = contigt[0] #Potencial error con missmatch de nombre original
            sep1 = []
            sep1.append(Id)
            sep1.append(start)
            sep1.append(end)
            sep1.append("0")
            sep1.append(Note)
        all_sep.append(sep1)

# Crear el archivo nuevo, con solo el encabezado
custom1 = "plasmidfinder_%s_results.txt" % (contig)

header_prokka_tsv = ["ID","START", "END", "STRAND", "NOTES"]
with open('%s'%(custom1), 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_prokka_tsv)
        
# Escribir la información en el archivo nuevo
with open('%s'%(custom1), 'a', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerows(all_sep)

############# Agradecimientos especiales a Pabu y Sir Robert ##################