b = input("Írj be egy számot: ")
c = int(b)*10
for i in range(int(c)):
	ib = i + 1
	name = 'víces' + str(ib) + '.txt'
	fp = open(name, 'w')
	print("Created file n " + str(ib))
	
	for x in range(10):
		xb = x + 1
		fp.write("X"*1024*1024*10)
		print("Writing... " + str(xb))