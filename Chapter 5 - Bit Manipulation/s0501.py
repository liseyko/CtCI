def ins_m_in_n(n,m,i,j):
    return((n >> j << j) + (m << i) + ((n >> i << i) ^ n))

if __name__=='__main__':
    n = int('10000000000',2)
    m = int('10011',2)
    i, j = 2, 6
    #print(bin(n))
    #print(bin((n >> j << j)))
    #print(bin(m << i))
    #print(bin((n >> i << i) ^ n))
    #print(bin((n >> j << j) + (m << i) + ((n >> i << i) ^ n)))
    print(bin(ins_m_in_n(n,m,i,j)))