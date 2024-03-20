# GMI-PAN: A bacterial plasmid annotation pipeline

## Update 03/20/24: Oh, you made it here! Thanks for your interest, I haven't made an annoucement yet but now I'm working as a bioinformatician and learned a lot after my thesis, so I'm sorry for my lack of programming etiquette back then. This first iteration of GMI-PAN will be improved in my free time so stay tuned!. Files appended here are product and evidence of a first functional iteration of GMI-PAN that is part of my thesis defense to obtain the professional academic grade in the Molecular Biotechnology Engineer career. Thanks to *BEM* and *GMI* for giving me the knowledge and space to work on this.

## What is this about?

The emergence of antibiotic resistance is a natural occurrence in microorganisms, but its prevalence in clinically significant strains has been accelerated due to the excessive use of antibiotics in humans and farm animals. The indiscriminate use of antibiotics has been identified as a key factor in the development of multidrug resistance, driven by selective pressure from an ecological perspective.

In this repository, I developed a bioinformatics tool called *"GMI-PAN"*, for the evaluation and annotation of antibiotic and metal resistance profiles, virulence factors, and mobile genetic elements in assembled nucleotide sequences of prokaryotic nature, optimized for the *Enterobacteriaceae* family. This tool, better known as a wrapper, allows for the automation of an annotation pipeline that integrates various previously developed tools, significantly reducing the time required for work and providing an in deph picture of the MDR resistance context in these organisms.

![pipeline](/Supplementary_Data/figura1.png)

## Dependencies
1. Python 3.6.13
1. PROKKA 1.14.6
1. RGI 5.2.1
1. PlasmidVerify
1. PlasmidFinder
1. PhageBoost 0.1.7 (xgboost 1.3.3)
1. I-VIP
1. NHMMER 3.3.2
1. bcbio-gff 0.6.9

## Installation & Usage

Coming soon...

## Colaborations

### Population genomics, resistance, pathogenic potential, and mobile genetic elements of carbapenem-resistant Klebsiella pneumoniae causing infections in Chile
*GMI-PAN* was used in this study as an annotation tool for the analysis of plasmids encoding carbapenemases and other resistance determinants. Please take a look at the results! https://doi.org/10.1128/spectrum.00399-23

## Special thanks!

*GMI-PAN* was currently based on annotation modules such as *PROKKA*, *PlasmidVerify*, *PlasmidFinder*, *RGI*, *PhageBoost*, *NHMMER* and *IVIP*. Thanks to the respective or respectives authors for their amazing contributions and please checkout their work!

1. *PROKKA*: https://github.com/tseemann/prokka
1. *RGI*: https://github.com/arpcard/rgi/releases
1. *I-VIP*: https://github.com/caozhichongchong/I-VIP
1. *PlasmidFinder*: https://bitbucket.org/genomicepidemiology/plasmidfinder/src/master/
1. *PlasmidVerify*: https://github.com/ablab/plasmidVerify
1. *PhageBoost*: https://github.com/ku-cbd/PhageBoost
1. *NHMMER*: https://github.com/EddyRivasLab/hmmer

## Author

- Joaquín Acosta
- eMAIL: joaquin.acosta@ug.uchile.cl

![logo](/miscellaneous/bem_long.png)
