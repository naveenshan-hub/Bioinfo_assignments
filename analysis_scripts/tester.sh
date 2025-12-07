#!/bin/bash
# change to raw_data directory to get the sample files
cd raw_data || exit
# loop through the files that matches the given pattern
for file in sample*_part1.FASTQ;do
  base=${file%_part1.FASTQ} # get the base name only by removing _part1.FASTQ part
  cat ${base}_part*.FASTQ | # concatenate all split samples respect to their parts
  #  add new lines after each @ and remove repeated headers and get combined FASTQ files
  sed 's/@/\n@/g'| awk 'NF{ if (/^@/) { if ($0==last_header) next; last_header=$0}
 print}'> ${base}_combined.FASTQ
# converting FASTQ -> fasta 
# convert @ to > and print 1st and 2nd lines  i.e. the header & Sequences 
  awk 'NR%4==1 {sub(/^@/,">"); print} NR%4==2 {print}' "${base}_combined.FASTQ"> "${base}.fasta"
rm -f *_combined.FASTQ  # removed the combined FASTQ files which is not required
done
rm -f *clean.fasta # remove any existing files in this name 
# processing each fasta files
for file in sample*.fasta;do
  base=${file%.fasta} 
# skip the headers, remove spaces in between the sequences and concatenate the result sequences and print it 
  awk -v base="$base" '/^>/ {next} {gsub (/ /,""); seq = seq $0} END {print ">" base; print seq}' "$file" >> "${base}clean.fasta"
done
cd "C:\Users\offic\BIF\Bioinformatics_assignment" # moving into main directory
mkdir -p cleaned_data # create a new folder for saving the clean fasta sequences
mv raw_data/*clean.fasta cleaned_data/  # move fasta files from raw_data to cleaned_data folder
echo "fasta files are saved in cleaned_data folder" 



