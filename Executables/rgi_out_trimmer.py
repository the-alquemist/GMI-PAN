#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:31:07 2022

@author: joaquin
"""

########## CREAR UN ARCHIVO DESDE TXT PARA CONVERTIR A GBK,RGI ################
import os
import sys
import csv

original = sys.argv[1] #.txt
custom0 = os.path.basename(original)
custom0a = custom0.split(".txt")[0]
custom0b = custom0a.split("RGI_")[1]
custom1 = "rgi_%s_results.txt" % (custom0b)

# Crear el archivo nuevo, con solo el encabezado
header_prokka_tsv = ["ID","START", "END", "STRAND", "NOTES"]
with open(custom1, 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_prokka_tsv)

# Lista que contendrá toda la información que será escrita
all_sep = []

# Abrir el archivo de salida de prokka
with open(original, "r") as data_genes:
    for line in data_genes:
        
        if "Contig" in line:
            continue
        
        else:
            # Se procesará la línea
            sep = []
            idy = []
            idx = []
            # Se separan las líneas donde haya un doble espacio
            sep = line.strip().split("#")
            # Se remueven los info extra
            for y in sep:
                if "ID=" in y:
                    idy = y.strip().split("\t")
                else:
                    continue
            for z in idy:
                if "protein homolog model" in z:
                    c = idy.index(z)
                    c1 = c + 3
                    antibiotico = idy[c1]
#                    c2 = c1 + 1
#                    target = idy[c2]
#                    c3 = c2 + 1
#                    family = idy[c3]
                else:
                    continue
            if ";" in antibiotico:
                        idx = antibiotico.strip().split(";")
                        sep[0] = idx[-1] + "(RGI)"
            else:                           
                 sep[0] = antibiotico + "(RGI)"            
        all_sep.append(sep)   
    # Escribir la información en el archivo nuevo    
with open(custom1, 'a', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerows(all_sep)

############# Agradecimientos especiales a Pabu y Sir Robert ##################          