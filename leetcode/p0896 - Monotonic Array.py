class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i] <= A[i+1] for i in range(len(A)-1)) or\
         all(A[i] >= A[i+1] for i in range(len(A)-1))

    def isMonotonic(self, A: List[int]) -> bool:
        status = 0
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                status |= 1
            elif A[i] > A[i+1]:
                status |= 2
            if status == 3:
                return False
        return True
