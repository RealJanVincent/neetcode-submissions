class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0;

        first = prices[0]
        rec_profit = self.maxProfit(prices[1:])

        max_profit = 0
        for p in prices:
            profit = p - first
            max_profit = max(profit, max_profit)
        
        return max(max_profit, rec_profit)


            