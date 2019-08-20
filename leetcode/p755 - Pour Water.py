class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        heights.append(float('inf'))

        def flowdown(step):
            i = K
            while heights[i+step] <= heights[i]:
                i += step
            while i != K and heights[i] == heights[i-step]:
                i -= step
            if i != K:
                heights[i] += 1
                return True
            return False

        for _ in range(V):
            if not flowdown(-1) and not flowdown(1):
                heights[K] += 1

        heights.pop()
        return heights
