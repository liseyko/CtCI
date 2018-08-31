#code
import sys

def chkPal(s):
    ln = len(s)
    if ln < 0:
        return False
    elif ln == 1:
        return True
    for i in range(ln // 2):
        if s[i] != s[~i]:
            return False
    return True
        

if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split()))[2::2]

    for s in data:
        print("Yes" if chkPal(s) else "No")
