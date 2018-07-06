#a. Implement an algorithm to determine if a string has all unique characters.
#b. What if you can not use additional data structures?

def isUniqueA(check_string):
    s = set()
    for c in check_string:
    	if c not in s:
    		s.add(c)
    	else:
    		return False
    return True

def isUniqueB(check_string):
    s = sorted(check_string)
    for i in range(1,len(s)):
      if s[i] == s[i-1]:
        return False
    return True
