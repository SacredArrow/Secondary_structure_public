### What is this?

The repository contains scripts that are used to handle data for my course project in SPbU/Bioinformatics Institute.

- [Goals of the project](#goals)
- [Description and examples](#description)
- [Links](#links)

<a name="goals"/>  

### Goals of the project

The project is aimed to develop an efficient way of RNA secondary structure prediction including pseudoknots. The data is processed using scripts in this repository, then it is used to  teach a neural network to predict secondary structure based on primary structure of RNA.  

<a name="description"/>

### Description and examples

To prepare data following steps are done:
1. Databases are collected in RNA_xxx.txt files.
2. `csv_builder.py` is run, making one .csv file.  
2a (Optional). Data is manually processed in `Notebook.ipynb`.
3. `./process_csv.sh` is run, shuffling them into 3 sets, making pictures from them and zipping them together.


|  File/Folder |  Description |  Example |
| ------------ | ------------ | ------------ |
|process_csv.sh   | Main script, containg whole workflow. Gets a csv (see `notebook_script.py`), shuffles it info 3 sets, creates 3 samples, makes pics and zips everything into 2 sets - with pics and with fastas.   |  `./process_csv.sh` |
|notebook_script.py   | Takes csv and shuffles in into 3 sets - train, test and validate. Is only used for `process_csv.sh`, because for elaborate analysis `Notebook.ipynb` is used.  | `python3 notebook_script.py`  |
| Notebook.ipynb  | Jupyter notebook, containing different code blocks for analysis and processing of csv files.  |   |
| Sets/ | This directory usually contains zipped pics and fastas. It also contains 3 folders with .png pictures, that are used for ML - test, train and validate.| |
|Sets/dot2img.py| Script for making .png pics from sample_xxx.txt files.| `python3 dot2img.py`|
|  Scripts/ | A bunch of scripts used for data manipulation. For more info see README.md inside the folder.  |   |
| RnaCentral/   | Scripts used to work with data extracted from RNACentral database.   |   |
| Playground/  | Some auxiliary scripts.  |   |

<a name="links"/>

### Links
- https://rnacentral.org/ - big RNA database without secondary structures, that was used to get data.
- http://www.rnasoft.ca/strand/ - Database with secondary structures.
- http://pseudobaseplusplus.utep.edu/ - Small database containing secondary structures with pseudoknots.
