"""
Testcases:
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[0,3,3],[3,5,3]]
[[2,9,10],[9,12,15]]
[[1,2,1],[1,2,2],[1,2,3]]
[[0,3,3],[1,5,3],[2,4,3],[3,7,3]]
[[2,4,7],[2,4,5],[2,4,6]]

"""


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        peaks = [[x1, y] for [x1, x2, y] in sorted(buildings)]
        valleys = [[x2, y] for [x1, x2, y] in sorted(buildings, key=lambda xxy: xxy[1])]
        results = []
        heights = {0: 1}
        j = 0
        top = 0

        for i, [vx, vy] in enumerate(valleys):
            while j < len(buildings) and peaks[j][0] <= valleys[i][0]:
                px, py = peaks[j]
                if py > top:
                    top = py
                    if results and results[-1][0] == px:
                        results[-1][1] = py
                    else:
                        results.append([px, py])
                heights[py] = heights[py] + 1 if py in heights else 1
                j += 1

            heights[vy] -= 1
            if not heights[vy]:
                del heights[vy]
            if vy == top and vy not in heights:
                top = max(heights.keys())
                if results[-1][0] == vx:
                    results[-1][1] = top
                else:
                    results.append([vx, top])

        return results
