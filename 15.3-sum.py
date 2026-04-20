#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            b = i + 1
            c = len(nums) - 1
            
            while b < c:
                total = a + nums[b] + nums[c]
                
                if total < 0:
                    b += 1
                elif total > 0:
                    c -= 1
                else:
                    res.append([a, nums[b], nums[c]])
                    b += 1
                    c -= 1
                    
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
        
        return res
            
        
# @lc code=end

