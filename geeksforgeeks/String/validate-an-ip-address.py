import sys

def ipIsValid(ip):
    ip = list(ip.split('.'))
    if len(ip) != 4:
        return 0
    for n in ip:
        if n[0] == '0':
            return 0
        try:
            n = int(n)
        except:
            return 0
        if n < 0 or n > 255:
            return 0
    return 1


if __name__ == '__main__':
    data = list(map(str,sys.stdin.read().split()))[1:]
    for ip in data:
        print(ipIsValid(ip))