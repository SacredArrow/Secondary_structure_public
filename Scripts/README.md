|  File/Folder |  Description |  Example |
| ------------ | ------------ | ------------ |
|PKB_changer.py| PKB base (from PseudoBase++) has unusual format, so needs to by unified.|`python3 PKB_changer.py`|
|aligner.py|Auxiliary script to view PKB sequences.| `python3 aligner.py`|
|counter.py| Small auxiliary script to count number of sequences in the file.| `python3 counter.py`|
|crawler.py| Crawler/parser for RNAStrand database.| `python3 crawler.py`|
|csv_builder.py| Makes one .csv file from RNA_xxx.txt files.| `python3 csv_builder.py > out_50_90.csv`|
|filter_sorter.py| Deprecated file used to work with external tools.| `python3 filter_sorter.py   `|
|only_sequences_for_parsing.py| Makes fastas from sample_xxx.txt files (those are picked after distribution into 3 sets). | `python3 only_sequences_for_parsing.py sample_test.txt > test.fasta`|
|sample_picker.py| Picks sequences into sample_xxx.txt files using .csv files and database files.| `python3 sample_picker.py . . ./RNA_banks`|
|stem_generator.py| Script to artificially create sequences with stem loops.|`python3 python3 stem_generator.py 8 90 100 --stem_number 4 > debug.txt`|
