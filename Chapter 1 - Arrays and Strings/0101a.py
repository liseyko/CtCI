print("Enter a test string:")
istr = input()
#print(istr)
s = set()
for c in istr:
	if c not in s:
		s.add(c)
	else:
		print("This string has a duplicate character: ", c)
		exit()
print("All characters are unique.")
		
	
