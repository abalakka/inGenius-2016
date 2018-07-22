

file = open('barcode.txt', 'r')
#file = raw_input()
s = []
for line in file:
	s = line.split()
word = s[3]
word = word[1:len(word)-1]


fileToSave = open('barcodeON', 'w')
fileToSave.write(word)
fileToSave.close() 
