class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        heights.append(float('inf'))

        def findNextLow(k, lr ):
            print('find', k, lr)
            if heights[k+lr] <= heights[k]:
                lower = findNextLow(k+lr, lr)
                print(heights[k+lr], '<', heights[k], lower)                
            elif heights[k+lr] < heights[k]:
                return lower if lower is not None else k+lr
                
        def findLow(k):
            nxtLow = findNextLow(k, -1)
            if not nxtLow:
                nxtLow = findNextLow(k, 1)
            if not nxtLow:
                nxtLow = k
            return nxtLow
            
        def pour(v, k):
            while v:
                lowspot = findLow(k)
                diff = max(1, min(v, heights[k] - heights[lowspot]))
                print(lowspot, diff)
                heights[lowspot] += diff
                v -= diff
        pour(V, K)
        return heights[:-1]
