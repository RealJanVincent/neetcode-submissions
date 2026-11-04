class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n

        # Invariant:
        # pre[i] = nums[0] * ... * nums[i - 1]
        cur = 1
        for i in range(n):
            pre[i] = cur
            cur *= nums[i]


        # Invariant:
        # pre[i] = nums[n - 1] * ... * nums[i + 1]
        cur = 1
        for i in reversed(range(n)):
            post[i] = cur
            cur *= nums[i]
        
        res = []
        for i in range(n):
            res.append(pre[i] * post[i])
        
        return res