if __name__=='__main__':
    t = int(input())
    for i in range(t):
        str = input().strip()
        print(remainderWith7(str))


''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. '''

#your task is to complete this function
#Function should return the required answer
#You are not allowed to convert string to integer
def remainderWith7(str):
    d = 0
    for c in str:
        d = d*10 + ord(c) - ord('0')
        #d %= 7
        while d >= 7:
            d -= 7
    return d