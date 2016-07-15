#!/usr/bin/python

import csv
from os import listdir
from os.path import isfile, join

def countAminoAcid(aminoAcid,genomSequence):
	total = 0
	index = 0
	while index < len(genomSequence):
		if(genomSequence[index]==aminoAcid):
			total=total+1
		index=index+1
	return total

def generateFlastaaArray(str):
	amino_acids = ['A','R','N','D','C','E','Q','G','H','I','L','K','M','F','P','S','T','W','Y','V']
	genome_keys = []
	index = str.find('&gt;',0,len(str))
	last_index = str.rfind('</PRE>',0,len(str))
	for flastaa in str[index:last_index].split('&gt;'):
		genomes = flastaa.split('\r\n')
		#print genomes
		if len(genomes) > 1:
			genome_name = genomes[0].strip()
			genome_sequence = ''.join(genomes[1:])
			genome_key = (genome_name, genome_sequence)
			genome_keys.append(genome_key)
	#print genome_keys
	#
	# Create CSV File
	with open('csv_files/genome.csv', 'w') as csvfile:
		fieldnames = ['GENOME NAME','GENOME LENGTH'] + amino_acids + ['GENOME SEQUENCE']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for gen_nm, gen_seq in genome_keys:
			percentages = {}
			for amino_acid in amino_acids:
				percentage = (float(countAminoAcid(amino_acid,gen_seq))/len(gen_seq))*100
				#percentage = countAminoAcid(amino_acid,gen_seq)
				percentages[amino_acid] = percentage
			y={}
			x={'GENOME NAME': gen_nm, 'GENOME LENGTH':len(gen_seq) ,'GENOME SEQUENCE': gen_seq}
			y=x.copy()
			y.update(percentages)
			writer.writerow(y)


	
	
def processFile(fileName):
	f = open(fileName, 'r')
	str = f.read()
	generateFlastaaArray(str)
	#print str

## Main Section
mypath = 'flastaa/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for fileName in onlyfiles: 
	processFile(mypath + fileName)
