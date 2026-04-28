class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        directions = [[-1, 0], [1,0], [0,1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
            

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if(row in range(ROWS)
                    and col in range(COLS)
                    and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            minutes += 1
            

        return minutes if fresh == 0 else -1
            
            
            

