import re

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if re.match(r'^\ *[\+\-]?\.\d+(e[\-\+]?\d+)?\ *$', s)\
        or re.match(r'^\ *[\+\-]?\d+(\.\d*)?(e[\-\+]?\d+)?\ *$', s):
            return True

        return False
