
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO

fasta_file = r"C:\Users\offic\bash_practice\sequences\samples\for_translation.fasta"
sequences = list(SeqIO.parse(fasta_file, "fasta"))

print("number of sequences:", len(sequences))


aa_sequences = []

for record in sequences:
    dna_seq = record.seq
    best_orf = ""
    best_frame = None

    for frame in range(3):
        protein = dna_seq[frame:].translate(to_stop=False)
        fragments = str(protein).split("*")
        longest_in_frame = max(fragments, key=len)

        if len(longest_in_frame) > len(best_orf):
            best_orf = longest_in_frame
            best_frame = frame

    best_protein = Seq(best_orf)

    des_words = record.description.split()
    scientific_name = "_".join(des_words[1:3])
    new_id = f"{record.id}_{scientific_name}"

    aa_record = SeqRecord(
        best_protein,
        id=new_id,
        description=""
    )
    aa_sequences.append(aa_record)


output_file = r"C:\Users\offic\bash_practice\sequences\samples\translated.fasta"
SeqIO.write(aa_sequences, output_file, "fasta")
print("Translated proteins saved to:", output_file)
