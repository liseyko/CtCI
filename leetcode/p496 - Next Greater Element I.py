class Solution:
    def nextGreaterElement(self, findNums, nums):
        st, d = [], {}
    
        for v in nums:
            while st and st[-1] < v:
                d[st.pop()] = v
            st.append(v)
        
        return [d.get(x, -1) for x in findNums]