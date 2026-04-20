#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        
        return []
        
# @lc code=end

sol = Solution()
numbers = [2,7,11,15]
target = 9
result = sol.twoSum(numbers=numbers, target=target)
print(result)
