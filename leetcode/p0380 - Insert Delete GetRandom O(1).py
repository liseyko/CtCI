class RandomizedSet:

    def __init__(self):
        self.dvk, self.data = {}, []  # dataVal2Key, dataList

    def insert(self, val: int) -> bool:
        if val in self.dvk:
            return False
        self.dvk[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dvk:
            return False
        self.data[self.dvk[val]] = self.data[-1]
        self.dvk[self.data[-1]] = self.dvk[val]
        self.data.pop()
        del self.dvk[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
