class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbrdic = {}
        for w in dictionary:
            key = self.w2a(w)
            if key not in self.abbrdic or self.abbrdic[key] == w:
                self.abbrdic[key] = w
            else:
                self.abbrdic[key] = None

    def w2a(self, w):
        cutSize = max(0, len(w)-2)
        return w[0]+str(cutSize)+w[-1] if cutSize else w

    def isUnique(self, word: str) -> bool:
        abbr = self.w2a(word)
        return abbr not in self.abbrdic or\
            self.abbrdic[abbr] == word
