# Write a method to replace all spaces in a c-string with '%20'.

def replace(string,fchr=" ",rstr="%20"):

    fchr_count = 0
    for c in string:
        if c == fchr:
            fchr_count += 1
    real_len = len(string)
    bs = bytearray(string+" "*fchr_count*(len(rstr)-1),'ascii')

    j = real_len + fchr_count*2-1
    for i in range(real_len-1,-1,-1):
        if chr(bs[i]) == ' ':
            bs[j] = ord('0'); j -= 1
            bs[j] = ord('2'); j -= 1
            bs[j] = ord('%'); j -= 1 ; i -= 1
            fchr_count -= 1
            if fchr_count == 0:
                break
        else:
            bs[j] = bs[i]
            j-=1
    return(bs.decode())
