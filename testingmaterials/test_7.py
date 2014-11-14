#Stop if the exon has length <2 bases?
##ADD INTO THE FOLLOWING FUNCTION THE LINES WHICH I HAVE COMMENTED AFTER

sequence =  'ACGTACGTACGTACGTACGTACGTACGTACGT' #####We don't need this stuff, I just wanted it to operate independently here######
coords =  [(1,2), (6,12)]#####We don't need this stuff, I just wanted it to operate independently here#####


def sequence_slicer(sequence, coords):
	'''
	This function takes the sequence and coordinates from lrg_parse()
	These are used to output a FASTA formatted file that contains the sections of 
	sequence defined by the coordinates.
	'''
	exons = []
	for exon in range(0, len(coords)):
		start, end = coords[exon]
		start = int(start)
		end = int(end)
		info = "exon %d start: %d, end: %d" % (exon+1, start, end)
		# start must be -1 for indexing, end is ok as the slice locations are between positions
		exon = info, sequence[start-1: end]
		exonSeq = sequence[start-1: end] #####Here is appended line######
		print exonSeq
		assert len(exonSeq) >= 3, "Exon is not long enough, it has fewer than 3 nucleotides" ######Here is appended line######
		exons.append(exon)
	return exons

ss = sequence_slicer(sequence, coords)
