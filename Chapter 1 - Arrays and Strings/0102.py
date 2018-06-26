bs = bytearray("Implement a function in C/C++ to reverse a null terminated string.",'ascii')

print(bs.decode("ascii"))

def reverse(string):

  def swap(i1,i2):
    #print(i1,i2,string[i1],string[i2])
    t = string[i1]
    string[i1] = string[i2]
    string[i2] = t

  sl = len(string)-1
  for i in range(sl//2):
    swap(i,sl-i)

reverse(bs)

print(bs.decode("ascii"))

