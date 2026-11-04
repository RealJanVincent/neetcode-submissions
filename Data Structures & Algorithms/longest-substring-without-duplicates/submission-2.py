class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if len(s) == 1:
        #     return 1

        longest = 0
        start = 0
        m = {}
        i = 0
        for c in s:
            if c in m and m[c] >= start:
                longest = max(longest, i - start)
                start = m[c] + 1
            m[c] = i
            i += 1
        print(m)
        return max(longest, i - start)