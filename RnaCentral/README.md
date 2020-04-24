

### Workflow

To prepare data downloaded from RnaCentral site following steps are reqired:
1. Acquire secondary structure, for example, with centroidFold: `centroid_fold RNA_AND_length90_TO_90.fasta > centroid_central_90_70K.txt`
2. Run merging script: `python3 merge_fasta_and_centroid.py RNA_AND_length90_TO_90.fasta centroid_central_90_70K.txt > RNA_CEN.txt`
3. Move to RNA_banks folder with name `RNA_CEN.txt` : `mv RNA_CEN.txt ../RNA_banks/RNA_CEN.txt`


|  File/Folder |  Description |  Example |
| ------------ | ------------ | ------------ |
|merge_fasta_and_centroid.py   | Merges file and centroid_fold result to bank file.   |  See above |
|central_api_crawler.py   | Uses RNACentral API. Is useful, when there is no ability to download from site directly. Not recommended in general  | `python3 central_api_crawler.py`  |
| seqs_to_fasta.py  | Converts crawler result to fasta file.  | `python3 seqs_to_fasta.py `  |
| sec_to_RNA_file.py | Merges secondary structure and crawling result. | `python3 sec_to_RNA_file.py ` |
