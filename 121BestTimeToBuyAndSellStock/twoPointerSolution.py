from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        maximum = 0
        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell = buy + 1
                continue
            profit = prices[sell] - prices[buy]
            if profit > maximum:
                maximum = profit
            sell += 1
        return maximum

"""
prices = [7,1,5,3,6,4]
buy = 1
sell = 6
maximum = 5
profit = 5
"""