#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        max_reach = 0
        end = 0
        jumps = 0
        
        for i in range(length - 1):
            max_reach = max(max_reach, i + nums[i])
            
            if i == end:
                jumps += 1
                end = max_reach

        return jumps
        
        
# @lc code=end

