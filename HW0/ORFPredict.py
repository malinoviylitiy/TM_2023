#!/bin/python3
from Bio import SeqIO

# Reading FASTA-file
input_fasta_file = "lacZ.fna"
output_bed_file = "ORFPredictOutput.bed"

# Minimal ORF lenght
min_orf_length = 100  

with open(output_bed_file, "w") as bed_file:
    for record in SeqIO.parse(input_fasta_file, "fasta"):
        dna_sequence = record.seq

        # Looking for all ORFs
        orfs = []
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]

        for frame in range(3):
            for i in range(frame, len(dna_sequence) - 2, 3):
                codon = dna_sequence[i:i + 3]
                if codon == start_codon:
                    end = None
                    for j in range(i + 3, len(dna_sequence) - 2, 3):
                        codon = dna_sequence[j:j + 3]
                        if codon in stop_codons:
                            end = j + 3
                            break
                    if end is not None and end - i >= min_orf_length:
                        orfs.append((i, end))

        # Creating BED-file
        for i, end in orfs:
            bed_file.write(f"{record.id}\t{i}\t{end}\tORF\t0\t+\n")

print(f"The informaition about the ORFs saved in {output_bed_file}")
