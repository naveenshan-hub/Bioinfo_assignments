# **Project: Identifying undocumented frozen meat samples**

# 

## **Overview:**

**This project aims to identify the Undocumented meat samples, which raises the concern that the samples could belong to protected species. We have been provided with FASTA sequences from DNA barcoding and now have to carry out the further analysis.** 



## **Description:**

**This repository contains scripts and data for analysing the sample sequences.** 

**It contains:** 

      **> Sample sequences in FASTQ format**

      **> Script to process FASTQ into a FASTA file**

      **> Reference sequences obtained from NCBI-BLAST**

      **> Scripts to translate the nucleotide sequences into protein sequences**



## **Repository Structure:**

* **analysis\_scripts: contains tester.sh and aa\_conversion.py scripts**
* **raw\_data: contains FASTQ files of our samples and unclean fasta files**
* **cleaned\_data: contains clean fasta files and reference sequences** 
* **results: contains concatenated fasta files for translation, translated fasta files, phylogenetic tree, multiple sequence alignment, and Jalview alignment image.**

## **Prerequisites:**

* **Git Bash**
* **Python 3.x**
* **Biopython ('pip install biopython')**
* **Basic knowledge of NCBI-BLAST and MSA tools**

## **Instructions:**

> Step 1: Convert FASTQ to fasta

* **log into the appropriate working directory**
* **Run the shell script to convert the FASTQ files into fasta files**
* **The clean fasta files are now saved into cleaned\_data folder**

> Step 2: Obtain Reference Sequences

* **Run NCBI-BLAST against our clean fasta files and select the reference sequences (max 5)** 
* **Concatenate the reference sequences and clean fasta files of our samples in Gitbash** 
* **Save the file as "for\_translation.fasta" in results folder** 

> Step 3: Translate Nucleotide sequences to Amino Acid sequences

* **Run the python script for the "for\_translation.fasta" file**
* **The script saves the translated files as "translated.fasta" in the results folder**

> Step 4: Multiple Sequence Alignment & Phylogenetic Tree

* **Use the "translated.fasta" to perform Multiple Sequence Alignment (MSA)**
* **In our case I used "https://www.ebi.ac.uk/jdispatcher/msa/clustalo" for MSA and building a Phylogenetic trees.**
* **Save the alignment file and phylogenetic tree in results folder.** 

> Interpreting Results

* Phylogenetic tree distances indicate evolutionary relatedness
* Samples clustering with known reference sequences suggest species identity



      



