class Solution:
    def get_perm_idxs(self,idx_set): # 1 2 3
        if len(idx_set) < 2:
            return [list(idx_set)]
        r = []
        for i in idx_set:
            r += [[i] + s for s in self.get_perm_idxs(idx_set-{i})]
        return r

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.get_perm_idxs(set(nums))

if __name__ == '__main__':
    s = Solution()
    print(s.permute([1,2,3]))
