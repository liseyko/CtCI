# Implement a method to perform basic string compression using counts of repeated characters.

import time
from io import StringIO

in_strings = ["aabcccccaaa","abbc","abbccc","xxxxxxxXyyyyyYzzzzzzZ","aaaaaaaaffffffffffffffffffdffffffffffffffffffffggggggggggggggggrttttttttttttttttttttttttttttgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggssssssssssssdddddddfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"]
for i in range(18):
    in_strings[0]+=in_strings[0]




def s_compress(s):
    os = ""
    i=0
    while(i<len(s)):
        cnt=1
        while(i<len(s)-1 and s[i] == s[i+1]):
            cnt+=1
            i+=1
        os+=s[i]+str(cnt)
        i+=1
    if len(os) < len(s):
        return os
    else:
        return s

def get_compressed_len(s):
    if len(s) == 0: return 0
    cl = 0
    i = 0
    while(i < len(s)):
        cnt = 1
        while(i<len(s)-1 and s[i] == s[i+1]):
            cnt+=1
            i+=1
        i+=1
        cl+=2
        while cnt>9:
            cnt = cnt//10
            cl+=1
    return(cl)


def s_compress_opt1(s):
    if len(s) <= get_compressed_len(s):
        return(s)
    str_list = []
    i=0
    while(i<len(s)):
        cnt=1
        while(i<len(s)-1 and s[i] == s[i+1]):
            cnt+=1
            i+=1
        str_list.append(s[i])
        str_list.append(str(cnt))
        i+=1
    return(''.join(str_list))

def s_compress_opt2(s):
    clen = get_compressed_len(s)
    if len(s) <= clen:
        return(s)

    bs = bytearray(clen)
    i=0
    j=0
    while(i<len(s)):
        cnt=1
        while(i<len(s)-1 and s[i] == s[i+1]):
            cnt+=1
            i+=1
        bs[j] = ord(s[i]); j+=1
        for b in str(cnt).encode():
            #print(b)
            bs[j] = b; j+=1
        i+=1
    return(bs.decode())


start_time = time.time()
for s in in_strings:
    #print(s_compress(s))
    s_compress(s)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for s in in_strings:
    #print(s_compress_opt1(s))
    s_compress_opt1(s)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for s in in_strings:
    #print(s_compress_opt2(s))
    s_compress_opt2(s)
print("--- %s seconds ---" % (time.time() - start_time))