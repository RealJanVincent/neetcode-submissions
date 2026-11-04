class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        items = list(freq.items())
        items.sort(key=lambda x : -x[1])
        res = []
        for i in range(k):
            res.append(items[i][0])
        return res
