class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        op = set(['(','{','['])
        for c in s:
            if c in op:
                stack.append(c)
            elif not stack or abs(ord(c) - ord(stack.pop())) > 2:
                return False
        return not stack

import argparse

def check_brackets(data):
    stack = []
    i = 0
    for c in data.strip('\n'):
        i += 1
        if c in {'(','[','{'}:
            stack.append(c)
        elif c in {')',']','}'}:
            if len(stack) == 0 or abs(ord(c) - ord(stack.pop())) > 2:
                return i
        else:
            continue
    if len(stack) > 0:
        return i
    return "Success"

def file_load():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="do something with a file",type=str)
    args = parser.parse_args()

    try:
        with open(args.filename,'r', encoding='utf-8') as f:
            data = f.read()
    except FileNotFoundError:
        print(f'File {args.filename} not found')
    else:
        return data


if __name__ == '__main__':
        print(check_brackets(file_load()))