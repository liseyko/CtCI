def reverse(string):

    bs = bytearray(string,'ascii')
    def swap(i1,i2):
        #print(i1,i2,string[i1],string[i2])
        t = bs[i1]
        bs[i1] = bs[i2]
        bs[i2] = t

    sl = len(bs)-1
    for i in range(sl//2):
        swap(i,sl-i)
    return bs.decode("ascii")
