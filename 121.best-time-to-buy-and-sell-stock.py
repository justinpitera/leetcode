#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_profit = 0
        
        for right in range(len(prices)):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right
                
            right += 1
        
        return max_profit
                
# @lc code=end

sol = Solution()
prices = [7,1,5,3,6,4]
result = sol.maxProfit(prices=prices)
