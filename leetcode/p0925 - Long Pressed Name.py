class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0
        ln, lt =  len(name), len(typed)

        while i < ln and j < lt:
            print(i,j)
            if i < ln - 1 and name[i] == typed[j] and name[i] == name[i+1] and j < lt:
                i, j = i+1, j+1
            elif j < len(typed)-1 and name[i] == typed[j] and name[i] == typed[j+1]:
                j += 1
            elif name[i] == typed[j]:
                i, j = i+1, j+1
            else:
                return False

        if i == ln and j == lt:
            return True
        else:
            return False