# Assume you have a method isSubstring which checks if one word is a substring
#of another. Given two strings, s1 and s2, write a code to check if s2 is a 
# rotation of s1 using only one call to isSubstring.
# ("waterbottle" is a rotation of "erbottlewat")

def isSubstring(string, sub_str):
    if sub_str in string:
        return True
    else:
        return False

def isRotation0(s1, s2):
    if len(s1) != len(s2):
        return False
    i,j = 0,0
    while i < len(s2):
        if s1[i]!=s2[j]:
            i+=1
            continue
        else:
            for i1 in range(i,len(s1)):
                if s1[i1] != s2[j]:
                    j=0
                    break
                else:
                    j+=1
            return s2[j:] == s1[:i]
        i+=1
    return False

def isRotation(s1, s2):
    l = len(s1)
    if l != len(s2) or l < 1:
        return False
    return isSubstring(s1+s1,s2)


"""
s1 = "waterbottle" 
s2 = "erbottlewat"
tests = [(s1,s2),("hello","llohe"),("hello","lloh"),("hello","ohlle"),("hello","ohell")]
expected_results = [True,True,False,False,True]

for s1,s2 in tests:
    if isRotation(s1, s2):
        print('"{0}" is a rotation of "{1}"'.format(s1,s2))
    else:
        print('"{0}" is NOT a rotation of "{1}"'.format(s1,s2))
"""