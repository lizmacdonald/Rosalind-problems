### Problem number 3


path = '/Users/elizabethmacdonald/desktop/python/Rosalind-problems/3_Complementing_a_strand_of_DNA/rosalind_revc.txt'
with open(path, 'r') as prob1:
    data = prob1.read()
    

comp = ""
i = len(data)

while i >0:
    comp = comp + data[i-1]
    i = i - 1


complement = ""

for i in comp:
    if i == "A":
        complement = complement + "T"
    elif i == "T":
        complement = complement + "A"
    elif i == "G":
        complement = complement + "C"
    elif i == "C":
        complement = complement + "G"



print (str(complement))