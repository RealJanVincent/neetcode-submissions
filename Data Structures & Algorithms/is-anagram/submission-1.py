class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1 = {}
        m2 = {}
        for i in range(len(t)):
            m1[s[i]] = m1.get(s[i], 0) + 1
            m2[t[i]] = m2.get(t[i], 0) + 1
        return m1 == m2