class Solution:
    """brute force"""
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def _isPal(w):
            for i in range(len(w)//2):
                if w[i] != w[~i]:
                    return False
            return True

        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if _isPal(words[i]+words[j]):
                    res.append([i, j])
                if _isPal(words[j]+words[i]):
                    res.append([j, i])
        return res

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(check):
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals

# TODO: Use Trie to optimize Brute Forse Sol