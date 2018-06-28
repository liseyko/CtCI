#a. Implement an algorithm to determine if a string has all unique characters.
#b. What if you can not use additional data structures?

#a

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
		

#b	

print("Enter another test string:")
istr = sorted(input())
#print(istr)

for i in range(1,len(istr)):
  if istr[i] == istr[i-1]:
    print("This string has a duplicate character: ", istr[i])
    exit()
print("All characters are unique.")