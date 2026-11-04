class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        w = strs[0]
        for i in range(len(w)):
            for s in strs:
                if len(s) <= i or s[i] != w[i]:
                    return res
            res = res + w[i]
        return res
        
        