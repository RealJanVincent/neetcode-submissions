class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            w = str(sorted(s))
            if w not in m:
                m[w] = []
            m[w].append(s)
        res = []
        for l in m.values():
            res.append(l)
        return res