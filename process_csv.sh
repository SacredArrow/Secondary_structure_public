echo "Enter archive prefix. (Like 'set_600')"
read Prefix
echo "Enter name of 2img program. (Like dot2img.py)"
read ToImg

echo Starting sample picking...
python3 sample_picker.py # Picks desired sequences based on 3 .csv files
echo Samples picked.
echo Fasta for validate... # Generate only fastas for parsing
python3 only_sequences_for_parsing.py sample_validate.txt > validate.fasta
echo Fasta for test...
python3 only_sequences_for_parsing.py sample_test.txt > test.fasta
echo Fasta for train...
python3 only_sequences_for_parsing.py sample_train.txt > train.fasta
echo Cleaning folders... # Clean-up of old pictures
cd sets
rm test/*
rm train/*
rm validate/*
echo Moving samples...
mv ../sample_validate.txt ./validate/sample_validate.txt
mv ../sample_test.txt ./test/sample_test.txt
mv ../sample_train.txt ./train/sample_train.txt
echo Running dot2img... # Generating pictures
python3 $ToImg ./test/sample_test.txt ./test
python3 $ToImg ./train/sample_train.txt ./train
python3 $ToImg ./validate/sample_validate.txt ./validate
echo Zipping... # Zip all files
zip -r "${Prefix}_pics.zip" test train validate ../validate.csv ../train.csv ../test.csv > /dev/null
cd ..
zip "${Prefix}_fastas.zip" validate.fasta train.fasta test.fasta > /dev/null
echo Done!
