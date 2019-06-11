class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def bt(idxs=[], used=set()):
            if len(idxs) == len(nums):
                res.append([nums[j] for j in idxs])
                return
            for j in range(len(nums)):
                if j not in used:
                    bt(idxs+[j], used | {j})
        bt()
        return res


def heaps_algorithm(a, n=None):
    if n is None:
        n = len(a)
    if n == 1:  # (got a new permutation)
        print(a)
        return
    for i in range(n-1):
        heaps_algorithm(a, n-1)
        # always swap the first when odd,
        # swap the i-th when even
        if n % 2 == 0:
            a[n-1], a[i] = a[i], a[n-1]
        else:
            a[n-1], a[0] = a[0], a[n-1]
    heaps_algorithm(a, n-1)


class Solution:
    def get_perm_idxs(self, idx_set):  # 1 2 3
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
    heaps_algorithm([1, 2, 3], 3)
    s = Solution()
    print(s.permute([1, 2, 3]))
