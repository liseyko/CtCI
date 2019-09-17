class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if not word:
            return True
        last_case = word[-1].islower()
        uniform_body = all((c.islower() == last_case for c in word[1:-1]))
        proper_head = word[0].isupper() if word[-1].isupper() else True
        return uniform_body and proper_head
