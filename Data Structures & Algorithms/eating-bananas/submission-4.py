class Solution:
    def isSolution(self, piles, h, k):
        for p in piles:
            h_p = p // k
            if p % k != 0:
                h_p += 1
            h -= h_p
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = max(piles)
        
        start = 1
        end = k
        while True:
            if end < start:
                return k
            if end == start:    
                cur_try = self.isSolution(piles, h, start)
                if cur_try >= 0:
                    return min(start, k)
                else:
                    return k
            step = (end - start) // 2
            mid = start + step
            cur_try = self.isSolution(piles, h, mid)
            if cur_try >= 0:
                k = mid
                end = mid - 1
            else:
                start = mid + 1

        return k