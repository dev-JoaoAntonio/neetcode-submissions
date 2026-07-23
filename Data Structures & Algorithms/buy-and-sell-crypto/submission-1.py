class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        bestProfit = 0
        for todaysPrice in prices:
            todaysProfit = todaysPrice - buy
            if todaysProfit > bestProfit:
                bestProfit = todaysProfit
            if todaysPrice < buy:
                buy = todaysPrice
        return bestProfit