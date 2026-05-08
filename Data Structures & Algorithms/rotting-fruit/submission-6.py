class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        bfs = deque()
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    bfs.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        def isValid(r, c):
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]) and grid[r][c] == 1:
                return True
            return False
        
        if fresh == 0:
            return 0

        minutes = -1

        while bfs:
            curr_rott = len(bfs)
            for i in range(curr_rott):
                temp = bfs.popleft()
                for dr, dc in directions:
                    if isValid(temp[0] + dr, temp[1] + dc):
                        bfs.append((temp[0] + dr, temp[1] + dc))
                        grid[temp[0] + dr][temp[1] + dc] = 2
            minutes += 1

        for r in grid:
            if 1 in r:
                return -1
        return minutes

        