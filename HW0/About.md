### ORFPredict.py - a script designed to identify Open Reading Frames (ORFs) in a DNA sequence 

This program performs the following tasks:

1. Reads a DNA sequence from a FASTA file.
2. Determines the minimum length of ORFs to consider, specified as "min_orf_length".
3. Searches for all ORFs within the DNA sequence, starting from the start codon "ATG" and ending with one of the stop codons ("TAA", "TAG", "TGA").
4. Records information about the identified ORFs into a BED file named "ORFPredictOutput.bed". Each entry in the file includes the following columns: record identifier, ORF start position, ORF end position, feature name (ORF), count (0), and orientation (+).

To test the program, you can use a DNA sequence, such as the gene lacZ, obtained from NCBI and saved in a FASTA file named "lacZ.fna."