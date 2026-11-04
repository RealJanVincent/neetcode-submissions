class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        m = {}      
        for n in set_nums:
            m[n] = []

        for n in set_nums:
            if len(m[n]) == 0:
                s = m[n]
                i = n
                while i in m:
                    s.append(i)
                    m[i] = s
                    i += 1
        
        longest = 0
        for s in m.values():
            longest = max(longest, len(s))

        return longest
                    
