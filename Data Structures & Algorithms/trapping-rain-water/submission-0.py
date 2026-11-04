class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0] * len(height)
        l = 0
        r = 1
        while r < len(height):
            while r < len(height) - 1 and height[l] > height[r]:
                r += 1
            
            if height[r] >= height[l]:
                for i in range(l + 1, r):
                    water[i] = height[l] - height[i]
            l = r
            r += 1
        print(water)
        l = len(height) - 2
        r = len(height) - 1
        while l >= 0:
            while l > 0 and height[r] > height[l]:
                l -= 1


            if height[l] >= height[r]:
                for i in range(l, r + 1):
                    water[i] = max(water[i], height[r] - height[i])
            r = l
            l -= 1
        print(water)

        return sum(water)
        