#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = defaultdict(list)
        state = [0] * numCourses
        
        # pop dict
        for course, p in prerequisites:
            preqs[course].append(p)
        
        def dfs(course) -> bool:
            # CYLCE
            if state[course] == 1:
                return False
            # COMPLETED
            if state[course] == 2:
                return True
            
            # MARK VISITNG
            state[course] = 1

            # DFS THRU EACH COURSE
            for p in preqs[course]:
                if not dfs(p):
                    return False
            # MARK COMPLETED
            state[course] = 2
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        return True

    
    
    
    
    
    
    
            
            
            
# @lc code=end




    