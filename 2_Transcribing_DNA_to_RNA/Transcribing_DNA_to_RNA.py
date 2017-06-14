### Project number 2


path = '/Users/elizabethmacdonald/desktop/python/Rosalind-problems/Transcribing_DNA_to_RNA/rosalind_rna.txt'
with open(path, 'r') as prob1:
    data = prob1.read()
    

alphabet = float

for i in data:
    if i == "T":
        alphabet = str(alphabet) + str("U")
    else:
        alphabet = str(alphabet) + str(i)

print (str(alphabet))