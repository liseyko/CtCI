class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ki = {k: i for i, k in enumerate(keyboard)}
        w = keyboard[0] + word
        return sum(abs(ki[w[i+1]] - ki[w[i]]) for i in range(len(w)-1))
