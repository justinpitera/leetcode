#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
from typing import List

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or 
                grid[r][c] != '1'
            ):
                return
            
            grid[r][c] = '0'
            
            DIRECTIONS = [(1,0),(-1,0),(0,-1),(0,1)]
            for dr, dc in DIRECTIONS:
                dfs(r + dr, c + dc)
                
        island_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)
                    
        return island_count
# @lc code=end

