#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 12:29:54 2022

@author: joaquin
"""
# Reemplazar sys por argparse. Tomar cada indentacion de PF,PB y IVIP y ponerlas bajo un if/else respectivamente # 

import datetime
import os
import argparse
from Bio import SeqIO

# Nombre del archivo .txt con la información a incorporar
parser = argparse.ArgumentParser()
parser.add_argument("-nh", type=str, help=("nhmmer input"))
parser.add_argument("-pf", type=str, help=("pfinder input"))
parser.add_argument("-pb", type=str, help=("pbooster input"))
parser.add_argument("-iv", type=str, help=("ivip input"))
parser.add_argument("-rg", type=str, help=("rgi input"))
parser.add_argument("-pv", type=str, help=("pverify input"))
parser.add_argument("-prvf", type=str, help=("prokka input"))
parser.add_argument("-prau", type=str, help=("prokka input"))
parser.add_argument("-prar", type=str, help=("prokka input"))
parser.add_argument("-prt4", type=str, help=("prokka input"))
parser.add_argument("-prme", type=str, help=("prokka input"))
parser.add_argument("-i", type=str, help=("fasta input"))

args = parser.parse_args()
gbknameo = os.path.basename(args.i)
gbkname = gbknameo.split(".fa")[0]
out_gbk = "Contannotate_%s.gbk" % (gbkname)
x = datetime.datetime.now()
date = x.strftime("%d ") + x.strftime("%B ") + x.strftime("%Y")
# Abrir el archivo con la información original de .fasta
with open(args.i,"r") as annot_file:
    # Se le pide a SeqIO que manipule la info del archivo como un genbank
    for record in SeqIO.parse(annot_file, "fasta"):
        # Abrir la tabla con los resultados de las secuencias
        # NHMMER #          
        with open(args.nh, "r") as data_genes:
            # Aquí va lo que quieres hacer con los datos del archivo .txt.
            # Lo que yo hacía era agregar la información como un feature
            # y lo agregaba al record abierto
            for line in data_genes:
                # Se procesará la línea
                sep = []
                # Se separan las líneas donde haya un doble espacio
                sep = line.strip().split("\t")
                if "ID" in line:
                    continue
             
                else:
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+1":
                        strnd = +1
                    elif sentido == "-1":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "oriT"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    feature = SeqFeature(
                        feature_location,
                        type=feature_type,
                        strand=strnd,
                        id=sep[0],
                        qualifiers={
                            "label" : sep[0],
                           "product": sep[0],
                           "note" : "This feature was annotated with NHMMER"
                           }
                        )
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)

        try:
            # PLASMIDFINDER #
            with open(args.pf, "r") as data_genes:
                for line in data_genes:
                        # Se procesará la línea
                        sep = []
                        # Se separan las líneas donde haya un doble espacio
                        sep = line.strip().split("\t")
                        if "ID" in line:
                            continue
                     
                        else:
                            from Bio import SeqFeature
                            sep[1] = int(sep[1])
                            sep[2] = int(sep[2])
                            sentido = sep[3]
                            #Forzar sentido
                            if sentido == "+1":
                                strnd = +1
                            elif sentido == "-1":
                                strnd = -1
                            else:
                                strnd = 0
                            #Ubicacion
                            if sep[1] < sep[2]:
                                start_pos = SeqFeature.ExactPosition(sep[1])
                                end_pos = SeqFeature.ExactPosition(sep[2])                    
                            else:
                                start_pos = SeqFeature.ExactPosition(sep[2])
                                end_pos = SeqFeature.ExactPosition(sep[1])                        
                            # Use the locations do define a FeatureLocation
                            from Bio.SeqFeature import FeatureLocation
                            feature_location = FeatureLocation(start_pos,end_pos)
                            # Define a feature type as a text string 
                            #(you can also just add the type when creating the SeqFeature)
                            feature_type = "INC"
                            # Create a SeqFeature
                            from Bio.SeqFeature import SeqFeature
                            feature = SeqFeature(
                                feature_location,
                                type=feature_type,
                                strand=strnd,
                                id=sep[0],
                                qualifiers={
                                    "label" : sep[0],
                                   "product": sep[0],
                                   "note" : "This feature was annotated with Plasmidfinder"
                                   }
                                )
                            # Append your newly created SeqFeature to your SeqRecord
                        record.features.append(feature)
        except:
            print("This contig does not include PF results.")
        
        try:    
            # PHAGEBOOSTER #
            with open(args.pb, "r") as data_genes:
                for line in data_genes:
                        # Se procesará la línea
                        sep = []
                        # Se separan las líneas donde haya un doble espacio
                        sep = line.strip().split("\t")
                        if "phage_id=" in line:
                            phageid = line.strip().split(";")
                            phageproduct = phageid[-1]
                        else:
                            continue
                        if "ID" in line:
                            continue
                     
                        else:
                            from Bio import SeqFeature
                            sep[1] = int(sep[1])
                            sep[2] = int(sep[2])
                            sentido = sep[3]
                            #Forzar sentido
                            if sentido == "+1":
                                strnd = +1
                            elif sentido == "-1":
                                strnd = -1
                            else:
                                strnd = 0
                            #Ubicacion
                            if sep[1] < sep[2]:
                                start_pos = SeqFeature.ExactPosition(sep[1])
                                end_pos = SeqFeature.ExactPosition(sep[2])                    
                            else:
                                start_pos = SeqFeature.ExactPosition(sep[2])
                                end_pos = SeqFeature.ExactPosition(sep[1])                        
                            # Use the locations do define a FeatureLocation
                            from Bio.SeqFeature import FeatureLocation
                            feature_location = FeatureLocation(start_pos,end_pos)
                            # Define a feature type as a text string 
                            #(you can also just add the type when creating the SeqFeature)
                            feature_type = "PHAGE"
                            # Create a SeqFeature
                            from Bio.SeqFeature import SeqFeature
                            feature = SeqFeature(
                                feature_location,
                                type=feature_type,
                                strand=strnd,
                                id=sep[0],
                                qualifiers={
                                    "label" : sep[0],
                                   "product": phageproduct[9:],
                                   "note" : "This feature was annotated with PHAGEBOOSTER"
                                   }
                                )
                            # Append your newly created SeqFeature to your SeqRecord
                            record.features.append(feature)
        except:
            print("This contig does not include PB results.")
        
        try:
            # IVIP #
            with open(args.iv, "r") as data_genes:
                IntList = open(args.iv,"r").readlines() 
                IntList = IntList[-1].strip()
                for line in data_genes:
                        # Se procesará la línea
                        sep = []
                        sep = line.strip().split("\t")
                        if "START" in line:
                            continue
                        
                        elif "Integron_Type" in line:
                            continue            
                        else:
                            from Bio import SeqFeature
                            sep[1] = int(sep[1])
                            sep[2] = int(sep[2])
                            sentido = sep[3]
                            sep[0] = sep[0] + " (IVIP)"
                            #Forzar sentido
                            if sentido == "1":
                                strnd = +1
                            elif sentido == "-1":
                                strnd = -1
                            else:
                                strnd = 0
                            #Ubicacion
                            if sep[1] < sep[2]:
                                start_pos = SeqFeature.ExactPosition(sep[1])
                                end_pos = SeqFeature.ExactPosition(sep[2])                    
                            else:
                                start_pos = SeqFeature.ExactPosition(sep[2])
                                end_pos = SeqFeature.ExactPosition(sep[1])                        
                            # Use the locations do define a FeatureLocation
                            from Bio.SeqFeature import FeatureLocation
                            feature_location = FeatureLocation(start_pos,end_pos)
                            # Define a feature type as a text string 
                            #(you can also just add the type when creating the SeqFeature)
                            feature_type = "INT"
                            # Create a SeqFeature
                            from Bio.SeqFeature import SeqFeature
                            feature = SeqFeature(
                                feature_location,
                                type=feature_type,
                                strand=strnd,
                                id=sep[0],
                                qualifiers={
                                   "label" : sep[0],
                                   "product": sep[0],
                                   "note" : "%s  \
                                       This feature was annotated with IVIP" % (IntList)
                                   }
                                )
                            # Append your newly created SeqFeature to your SeqRecord
                            record.features.append(feature)
        except:
            print("This contig does not include IVIP results.")    
        # RGI #
        with open(args.rg, "r") as data_genes:
            for line in data_genes:
                # Se procesará la línea
                sep = []
                idy = []
                # Se separan las líneas donde haya un doble espacio
                sep = line.strip().split("#")
                # Se juntarán las líneas con un espacio entremedio,
                # esto eliminará los elementos que son solo un espacio
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
                        c2 = c1 + 1
                        target = idy[c2]
                        c3 = c2 + 1
                        family = idy[c3]
                if "STRAND" in line:
                    continue            
                else:
                    sep = line.strip().split("\t")
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+":
                        strnd = +1
                    elif sentido == "-":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "CDS"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    feature = SeqFeature(
                        feature_location,
                        type=feature_type,
                        strand=strnd,
                        id=sep[0],
                        qualifiers={  
                           "product": family,
                           "note" : "Antibiotic = %s \
                                     Target = %s \
                                     Family = %s        \
                                     This feature was annotated with RGI" \
                                     % (antibiotico, target, family),
                           "translation" : "",
                           }
                        )
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)
        # PlasmidVerify #
        with open(args.pv, "r") as data_genes:
            for line in data_genes:
                # Se procesará la línea
                sep = []
                # Se separan las líneas donde haya un doble espacio
                sep = line.strip().split(",")
                # Se juntarán las líneas con un espacio entremedio,
                # esto eliminará los elementos que son solo un espacio
                sep = " ".join(sep).split()
                if "Contig name" in line:
                    continue
             
                else:
                    record.description = "This contig corresponds to a " + \
                        sep[1] + " with a log-likelihood of " + sep[2] \
                        + " and it was pipelined thorugh Contannotate"
        
        # PROKKAVF #
        with open(args.prvf, "r") as data_genes:
            for line in data_genes:
                if "STRAND" in line:
                    continue
                else:
                    # Se procesará la línea
                    sep = []
                    # Se separan las líneas donde haya un doble espacio
                    sep = line.strip().split("\t")
                    idy = sep[-1].strip().split(";")
                    switch = 0
                    for x in idy:
                        if "gene=" in x:
                            genename = x
                            switch = 1
                        else:
                            continue
                    locustag = idy[-2]
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+":
                        strnd = +1
                    elif sentido == "-":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "CDS"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    if switch == 1 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "gene": genename[5:],
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (VFDB)",
                              "translation" : "",
                              }
                          )
                    elif switch == 0 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (VFDB)",
                              "translation" : "",
                              }
                          )  
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)
        
        # PROKKAAUX #
        with open(args.prau, "r") as data_genes:
            for line in data_genes:
                if "STRAND" in line:
                    continue
                else:
                    # Se procesará la línea
                    sep = []
                    # Se separan las líneas donde haya un doble espacio
                    sep = line.strip().split("\t")
                    idy = sep[-1].strip().split(";")
                    switch = 0
                    for x in idy:
                        if "gene=" in x:
                            genename = x
                            switch = 1
                        else:
                            continue
                    locustag = idy[-2]
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+":
                        strnd = +1
                    elif sentido == "-":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "CDS"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    if switch == 1 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "gene": genename[5:],
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (AUXDB)",
                              "translation" : "",
                              }
                          )
                    elif switch == 0 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (AUXDB)",
                              "translation" : "",
                              }
                          )  
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)
                    
        # PROKKARE #
        with open(args.prar, "r") as data_genes:
            for line in data_genes:
                if "STRAND" in line:
                    continue
                else:
                    # Se procesará la línea
                    sep = []
                    # Se separan las líneas donde haya un doble espacio
                    sep = line.strip().split("\t")
                    idy = sep[-1].strip().split(";")
                    switch = 0
                    for x in idy:
                        if "gene=" in x:
                            genename = x
                            switch = 1
                        else:
                            continue
                    locustag = idy[-2]
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+":
                        strnd = +1
                    elif sentido == "-":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "CDS"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    if switch == 1 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "gene": genename[5:],
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (AREDB)",
                              "translation" : "",
                              }
                          )
                    elif switch == 0 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (AREDB)",
                              "translation" : "",
                              }
                          )  
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)
        # PROKKAT4CP #
        with open(args.prt4, "r") as data_genes:
            for line in data_genes:
                if "STRAND" in line:
                    continue
                else:
                    # Se procesará la línea
                    sep = []
                    # Se separan las líneas donde haya un doble espacio
                    sep = line.strip().split("\t")
                    idy = sep[-1].strip().split(";")
                    switch = 0
                    for x in idy:
                        if "gene=" in x:
                            genename = x
                            switch = 1
                        else:
                            continue
                    locustag = idy[-2]
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+":
                        strnd = +1
                    elif sentido == "-":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "CDS"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    if switch == 1 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "gene": genename[5:],
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (T4CPDB)",
                              "translation" : "",
                              }
                          )
                    elif switch == 0 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (T4CPDB)",
                              "translation" : "",
                              }
                          )  
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)
                    
        # PROKKAMET #
        with open(args.prme, "r") as data_genes:
            for line in data_genes:
                if "STRAND" in line:
                    continue
                else:
                    # Se procesará la línea
                    sep = []
                    # Se separan las líneas donde haya un doble espacio
                    sep = line.strip().split("\t")
                    idy = sep[-1].strip().split(";")
                    switch = 0
                    for x in idy:
                        if "gene=" in x:
                            genename = x
                            switch = 1
                        else:
                            continue
                    locustag = idy[-2]
                    from Bio import SeqFeature
                    sep[1] = int(sep[1])
                    sep[2] = int(sep[2])
                    sentido = sep[3]
                    #Forzar sentido
                    if sentido == "+":
                        strnd = +1
                    elif sentido == "-":
                        strnd = -1
                    else:
                        strnd = 0
                    #Ubicacion
                    if sep[1] < sep[2]:
                        start_pos = SeqFeature.ExactPosition(sep[1])
                        end_pos = SeqFeature.ExactPosition(sep[2])                    
                    else:
                        start_pos = SeqFeature.ExactPosition(sep[2])
                        end_pos = SeqFeature.ExactPosition(sep[1])                        
                    # Use the locations do define a FeatureLocation
                    from Bio.SeqFeature import FeatureLocation
                    feature_location = FeatureLocation(start_pos,end_pos)
                    # Define a feature type as a text string 
                    #(you can also just add the type when creating the SeqFeature)
                    feature_type = "CDS"
                    # Create a SeqFeature
                    from Bio.SeqFeature import SeqFeature
                    if switch == 1 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "gene": genename[5:],
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (METDB)",
                              "translation" : "",
                              }
                          )
                    elif switch == 0 :
                      feature = SeqFeature(
                          feature_location,
                          type=feature_type,
                          strand=strnd,
                          id=sep[0],
                          qualifiers={
                              "locus_tag":locustag[10:],
                              "product": sep[0],
                              "note" : "This feature was annotated with PROKKA (METDB)",
                              "translation" : "",
                              }
                          )  
                    # Append your newly created SeqFeature to your SeqRecord
                    record.features.append(feature)
        
        #RECORD ADDITIONAL DATA#
        record.name = gbkname            
        record.annotations["date"] = "%s" % (date)            
        record.annotations["molecule_type"] = "DNA"
        record.annotations["form"] = "double stranded"
        record.annotations["topology"] = "circular"
        
        # FEATUREDUPLICATE --> DELETION #
        n1 = 0
        n2 = 0
        n3 = 0
        n4 = 0
        n5 = 0
        n6 = 0
        n7 = 0
        fbankl = []
        fbankf = []
        fbank_unicos = []
        fbank_duplicados=[]
        newfeatures = []
        rescuefeatures = []
        recoveredfeatures = []
        trueduplicates = []
        newfeaturesf = []
        newfeaturesl = []
        recoveredfeaturesf = []
        recoveredfeaturesl = []
        nfpnc = []
        nfpncr = []
        nfpncrl = []
        nfpncrf = []
        nft = []
        nfpncr2 = []
        nfpncr2f = []
        nfpncr2l = []
        prefinalfeature = []
        prefinalfeaturel = []
        prefinalfeaturef = []
        for feature in record.features:
            fbankf.append(feature)
            fbankl.append(feature.location)
        for i in fbankl:
            if i not in fbank_unicos:
                fbank_unicos.append(i)
                newfeatures.append(record.features[n1])
            else:
                fbank_duplicados.append(i)
                rescuefeatures.append(record.features[n1])
            n1 = n1 + 1
        # SAVING LOST FEATURES #
        for d in rescuefeatures:
            if "hypothetical protein" not in rescuefeatures[n2].id:
                recoveredfeatures.append(rescuefeatures[n2])
            else:
                trueduplicates.append(rescuefeatures[n2])
            n2 = n2 + 1
        for g in newfeatures:
            newfeaturesf.append(g)
            newfeaturesl.append(g.location)
        for h in recoveredfeatures:
            recoveredfeaturesf.append(h)
            recoveredfeaturesl.append(h.location)
        for c in newfeaturesl:
            if c in recoveredfeaturesl:
                nfpnc.append(newfeaturesf[n3])
            else:
                nft.append(newfeaturesf[n3])
            n3 = n3 + 1
        for p in nfpnc:
            if "hypothetical protein" in nfpnc[n4].id and len(nfpnc[n4].id) == 20:
                nfpncr.append(p)
            n4 = n4 + 1
        for z in nfpncr:
            nfpncrf.append(z)
            nfpncrl.append(z.location)
        for j in recoveredfeaturesl:
            if j in nfpncrl:
                nfpncr2.append(recoveredfeatures[n5])
            n5 = n5 + 1
        #Ahora eliminar duplicados de nfpncr2 y reemplazar en newfeatures#
        for deets in nfpncr2:
            nfpncr2l.append(deets.location)
            nfpncr2f.append(deets)
        for du in nfpncr2l:
            if du not in prefinalfeature:
                prefinalfeature.append(nfpncr2[n6])
            n6 = n6 + 1
        for wa in prefinalfeature:
            prefinalfeaturel.append(wa.location)
            prefinalfeaturef.append(wa)
        for finalfeature in newfeaturesl:
            if finalfeature in prefinalfeaturel:
                newfeatures.remove(newfeaturesf[n7])
            n7 = n7 + 1
        for end in prefinalfeature:
            newfeatures.append(end)
        record.features = newfeatures        
        
        # Escribir la información de este record en el archivo .gbk
        # Cada record se va agregando al final del archivo
        with open(out_gbk,"w") as gbk_output:
            SeqIO.write(record,gbk_output,"gb")
            
# GFF SUBPRODUCT #
from BCBio import GFF
from Bio import SeqIO

in_file = "%s" % (out_gbk)
out_file = "Contannotate_" + "%s" % (gbkname) + ".gff"
in_handle = open(in_file)
out_handle = open(out_file, "w")

GFF.write(SeqIO.parse(in_handle, "genbank"), out_handle)

in_handle.close()
out_handle.close()       