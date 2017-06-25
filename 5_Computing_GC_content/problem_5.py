
path = '/Users/elizabethmacdonald/desktop/python/Rosalind-problems/5_Computing_GC_content/rosalind_gc.txt'
with open(path, 'r') as prob1:
    data = prob1.read()

spdat = []
spdat = data.split(">Rosalind_")



for set in spdat:
	set.find("GC")
	gc_count = 0
	len_count = len(i) - 4
	for t in i:
		if t == "\n":
			len_count = len_count -1
	for x in i:
		if x == "C":
			gc_count = gc_count + 1
		elif x == "G":
			gc_count = gc_count + 1
	gc_percent = gc_count/len_count * 100
	print (str("Rosalind_" + str(i[0:4])))
	print (str('GC: ' + str(gc_percent)))


path = '/Users/elizabethmacdonald/desktop/python/Rosalind-problems/5_Computing_GC_content/rosalind_gc.txt'
with open(path, 'r') as prob1:
    data = prob1.read()

spdat = []
spdat = data.split(">Rosalind_")

for fastaRaw in spdat[1::]:
	index = fastaRaw.find('\n') + 1
	fasta = fastaRaw[index::]
	fasta = fasta.replace('\n', '')
	length = len(fasta)
	gc_count = 0
	for seq in fasta:
		if seq == "C" or seq == "G":
			gc_count = gc_count + 1
	gc_percent = gc_count/length * 100
	print (str("Rosalind_" + str(fastaRaw[0:4])))
	print (str('GC: ' + str(gc_percent)))