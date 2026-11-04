class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        m = {}
        for j in range(len(nums)):
            for i in range(j):
                summ = nums[i] + nums[j]
                if summ not in m:
                    m[summ] = []
                m[summ].append([i, j]) 
        triplets = []
        for i in range(len(nums)):
            comp = -nums[i]
            if comp in m:
                pairs = m[comp]
                for p in pairs:
                    if i not in p:
                        triplet = [p[0], p[1], i]
                        triplets.append(triplet)
        res = []
        for t in triplets:
            sortedTuple = tuple(sorted([nums[i] for i in t]))
            res.append(sortedTuple)
        return list(set(res))
            