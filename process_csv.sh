read -p "Enter archive prefix (Like 'set_600'): " Prefix
# echo
read -p "Enter name of 2img program [dot2img.py]: " ToImg
ToImg=${ToImg:-dot2img.py}
read -p "Automate csv creation? Yes/No [Yes]" Automate
Automate=${Automate:-Yes}
if [ "$Automate" = "Yes" ]; then
  echo "Shuffling file"
  python3 notebook_script.py
fi

script_path="$(realpath $(dirname "$0"))"
cd $script_path # For paths to work (scripts require full path anyway)
echo Starting sample picking...
python3 ./Scripts/sample_picker.py $script_path $script_path "$script_path/RNA_banks" # Picks desired sequences based on 3 .csv files
echo Samples picked.
echo Fasta for validate set... # Generate only fastas for parsing
python3 ./Scripts/only_sequences_for_parsing.py "$script_path/sample_valid.txt" > valid.fasta
echo Fasta for test...
python3 ./Scripts/only_sequences_for_parsing.py "$script_path/sample_test.txt" > test.fasta
echo Fasta for train...
python3 ./Scripts/only_sequences_for_parsing.py "$script_path/sample_train.txt" > train.fasta
echo Cleaning folders... # Clean-up of old pictures
cd Sets
rm -r test/
rm -r train/
rm -r valid/
mkdir test; mkdir train; mkdir valid;
echo Moving samples...
mv ../sample_valid.txt ./valid/sample_valid.txt
mv ../sample_test.txt ./test/sample_test.txt
mv ../sample_train.txt ./train/sample_train.txt
echo Running dot2img... # Generating pictures
python3 $ToImg ./test/sample_test.txt ./test
python3 $ToImg ./train/sample_train.txt ./train
python3 $ToImg ./valid/sample_valid.txt ./valid
echo Zipping... # Zip all files and fastas in separate archives
zip -r "${Prefix}_pics.zip" test train valid ../valid.csv ../train.csv ../test.csv > /dev/null
zip "${Prefix}_fastas.zip" ../valid.fasta ../train.fasta ../test.fasta > /dev/null
cd ..
echo Done!
