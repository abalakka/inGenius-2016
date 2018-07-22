file1 = open("outputON",'r')
file2 = open("barcodeON",'r')
s=[]
i=0
for line1 in file1:
	s.append (line1)
for line2 in file2:
	line2 = line2 
	s.append(line2)

if s[0]==s[1]:
	print 1
else:
	print 0
	
