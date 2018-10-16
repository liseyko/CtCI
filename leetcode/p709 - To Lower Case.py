class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        r = []

        for c in str:
            if 'A' <= c <= 'Z':
                r.append(chr(ord(c)+32))
            else:
                r.append(c)
        #r = []
        #for c in str:
        #    r.append(chr(ord(c)|ord(" ")))
               
        return ''.join(r)