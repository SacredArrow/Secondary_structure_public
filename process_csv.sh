read -p "Enter archive prefix (Like 'set_600'): " Prefix
echo
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
echo Fasta for validate... # Generate only fastas for parsing
python3 ./Scripts/only_sequences_for_parsing.py "$script_path/sample_validate.txt" > validate.fasta
echo Fasta for test...
python3 ./Scripts/only_sequences_for_parsing.py "$script_path/sample_test.txt" > test.fasta
echo Fasta for train...
python3 ./Scripts/only_sequences_for_parsing.py "$script_path/sample_train.txt" > train.fasta
echo Cleaning folders... # Clean-up of old pictures
cd sets
rm -r test/
rm -r train/
rm -r validate/
mkdir test; mkdir train; mkdir validate;
echo Moving samples...
mv ../sample_validate.txt ./validate/sample_validate.txt
mv ../sample_test.txt ./test/sample_test.txt
mv ../sample_train.txt ./train/sample_train.txt
echo Running dot2img... # Generating pictures
python3 $ToImg ./test/sample_test.txt ./test
python3 $ToImg ./train/sample_train.txt ./train
python3 $ToImg ./validate/sample_validate.txt ./validate
echo Zipping... # Zip all files and fastas in separate archives
zip -r "${Prefix}_pics.zip" test train validate ../validate.csv ../train.csv ../test.csv > /dev/null
cd ..
zip "${Prefix}_fastas.zip" validate.fasta train.fasta test.fasta > /dev/null
echo Done!
