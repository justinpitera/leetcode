#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[n] = i
        
        return []

# @lc code=end

sol = Solution()
numbers = [2,7,11,15]
target = 9
result = sol.twoSum(nums=numbers, target=target)
print(result)
