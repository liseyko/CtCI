class Solution:
    def intervalIntersection(self, A, B):
        res = []
        i = j = 0

        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                res.append([lo, hi])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return res

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            intersection = [max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]
            if intersection[0] <= intersection[1]:
                res.append(intersection)
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        h = []
        for iv in A+B:
            heapq.heappush(h, (iv[0], float('-inf'), 1))
            heapq.heappush(h, (iv[1], float('inf'), -1))

        res = []
        state = 0
        while h:
            x, _, flag = heapq.heappop(h)
            state += flag
            print(x, flag, state)
            if state == 2 and flag == 1:
                interval = [x, x]
            elif state == 1 and flag == -1:
                interval[1] = x
                res.append(interval[:])

        return res
