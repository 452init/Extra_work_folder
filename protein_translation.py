#!/usr/bin/env python3
import time
import timeit
from itertools import takewhile

STRAND = 'UUUUUCUUAUUGCUUCUCCUACUGAUUCGTCGCCGACGGAGAAGGAATAACGATGACAATAACGATGACTGTTGCCAACAGGAAGAGGGTGGCGGAGGGGTTGTCGTAGTGTCTTCCTCATCGAGTTAATGATAGCTTCTCCTACTGTTATTG'

RNA_SEQUENCE = {
		'AUG': 'Methionine',
		'UGG': 'Tryptophan',
		'UUU': 'Phenylalanine',
		'UUC': 'Phenylalanine',
		'UUA': 'Leucine',
		'UUG': 'Leucine',
		'UCU': 'Serine',
		'UCG': 'Serine',
		'UCA': 'Serine',
		'UCC': 'Serine',
		'UAU': 'Tyrosine',
		'UAC': 'Tyrosine',
		'UGU': 'Cysteine',
		'UGC': 'Cysteine',
		}

stop_codon = {'UAG', 'UGA', 'UAA'}

def protein_generator(strand: str) -> list:
	for i in range(0, len(strand), 3):
		codon = strand[i:i+3]
		if codon in stop_codon:
			return
		if codon in RNA_SEQUENCE:
			yield RNA_SEQUENCE[codon]
#result_list = list(protein_generator(STRAND))



	#codon = [strand[x:x+3] for x in range(0, len(strand), 3)]

	#valid_codons = takewhile(
	#lambda codon: codon not in stop_codon and codon in RNA_SEQUENCE, codon
	#)

	#protein_name = [RNA_SEQUENCE[codon] for codon in valid_codons]


	#stop_codons = {key for key, value in RNA_SEQUENCE.items() if value == 'STOP'}
	#codons = []
	#protein_name = []
	#for x in range(0, len(strand), 3): # loops over the strands in steps of 3
	#	codons = strand[x:x+3]
	#	if codons in stop_codons:
	#		break
	#	elif codons in RNA_SEQUENCE:
	#		protein_name.append(RNA_SEQUENCE[codons])

	#return protein_name

if __name__ == '__main__':

	# --- Time a single run with high-resolution clock ---
	start = time.perf_counter()
	result_one = list(protein_generator(STRAND))
	end = time.perf_counter()
	single_elapsed = end - start



	print("Result of a single run:", result_one)
	print(f"Time for a single run: {single_elapsed:.9f} seconds")

	# --- Time many runs with timeit (measure average) ---
	# Choose a number that completes in a reasonable time on your machine.
	number = 100_000  # try 100k first; reduce if that takes too long
	total_time = timeit.timeit(lambda: list(protein_generator(STRAND)), number=number)

	print(f"\nTotal time for {number:,} runs: {total_time:.6f} seconds")
	print(f"Average time per run: {total_time/number:.9f} seconds")
