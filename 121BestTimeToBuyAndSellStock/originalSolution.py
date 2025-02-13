from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        for bought_i in range(0, len(prices)):
            for sold_j in range(bought_i + 1, len(prices)):
                if prices[bought_i] < prices[sold_j]:
                    profit = prices[sold_j] - prices[bought_i]
                    if profit > maximum:
                        maximum = profit
        return maximum


"""
prices = [7,1,5,3,6,4]
maximum = 0

bought_i = 1
sold_j = 3

"""


