class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            if l < 10:
                l = "00" + str(l)
            elif l < 100:
                l = "0" + str(l)
            else:
                l = str(l)
            res = res + l + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            l = int(s[i:i + 3])
            i += 3
            st = s[i:i + l]
            strs.append(st)
            i += l
        return strs
        