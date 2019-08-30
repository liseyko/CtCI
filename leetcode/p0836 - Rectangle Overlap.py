class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        r1x = sorted(rec1[0::2])
        r1y = sorted(rec1[1::2])
        r2x = sorted(rec2[0::2])
        r2y = sorted(rec2[1::2])
        return any(r1x[0] < x < r1x[1] for x in r2x) and\
            any(r1y[0] < y < r1y[1] for y in r2y) or\
            any(r2x[0] < x < r2x[1] for x in r1x) and\
            any(r2y[0] < y < r2y[1] for y in r1y) or\
            r2x[0] <= r1x[0] and r2x[1] >= r1x[1] and\
            r1y[0] <= r2y[0] and r1y[1] >= r2y[1] or\
            r2y[0] <= r1y[0] and r2y[1] >= r1y[1] and\
            r1x[0] <= r2x[0] and r1x[1] >= r2x[1]

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not(rec1[0] >= rec2[2] or
                   rec1[2] <= rec2[0] or
                   rec1[3] <= rec2[1] or
                   rec1[1] >= rec2[3])
