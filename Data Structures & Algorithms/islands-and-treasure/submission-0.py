class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1,0], [1,0], [0, 1], [0, -1]]

        def dfs(r, c, distance):
            if(r < 0 or c < 0
            or r >= ROWS or c >= COLS or 
            grid[r][c] == 0 or grid[r][c] == -1) or distance >= grid[r][c]:
                return;
            
            grid[r][c] = distance

            for dr, dc in directions:
                dfs(r + dr, c + dc, grid[r][c] + 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    for dr, dc in directions:
                        dfs(r + dr, c + dc, grid[r][c] + 1)
        






