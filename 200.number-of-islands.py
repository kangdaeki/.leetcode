#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        y=len(grid)
        x=len(grid[0])
        no_islands=0

        def dfs(a:int,b:int):
            if a<0 or b<0 or a>=y or b>=x:
                return
            if "1"==grid[a][b]:
                grid[a][b]="0"
                dfs(a+1,b)
                dfs(a-1,b)
                dfs(a,b-1)
                dfs(a,b+1)

        for i in range(y):
            for j in range(x):
                if "1"==grid[i][j]:
                    no_islands+=1
                    dfs(i,j)
        return no_islands
# @lc code=end

