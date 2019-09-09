class TwoSum:
    """for few add() and many find()"""
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        bisect.insort(self.nums, number)

    def find(self, value: int) -> bool:
        if sum(self.nums[-2:]) < value or\
           sum(self.nums[:2]) > value:
            return False
        i, j = 0, len(self.nums)-1
        while i < j:
            summ = self.nums[i]+self.nums[j]
            if summ < value:
                i += 1
            elif summ > value:
                j -= 1
            else:
                return True
        return False


class TwoSum:
    """for many add() and few find()"""
    def __init__(self):
        self.nums = []

    def add(self, number: int) -> None:
        self.nums.append(number)

    def find(self, value: int) -> bool:
        self.nums.sort()
        if sum(self.nums[-2:]) < value or\
           sum(self.nums[:2]) > value:
            return False
        i, j = 0, len(self.nums)-1
        while i < j:
            summ = self.nums[i]+self.nums[j]
            if summ < value:
                i += 1
            elif summ > value:
                j -= 1
            else:
                return True
        return False
