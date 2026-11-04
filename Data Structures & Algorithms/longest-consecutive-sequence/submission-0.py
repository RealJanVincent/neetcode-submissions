class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = {}      
        for n in nums:
            m[n] = set()

        for n in nums:
            if len(m[n]) == 0:
                s = m[n]
                i = n
                while i in m:
                    s.add(i)
                    m[i] = s
                    i += 1
        
        longest = 0
        for s in m.values():
            longest = max(longest, len(s))

        return longest
                    
