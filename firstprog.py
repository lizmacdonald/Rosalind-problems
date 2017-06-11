
path = '/Users/elizabethmacdonald/desktop/python/rosalind_dna.txt'
with open(path, 'r') as prob1:
    data = prob1.read()


acount = 0
tcount = 0
ccount = 0
gcount = 0

for i in data:
    if i == 'A':
        acount = acount + 1
    elif i == 'T':
        tcount = tcount + 1
    elif i == 'C':
        ccount = ccount + 1
    elif i == 'G':
        gcount = gcount + 1

acount = str(acount)
ccount = str(ccount)
tcount = str(tcount)
gcount = str(gcount)

print (str('A: ' + acount))
print (str('C: ' + ccount))
print (str('G: ' + gcount))
print (str('T: ' + tcount))

