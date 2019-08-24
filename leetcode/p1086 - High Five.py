class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = collections.defaultdict(list)
        for student, grade in items:
            heapq.heappush(scores[student], grade)
            if len(scores[student]) > 5:
                heapq.heappop(scores[student])

        return [[k, sum(v)//5] for k, v in scores.items()]
