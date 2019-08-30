class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:

        def intersectSize(pl, pr, ql, qr):
            return max(0, min(pr, qr)-max(pl, ql))

        return((D-B)*(C-A)+(H-F)*(G-E)-intersectSize(A,C,E,G)*intersectSize(B,D,F,H))
