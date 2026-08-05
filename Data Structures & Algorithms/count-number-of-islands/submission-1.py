class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        def dfs(x,y) -> None:
            neighbors = [[1,0],[0,1],[0,-1],[-1,0]]
            grid[x][y] = "0"
            for dx, dy in neighbors:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[dx+x][dy+y] == "1":
                    dfs(x+dx, y+dy)
        
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    dfs(x,y)
                    count += 1
        
        return count
            
                    