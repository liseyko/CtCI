class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def dfs(left, path, idx):
            #print(left, path, idx)
            if not left: res.append(path[:])
            else:
                for i, val in enumerate(nums[idx:]):
                    if val > left: break
                    dfs(left - val, path + [val], idx + i)

        dfs(target, [], 0)
        return res