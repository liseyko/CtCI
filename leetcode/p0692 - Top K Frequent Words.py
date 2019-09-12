class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wc = collections.Counter(words)
        h = [(-cnt, w) for w, cnt in wc.items()]
        heapq.heapify(h)
        return [heapq.heappop(h)[1] for _ in range(k)]
