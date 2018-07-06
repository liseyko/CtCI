#Given two strings, write a method to decide if one is permutation of the other.

from collections import defaultdict

def check_permutation0(s1,s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

def check_permutation1(s1,s2):
    if len(s1) != len(s2):
        return False
    d = defaultdict(int)
    for i in range(len(s1)):
        d[s1[i]]+=1
        d[s2[i]]-=1
    for i in d.values():
        if i != 0:
            return False
    return True

