from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for prices in prices:
            if prices < min_price:
                min_price = prices
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit