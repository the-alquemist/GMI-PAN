#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 15:18:40 2021

@author: joaquin

PROJECT CODE < > CONTANNOTATE
"""
####################### MADE FOR PYTHON 3.6 #################################
import os
import subprocess
import sys                    
from Bio import SeqIO
from distutils.spawn import find_executable 

# PYTHON 3.6 : PROKKA (VFDB, ISFinder, BacMet, AuxDB, RelaxaseDB, T4SS),I-VIP,
# RGI,PlasmidVerify,PlasmidFinder,PhageBoost(downgrade xgboost to 1.3.3),nhmmer

print(" Welcome!This program will help you annotate bacterial genomes so\n \
make sure your input is a fasta file and all dependencies are installed.\n")

################################ (FORMAT) #####################################
fafile = sys.argv[1]          #### fafile as argument 1 ####
            
def is_fasta(filename):       #### function that checks file format ####
    with open(filename, "r") as handle:
        fasta = SeqIO.parse(handle, "fasta") 
        return any(fasta)

if not is_fasta(fafile):
    print(" This is not a fasta file.... closing program.")
    sys.exit(1)
else:
    print(" Fasta file confirmed.... executing program...\n")

###################### CREATE A BASENAME FOR FILE #############################
basename = fafile.split(".")[0]

################################ (PATHS) ######################################    
p1='/home/joaquin/anaconda3/envs/Contannotate2/plus_executables/plasmidverify.py'
p2='/home/joaquin/I-VIP.py'
p3='/home/joaquin/c_%s_raw_results' % (basename)
p4='/home/joaquin/Databases/VFDB_db/db_VFDB_prokka.fasta'
p6='/home/joaquin/Databases/oriTDB/auxiliary_all.fa'
p8='/home/joaquin/Databases/oriTDB/relaxase_all.fa'
p10='/home/joaquin/Databases/oriTDB/t4cp_all.fa'
p11='/home/joaquin/anaconda3/envs/Contannotate/plus_executables/plasmidverify.py'
p14='/home/joaquin/Databases/plasmidfinder_db'
p18='/home/joaquin/Databases/oriTDB/oriT_all.fa'
p19='/home/joaquin/Databases/bacmet_db/bacmet_db.fa'

def is_tool(name):
    """Check whether name is on PATH."""
    return find_executable(name) is not None

listasof = ['prokka','plasmidfinder.py','rgi', p1,'PhageBoost','nhmmer',p2]  

for software in listasof:
    if is_tool(software):
        print(" Checking %s: %s was correctly detected. \n" % (software, software))
    else:
        print(" Checking %s: ERROR: %s not found. \n" % (software, software))
        sys.exit(1)

################################TREE MAKING####################################
executionI= subprocess.run("mkdir c_%s_raw_results ; mkdir tmp ; cp *.fa /home/joaquin/tmp ; rm *.fa ; cp /home/joaquin/tmp/%s /home/joaquin/" \
                           % (basename,fafile), shell=True, stdout=subprocess.PIPE)
executionII = subprocess.run("touch /home/joaquin/c_%s_raw_results/nhmmer_%s.txt" %\
                             (basename, basename), shell=True, stdout=subprocess.PIPE)
executionIII = subprocess.run("mkdir /home/joaquin/c_%s_raw_results/PF_%s" %\
                             (basename, basename), shell=True, stdout=subprocess.PIPE)

###################### PROKKA VFDB RUN COMMAND ################################
execution0 = subprocess.run("prokka --outdir %s/PROKKAVF_%s --cpus 0 --mincontiglen \
                            300 --prefix %s --proteins %s /home/joaquin/%s"\
                            % (p3, basename, basename, p4, fafile), shell=True,\
                            stdout=subprocess.PIPE)
###################### PROKKA AUXDB RUN COMMAND ###############################
execution1 = subprocess.run("prokka --outdir %s/PROKKAAUX_%s --cpus 0 --mincontiglen \
                            300 --prefix %s --proteins %s /home/joaquin/%s"\
                            % (p3, basename, basename, p6, fafile), shell=True,\
                            stdout=subprocess.PIPE)
###################### PROKKA REDB RUN COMMAND ################################
execution2 = subprocess.run("prokka --outdir %s/PROKKARE_%s --cpus 0 --mincontiglen \
                            300 --prefix %s --proteins %s /home/joaquin/%s"\
                            % (p3, basename, basename, p8, fafile), shell=True,\
                            stdout=subprocess.PIPE)
###################### PROKKA T4CPDB RUN COMMAND ##############################
execution3 = subprocess.run("prokka --outdir %s/PROKKAT4CP_%s --cpus 0 --mincontiglen \
                            300 --prefix %s --proteins %s /home/joaquin/%s"\
                            % (p3, basename, basename, p10, fafile), shell=True,\
                            stdout=subprocess.PIPE)
###################### PROKKA BACMET RUN COMMAND ##############################
execution0 = subprocess.run("prokka --outdir %s/PROKKAMET_%s --cpus 0 --mincontiglen \
                            300 --prefix %s --proteins %s /home/joaquin/%s"\
                            % (p3, basename, basename, p19, fafile), shell=True,\
                            stdout=subprocess.PIPE)
###################### PLASMIDVERIFY RUN COMMAND ##############################
execution4 = subprocess.run("python3 %s -f /home/joaquin/%s -o %s/PV_%s \
                            --hmm /home/joaquin/Databases/Pfam-A.hmm" % \
                            (p11, fafile, p3, basename), shell=True, stdout=\
                            subprocess.PIPE)
###################### PLASMIDFINDER RUN COMMAND ##############################
execution5 = subprocess.run("plasmidfinder.py -x -i /home/joaquin/%s -o %s/PF_%s \
                            -d enterobacteriaceae -p %s -mp blastn -l 0.60 -t \
                            0.95" % (fafile, p3, basename, p14),\
                            shell=True, stdout=subprocess.PIPE)
############################# RGI RUN COMMAND #################################
execution6 = subprocess.run("rgi main -i /home/joaquin/%s -o %s/RGI_%s  --local \
                            --clean --data NA"\
                            % (fafile, p3, basename), shell=True, stdout=\
                            subprocess.PIPE)
############################# PHAGEBOOST RUN COMMAND ##########################
execution7 = subprocess.run("PhageBoost -f /home/joaquin/%s -o %s/PB_%s" % (fafile,\
                            p3, basename), shell=True, stdout=subprocess.PIPE)
############################# NHMMER RUN COMMAND ##############################
execution8 = subprocess.run("nhmmer --dna --cpu 100 --tblout %s/nhmmer_%s.txt \
                            %s /home/joaquin/%s" % (p3, basename, p18, fafile),\
                            shell=True, stdout=subprocess.PIPE)
############################# I-VIP RUN COMMAND ###############################
execution9b = subprocess.run("python3 I-VIP.py -i /home/joaquin/ -f .fa --o .faa \
                            --ot 1 --a Y --m 2 --t 10 --u None \
                            --r %s/IVIP_%s --tc None --tx None" % (p3, basename),\
                            shell=True, stdout=subprocess.PIPE)
    
############################### END OF ANALYSIS ###############################
executionIV = subprocess.run("rm *.fa.fai ; rm *.faa ; cp /home/joaquin/tmp/*.fa /home/joaquin/ ; rm -r tmp" \
                             , shell=True, stdout=subprocess.PIPE)

############################### TRIMMING PIPELINE #############################
executionV = subprocess.run("mkdir c_%s_final_results " %(basename),shell=True, stdout=subprocess.PIPE)
pfsize = os.path.getsize("/home/joaquin/c_%s_raw_results/PF_%s/results_tab.tsv" %(basename,basename))

if os.path.isfile("/home/joaquin/c_%s_raw_results/IVIP_%s/output/%s.Z.max.attc.hits.txt2.txt" %(basename,basename,fafile)):
    execution10 = subprocess.run("python3 /home/joaquin/Contannotate_executables/ivip_out_trimmer.py \
                                /home/joaquin/c_%s_raw_results/IVIP_%s/Integron/all.ORFs.fasta \
                                /home/joaquin/c_%s_raw_results/IVIP_%s/output/%s.Z.max.attc.hits.txt2.txt \
                                /home/joaquin/c_%s_raw_results/IVIP_%s/result/%s.Integron.txt" % \
                                (basename,basename,basename,basename,fafile,basename,basename,basename),shell=True, stdout=subprocess.PIPE)
    executionVI = subprocess.run("cp ivip_%s_results.txt /home/joaquin/c_%s_final_results ; rm ivip_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)

else:
    executionVI = subprocess.run("rm -r /home/joaquin/c_%s_raw_results/IVIP_%s" %(basename,basename),shell=True, stdout=subprocess.PIPE)
        
execution11 = subprocess.run("python3 /home/joaquin/Contannotate_executables/nhmmer_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/nhmmer_%s.txt" % \
                            (basename, basename),shell=True, stdout=subprocess.PIPE)
executionVII = subprocess.run("cp nhmmer_%s_results.txt /home/joaquin/c_%s_final_results ; rm nhmmer_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)
    
if os.path.exists("/home/joaquin/c_%s_raw_results/PB_%s" %(basename, basename)):
    execution12 = subprocess.run("python3 /home/joaquin/Contannotate_executables/phagebooster_out_trimmer.py \
                                /home/joaquin/c_%s_raw_results/PB_%s/phages_%s.gff" % \
                                (basename, basename,basename),shell=True, stdout=subprocess.PIPE)
    executionVIII = subprocess.run("cp phagebooster_%s_results.txt /home/joaquin/c_%s_final_results ; rm phagebooster_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)    
    
execution13 = subprocess.run("python3 /home/joaquin/Contannotate_executables/rgi_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/RGI_%s.txt" % \
                            (basename,basename),shell=True, stdout=subprocess.PIPE)
executionIX = subprocess.run("cp rgi_%s_results.txt /home/joaquin/c_%s_final_results ; rm rgi_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)    

if pfsize > 98:
    execution14 = subprocess.run("python3 /home/joaquin/Contannotate_executables/plasmidfinder_out_trimmer.py \
                                 /home/joaquin/c_%s_raw_results/PF_%s/results_tab.tsv" % \
                                (basename,basename),shell=True, stdout=subprocess.PIPE)
    executionX = subprocess.run("cp plasmidfinder_%s_results.txt /home/joaquin/c_%s_final_results ; rm plasmidfinder_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)

else:
    executionX = subprocess.run("rm -r /home/joaquin/c_%s_raw_results/PF_%s" %(basename,basename),shell=True, stdout=subprocess.PIPE)
    
execution15 = subprocess.run("python3 /home/joaquin/Contannotate_executables/prokkavf_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/PROKKAVF_%s/%s.gff" % \
                            (basename,basename,basename),shell=True, stdout=subprocess.PIPE)
executionXI = subprocess.run("cp prokkavf_%s_results.txt /home/joaquin/c_%s_final_results ; rm prokkavf_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)

execution16 = subprocess.run("python3 /home/joaquin/Contannotate_executables/prokkaaux_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/PROKKAAUX_%s/%s.gff" % \
                            (basename,basename,basename),shell=True, stdout=subprocess.PIPE)
executionXII = subprocess.run("cp prokkaaux_%s_results.txt /home/joaquin/c_%s_final_results ; rm prokkaaux_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)
    
execution17 = subprocess.run("python3 /home/joaquin/Contannotate_executables/prokkare_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/PROKKARE_%s/%s.gff" % \
                            (basename,basename,basename),shell=True, stdout=subprocess.PIPE)
executionXI = subprocess.run("cp prokkare_%s_results.txt /home/joaquin/c_%s_final_results ; rm prokkare_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)
    
execution18 = subprocess.run("python3 /home/joaquin/Contannotate_executables/prokkat4cp_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/PROKKAT4CP_%s/%s.gff" % \
                            (basename,basename,basename),shell=True, stdout=subprocess.PIPE)
executionXII = subprocess.run("cp prokkat4cp_%s_results.txt /home/joaquin/c_%s_final_results ; rm prokkat4cp_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)
    
execution19 = subprocess.run("python3 /home/joaquin/Contannotate_executables/prokkamet_out_trimmer.py \
                             /home/joaquin/c_%s_raw_results/PROKKAMET_%s/%s.gff" % \
                            (basename,basename,basename),shell=True, stdout=subprocess.PIPE)
executionXI = subprocess.run("cp prokkamet_%s_results.txt /home/joaquin/c_%s_final_results ; rm prokkamet_%s_results.txt"%(basename,basename,basename),shell=True, stdout=subprocess.PIPE)

################################# GBK MAKER ###################################  
execution20 = subprocess.run("python3 /home/joaquin/Contannotate_executables/gbk_maker.py \
                             -iv /home/joaquin/c_%s_final_results/ivip_%s_results.txt \
                             -nh /home/joaquin/c_%s_final_results/nhmmer_%s_results.txt \
                             -pf /home/joaquin/c_%s_final_results/plasmidfinder_%s_results.txt \
                             -pb /home/joaquin/c_%s_final_results/phagebooster_%s_results.txt \
                             -rg /home/joaquin/c_%s_final_results/rgi_%s_results.txt \
                             -pv /home/joaquin/c_%s_raw_results/PV_%s/%s_result_table.csv \
                             -prvf /home/joaquin/c_%s_final_results/prokkavf_%s_results.txt \
                             -prau /home/joaquin/c_%s_final_results/prokkaaux_%s_results.txt \
                             -prar /home/joaquin/c_%s_final_results/prokkare_%s_results.txt \
                             -prt4 /home/joaquin/c_%s_final_results/prokkat4cp_%s_results.txt \
                             -prme /home/joaquin/c_%s_final_results/prokkamet_%s_results.txt \
                             -i /home/joaquin/%s" %(basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,basename,fafile),shell=True, stdout=subprocess.PIPE)

################################# CLEANHOUSE ##################################
nhmmers = os.path.getsize("/home/joaquin/c_%s_final_results/nhmmer_%s_results.txt"%(basename,basename))
rgis = os.path.getsize("/home/joaquin/c_%s_final_results/rgi_%s_results.txt"%(basename,basename))

if nhmmers == 27:
    execution1r = subprocess.run("rm -r /home/joaquin/c_%s_final_results/nhmmer_%s_results.txt" %(basename,basename),shell=True, stdout=subprocess.PIPE)

if rgis == 27:
    execution2r = subprocess.run("rm -r /home/joaquin/c_%s_final_results/rgi_%s_results.txt" %(basename,basename),shell=True, stdout=subprocess.PIPE)
                                   
executionXII = subprocess.run("mkdir Contannotate_Final_Results",shell=True, stdout=subprocess.PIPE)
executionXIII = subprocess.run("cp -r c_%s_raw_results /home/joaquin/Contannotate_Final_Results ; rm -r c_%s_raw_results"%(basename,basename),shell=True, stdout=subprocess.PIPE)
executionXIV = subprocess.run("cp -r c_%s_final_results /home/joaquin/Contannotate_Final_Results ; rm -r c_%s_final_results"%(basename,basename),shell=True, stdout=subprocess.PIPE)
executionXV = subprocess.run("cp -r Contannotate_%s.gbk /home/joaquin/Contannotate_Final_Results ; rm -r Contannotate_%s.gbk"%(basename,basename),shell=True, stdout=subprocess.PIPE)
executionXVI = subprocess.run("cp -r Contannotate_%s.gff /home/joaquin/Contannotate_Final_Results ; rm -r Contannotate_%s.gff"%(basename,basename),shell=True, stdout=subprocess.PIPE)
