''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#Your task is to complete this function 
#Your function should return a String
def convertRoman(n):
    ints = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    i2r = {1000:'M', 900:'CM', 500:'D', 400:'CD', \
            100:'C', 90: 'XC', 50: 'L', 40: 'XL', \
             10:'X', 9:  'IX', 5:  'V', 4:  'IV', 1: 'I'}
             
    r = []
    for i in ints:
        while n >= i:
            n -= i
            r.append(i2r[i])
        if n == 0:
            break
    return ''.join(r)


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        print(convertRoman(n))
