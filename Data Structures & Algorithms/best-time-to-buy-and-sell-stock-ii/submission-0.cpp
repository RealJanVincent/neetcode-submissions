class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int i = 0;
        while (i + 1 < prices.size()) {
            if (prices[i] < prices[i + 1]) {
                profit = profit + prices[i + 1] - prices[i];
            }
            i++;
        }
        return profit;
    }
};