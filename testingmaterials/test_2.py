#Checks that the sequence contains only A, C, T, G.
##Sequence we want is gsequence from first function

#Import file
##TO DO
gsequence = 'AGCTAG2TCGATCT'

nucleotides = ['A','C','T','G']

for nuc in gsequence:
    assert nuc in nucleotides, "Mistake"
    print 'working fine'