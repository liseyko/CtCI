class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (any(rec1[0] < x < rec1[2] for x in rec2[0::2]) or
                any(rec2[0] < x < rec2[2] for x in rec1[0::2])) and\
               (any(rec1[1] < y < rec1[3] for y in rec2[1::2]) or
                any(rec2[1] < y < rec2[3] for y in rec1[1::2]))

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not(rec1[0] >= rec2[2] or
                   rec1[2] <= rec2[0] or
                   rec1[3] <= rec2[1] or
                   rec1[1] >= rec2[3])

    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:

        def intersect(pl, pr, ql, qr):
            return min(pr, qr) > max(pl, ql)

        return intersect(*rec1[0::2], *rec2[0::2]) and\
            intersect(*rec1[1::2], *rec2[1::2])
