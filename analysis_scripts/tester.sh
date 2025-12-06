#!/bin/bash
for file in sample*_part1.FASTQ;do
  base=${file%_part1.FASTQ}
  cat ${base}_part*.FASTQ |
  sed 's/@/\n@/g'| awk 'NF{ if (/^@/) { if ($0==last_header) next; last_header=$0} print}'> ${base}_combined.FASTQ
  awk 'NR%4==1 {sub(/^@/,">"); print} NR%4==2 {print}' "${base}_combined.FASTQ"> "${base}.fasta"
rm -f *_combined.FASTQ
done
rm -f *clean.fasta
for file in sample*.fasta;do
  base=${file%.fasta}
  awk -v base=$base '/^>/ {next} {gsub (/ /,""); seq = seq $0} END {print ">" base; print seq}' "$file" >> "${base}clean.fasta"
done
echo "fasta file is ready"
