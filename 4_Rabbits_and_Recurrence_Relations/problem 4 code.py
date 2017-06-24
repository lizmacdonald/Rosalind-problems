### Problem number 4

  
  
numMonths = 34
numOffspring = 4

a,b = 0,1

for i in range(1, numMonths):
	a, b = b, numOffspring * a + b
	print (b)