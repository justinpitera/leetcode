#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_reach = 0
        curr_reach = 0
        jumps = 0
        
        for i in range(n - 1):
            max_reach = max(max_reach, i + nums[i])
            
            # review
            if i == curr_reach:
                jumps += 1
                curr_reach = max_reach
        
        return jumps
        
        
# @lc code=end

