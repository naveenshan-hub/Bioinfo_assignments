# import required objects from biopython
from Bio.Seq import Seq  # takes care of DNA sequence objects
from Bio.SeqRecord import SeqRecord  # stores ID and description
from Bio import SeqIO  # reads and writes fasta
# input the required fasta file
fasta_file = r"C:\Users\offic\BIF\Bioinformatics_assignment\results\for_translation.fasta"
# reads all the sequences from input and stores it in seqeecord objects
sequences = list(SeqIO.parse(fasta_file, "fasta"))

# just to make sure of all the reference and sample sequences are taken in
print("number of sequences:", len(sequences))

aa_sequences = []  # an empty list to store protein sequences after translation
# looping through each sequences
for record in sequences:
    dna_seq = record.seq  # extract the sequneces
    best_orf = ""  # variables to keep best orf record
    best_frame = None
# check translation in all three forward reading frames
    for frame in range(3):
        protein = dna_seq[frame:].translate(
            to_stop=False)  # trasnlate from this frame
        # split translation into fragments seperated by stop codons
        fragments = str(protein).split("*")
        # select longest fragment as longest orf in that frame
        longest_in_frame = max(fragments, key=len)
# keep the best longest orf among all frames
        if len(longest_in_frame) > len(best_orf):
            best_orf = longest_in_frame
            best_frame = frame
# convert selected protein sequence into seq object
    best_protein = Seq(best_orf)
# create clean sequence ID
    des_words = record.description.split()
    # get the genus and species name
    scientific_name = "_".join(des_words[1:3])
    new_id = f"{record.id}_{scientific_name}"
# create a new seqrecord for translated protein
    aa_record = SeqRecord(
        best_protein,  # amino acid sequence
        id=new_id,  # new ID
        description=""  # remove unwanted descriptions
    )
    # add the output sequence to the output list
    aa_sequences.append(aa_record)
# save all translated proteins into a fasta file
output_file = r"C:\Users\offic\BIF\Bioinformatics_assignment\results\translated.fasta"
SeqIO.write(aa_sequences, output_file, "fasta")
# this message pops after the whole process is complete
print("Translated proteins saved to:", output_file)
