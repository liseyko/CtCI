class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)

        return list(res.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyTpl = [0]*26

        def mkkey(w):
            key = keyTpl[:]
            for c in w:
                key[ord(c)-ord('a')] += 1
            return tuple(key)

        dic = collections.defaultdict(list)
        for word in strs:
            dic[mkkey(word)].append(word)

        return list(dic.values())
