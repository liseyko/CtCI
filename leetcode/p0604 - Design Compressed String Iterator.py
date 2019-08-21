class StringIterator:

    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.ptr, self.ctr, self.ctrlen = -2, 1, 1
        self._adjustPtr()

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        res = self.compressedString[self.ptr]
        self._adjustPtr()
        return res

    def _adjustPtr(self):
        self.ctr -= 1
        if self.ctr:
            return
        self.ptr += 1 + self.ctrlen
        if not self.hasNext:
            return
        self._loadCtr()

    def _loadCtr(self):
        self.ctr, self.ctrlen = 0, 0
        while self.ptr+1+self.ctrlen < len(self.compressedString) and\
                self.compressedString[self.ptr+1+self.ctrlen].isdigit():
            self.ctr = self.ctr * 10 + int(self.compressedString[self.ptr +1+self.ctrlen])
            self.ctrlen += 1

    def hasNext(self) -> bool:
        if self.ptr < len(self.compressedString):
            return True
        return False


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
