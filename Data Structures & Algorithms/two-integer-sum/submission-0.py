class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[nums[i]] = []
            m[nums[i]].append(i)

        k = -1
        l = -1
        for i in range(len(nums)):
            toFind = target - nums[i]
            inds = m.get(toFind, [])
            for ind in inds:
                if ind != i:
                    k = i
                    l = ind
                    return [k, l]
                    