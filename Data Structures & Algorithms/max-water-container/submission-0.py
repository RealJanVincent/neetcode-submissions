class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        h = min(heights[l], heights[r])
        max_vol = 0
        while l != r:
            h = min(heights[l], heights[r])
            vol = h * (r - l)
            max_vol = max(vol, max_vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_vol

