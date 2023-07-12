#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 19:03:33 2022

@author: joaquin
"""

########## CREAR UN ARCHIVO DESDE GFF PARA CONVERTIR A GBK,PROKKA #############
import os
import sys
import csv

original = sys.argv[1] #.gff
custom0 = os.path.basename(original)
custom0a = custom0.split(".gff")[0]
custom0b = custom0a.split("phages_")[1]
custom1 = "phagebooster_%s_results.txt" %(custom0b)

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
        
        if '#' in line:
            continue
        
        else:
            # Se procesará la línea
            sep = []
            # Se separan las líneas donde haya un doble espacio
            sep = line.strip().split("\t")
            # Se juntarán las líneas con un espacio entremedio,
            # esto eliminará los elementos que son solo un espacio
            sep = " ".join(sep).split()
            last = int(len(sep))
            # Loop que juntará todas las palabras en el elemento de index = 
            c_word = 6
            list_words_description = []
            rot1=sep[5]
            rot2=sep[6]
            sep[5]=rot2
            sep[6]=rot1
            while(c_word < int(last)):
                list_words_description.append(sep[c_word])
                new_description = " ".join(list_words_description)
                c_word = c_word + 1
    
            sep[6] = new_description
            #Se borrarán los elementos sobrantes
            del(sep[7:last+1])
            del(sep[1:3])
            
            #Cambiar . por 0
            if '.' in sep[3]:
                sep[3]='0'
            contig = sep[0]
            sep[0] = "PHAGE(" + contig + ")"
            
        all_sep.append(sep)     
    # Escribir la información en el archivo nuevo    
with open(custom1, 'a', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    tsv_output.writerows(all_sep)

############# Agradecimientos especiales a Pabu y Sir Robert ##################          