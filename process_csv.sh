echo Starting sample picking...
python3 sample_picker.py
echo Samples picked.
echo Fasta for validate...
python3 only_sequences_for_parsing.py sample_validate.txt > validate.fasta
echo Fasta for test...
python3 only_sequences_for_parsing.py sample_test.txt > test.fasta
echo Fasta for train...
python3 only_sequences_for_parsing.py sample_train.txt > train.fasta
echo Cleaning folders...
cd sets
pwd
rm test/*
rm train/*
rm validate/*
echo Moving samples...
mv ../sample_validate.txt ./validate/sample_validate.txt
mv ../sample_test.txt ./test/sample_test.txt
mv ../sample_train.txt ./train/sample_train.txt
echo Running dot2img...
python3 dot2img.py ./test/sample_test.txt ./test
python3 dot2img.py ./train/sample_train.txt ./train
python3 dot2img.py ./validate/sample_validate.txt ./validate
echo Done!
