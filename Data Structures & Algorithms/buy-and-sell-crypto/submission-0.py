class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for price in prices:
            minBuy = min(minBuy, price)
            profit = price - minBuy
            maxProfit = max(maxProfit, profit)

        return maxProfit