#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
from typing import List

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            allowed_height = min(height[left], height[right])
            curr_area = allowed_height * (right - left)
            
            max_area = max(max_area, curr_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
            
    
# @lc code=end

sol = Solution()

res = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(res)