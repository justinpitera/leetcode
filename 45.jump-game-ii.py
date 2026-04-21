#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
from typing import List
# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        max_reach = 0
        end = 0
        jumps = 0
        
        for i in range(length - 1): # skip last index, no need to jump
            print(i)
            max_reach = max(max_reach, i + nums[i])
            
            if i == end:
                jumps += 1
                end = max_reach

        return jumps
        
        
# @lc code=end

sol = Solution()

res = sol.jump([2,3,1,1,4])
print(res)