class RandomizedSet:

    def __init__(self):
        self.val2id = {}
        self.id2val = {}

    def insert(self, val: int) -> bool:
        if val in self.val2id:
            return False
        cur_id = len(self.val2id)
        self.val2id[val] = cur_id
        self.id2val[cur_id] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.val2id:
            last_id = len(self.val2id)-1
            last_val = self.id2val[last_id]
            cur_id = self.val2id[val]
            self.val2id[last_val] = cur_id
            self.id2val[cur_id] = last_val
            del self.val2id[val]
            del self.id2val[last_id]
            return True
        return False

    def getRandom(self) -> int:
        max_id = len(self.val2id)-1
        if max_id >= 0:
            id = random.randint(0, max_id)
            return self.id2val[id]
