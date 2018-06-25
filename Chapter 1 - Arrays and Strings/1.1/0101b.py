print("Enter a test string:")
istr = sorted(input())
#print(istr)

for i in range(1,len(istr)):
  if istr[i] == istr[i-1]:
    print("This string has a duplicate character: ", istr[i])
    exit()
print("All characters are unique.")