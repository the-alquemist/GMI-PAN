#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 15:31:07 2022

@author: joaquin
"""

################# CREAR UN ARCHIVO DESDE TXT DESDE NHMMER #####################

import os
import sys
import csv

original = sys.argv[1]
custom0 = os.path.basename(original)
custom0a = custom0.split(".txt")[0]
custom0b = custom0a.split("nhmmer_")[1]
custom1 = "nhmmer_%s_results.txt" %(custom0b)

# Crear el archivo nuevo, con solo el encabezado
header_nhmmer_tsv = ["ID","START", "END", "STRAND", "NOTES"]
with open(custom1, 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerow(header_nhmmer_tsv)

# Lista que contendrá toda la información que será escrita
all_sep = []

# Abrir el archivo de salida de nhmmer
with open(original, "r") as data_genes:
    for line in data_genes:
        
        if "#" in line:
            continue
        
        else:
            # Se procesará la línea
            sep = []
            # Se separan las líneas donde haya un doble espacio
            sep = line.strip().split("  ")
            # Se juntarán las líneas con un espacio entremedio,
            # esto eliminará los elementos que son solo un espacio
            sep = " ".join(sep).split()
            last = int(len(sep))
            # Loop que juntará todas las palabras en el elemento de index = 15
            c_word = 15
            list_words_description = []
            
            while(c_word < int(last)):
                list_words_description.append(sep[c_word])
                new_description = " ".join(list_words_description)
                c_word = c_word + 1
            
            sep[15] = new_description
            # Se borrarán los elementos sobrantes
            del(sep[16:last+1])
            # Quiero que el nombre del target vaya en la descripcion no antes
            sep.append(sep[2])
            removables = [sep[1],sep[2],sep[3],sep[4],sep[5]]       
            for x in removables:
                sep.remove(x)
            del(sep[3:6])
            del(sep[4:8])
            rot = sep[0]
            rot1 = sep[4]
            sep[0] = rot1
            sep[4] = rot
            if "+" in sep[3]:
                sep[3] = "+1"
            elif "-" in sep[3]:
                sep[3] = "-1"
            else:
                sep[3] = "0"
            
        all_sep.append(sep)

    # Escribir la información en el archivo nuevo
    with open(custom1, 'a', newline='') as f_output:
        tsv_output = csv.writer(f_output, delimiter='\t')
        tsv_output.writerows(all_sep)

############# Agradecimientos especiales a Pabu y Sir Robert ##################