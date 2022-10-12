def printValues():
	l = list()
	for i in range(1,33):
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()