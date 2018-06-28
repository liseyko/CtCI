# Write a method to replace all spaces in a c-string with '%20'.

istr = bytearray("Mr John Smith     ",'ascii')
ilen = 13

wsc = 0
print(istr)
print(istr.decode())

for i in range(13):
    if chr(istr[i]) == ' ':
        wsc+=1

j = ilen+wsc*2-1
for i in range(ilen-1,0,-1):
    if chr(istr[i]) == ' ':
        istr[j] = ord('0'); j-=1
        istr[j] = ord('2'); j-=1
        istr[j] = ord('%'); j-=1 ; i-=1
        wsc-=1
        if wsc == 0:
            break
    else:
        istr[j] = istr[i]
        j-=1

print(istr)
print(istr.decode())

