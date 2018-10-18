# Xiaoli Sky Wu
# 2018/10/17
# add backbone and produce reverse complementary sequence for sgRNA

import sys

####################################################################################
# help information 
if '-h' in sys.argv or 'help' in sys.argv:
	print('Usage of the script: python add_backone.py your_input_file_name')
	print()
	print('After typing python and space, you can drag the script into terminal, and then hit space again, you can now drag your input file into terminal and hit Enter.')
	print('With this method you do not have to specify absolute path of your files')
	print()
	print('Your input file should be: geneName\tsgRNAsequence')
	exit()
####################################################################################

################################################################
# producing reverse complement sequence for sgRNA
def reverse_complement(sgRNA_sequence):
	seq = sgRNA_sequence[::-1]
	rev_seq = ''
	for nucleotide in seq:
		rev_seq += seq_dict[nucleotide]
	return rev_seq
################################################################


###############################################################
# read input file name 
fileName = sys.argv[1]

# error message for not putting input file name
if len(fileName) < 1:
	print('You forget to specify your input file name')
############################################################


################################################################
# create output file based on input file name
inputFile = open(fileName,'r')
outputFile = open(fileName.split('.txt')[0]+'_output.txt','w')

# customize sgRNA name
count = 0 
gene_name = ''
seq_dict = {'A':'T','C':'G','T':'A','G':'C'}


# read in the sequence information and produce output
for line in inputFile:
	line = line.strip('\n').split('\t')

	# error message for wrong input format
	if len(line) < 2:
		print('Your input file has wrong format')
		print('right input format: geneName/tsgRNAsequence/n')
		break

	# store the gene name as well as sgRNA sequence
	new_name,sgRNA_seq = line[0],line[-1]	

	# error message for wrong input format
	nucleotides = set(sgRNA_seq)
	for nucleotide in nucleotides:
		if not nucleotide.upper() in seq_dict.keys():
			print('the last item in your line is not a sgRNA sequence!')
			break

	sgRNA_seq = sgRNA_seq.upper()

	# if the gene name has changed, restart the number
	if gene_name == new_name:
		count += 1
	else:
		gene_name = new_name
		count = 1


	sgRNA_name = gene_name + '_sg' + str(count) 

	rev_seq = reverse_complement(sgRNA_seq)

	# add backbones to the sgRNAs
	if sgRNA_seq.startswith('G'):
		sgRNA_seq = 'CACC' + sgRNA_seq
	else:
		sgRNA_seq = 'CACCG' + sgRNA_seq
	if rev_seq.endswith('C'):
		rev_seq = 'AAAC' + rev_seq
	else:
		rev_seq = 'AAAC' + rev_seq + 'C'


	# write information to output file
	outputFile.write(sgRNA_name +'_For\t\t'+sgRNA_seq+'\n')
	outputFile.write(sgRNA_name +'_Rev\t\t'+rev_seq+'\n')

outputFile.close()
print('All Done!')
###############################################################


