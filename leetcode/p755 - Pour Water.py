class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        heights.append(float('inf'))
        
        def flow(step):
            nonlocal V
            i = K
            while heights[i+step] <= heights[i]:
                i += step
            while i != K and heights[i] == heights[i-step]:
                i -= step
            if i != K:
                heights[i] += 1
                V -= 1
                return True
            return False

        while V:
            if not flow(-1) and not flow(1):
                heights[K] += 1
                V -= 1

        return heights[:-1]
