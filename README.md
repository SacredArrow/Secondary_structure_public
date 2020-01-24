### What is this?

The repository contains scripts that are used to handle data for my course project in SPbU/Bioinformatics Institute.

[TOC]

### Goals of the project

The project is aimed to develop an efficient way of RNA secondary structure prediction including pseudoknots. The data is processed using scripts in this repository, then it is used to  teach a neural network to predict secondary structure based on primary structure of RNA.

### Description and examples
|  File/Folder |  Description |  Example |
| ------------ | ------------ | ------------ |
|process_csv.sh   | Main script, containg whole workflow. Gets a csv(see `notebook_script.py`, shuffles it info 3 sets, creates 3 samples, makes pics and zips everything into 2 sets - with pics and with fastas   |  `./process_csv.sh` |
|notebook_script.py   | Takes csv and shuffles in into 3 sets - train, test and validate. Is only used for `process_csv.sh`, because for elaborate analysis `Notebook.ipynb` is used  | `python3 notebook_script.py`  |
| Untitled.ipynb  | Jupyter notebook, containing different code blocks to analisys and processing of csv files  |   |
|sets/dot2img.py| Script for making .pdf pics from sample_xxx.txt files| `python3 dot2img.py`|
|  Scripts/ | A bunch of scripts used to data manipulation. For more info see README.md inside the folder  |   |
| RnaCentral/   | Scripts used to work with data extracted from RNACentral database   |   |
| playground/  | Some auxiliary scripts  |   |

### Links
- https://rnacentral.org/
- http://www.rnasoft.ca/strand/
- http://pseudobaseplusplus.utep.edu/
