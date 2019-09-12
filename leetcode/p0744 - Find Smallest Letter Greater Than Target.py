class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect(letters, target) 
        return letters[i % len(letters)]
