class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max_profit = 0
        # # i = left
        # # l = right
        # i = 0
        # j = 0
        # while i < len(prices) - 1:
        #     while i < len(prices) - 2 and prices[i] > prices[i + 1]:
        #         i += 1
        #     j = i + 1
        #     while j < len(prices) - 1 and prices[j] < prices[i + 1]:
        #         j += 1
        #     max_profit = max(max_profit, prices[j] - prices[i])
        #     i = j + 1

        # return max_profit

        min_price = 1000
        profit = 0
        for p in prices:
            if p < min_price:
                min_price = p
            else:
                profit = max(profit, p - min_price)
        return profit

