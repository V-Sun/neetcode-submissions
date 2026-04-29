class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        Rows, Cols = len(heights), len(heights[0])
        Directions = [[-1,0], [1,0], [0,-1], [0,1]]

        def isValid(i, j):
            if i >= Rows or j >= Cols or i < 0 or j < 0:
                return False
            return True
    
        def dfs(i, j, visited):
            if isValid(i, j) is False or (i,j) in visited:
                return

            visited.add((i,j))
            
            for dr, dc in Directions:
                if isValid(i + dr, j + dc):
                    if heights[i + dr][j + dc] >= heights[i][j]:
                        dfs(i + dr, j + dc, visited)
    
        pac_visited = set()
        atl_visited = set()

        # DFS from all pacific border cells
        for r in range(Rows):
            dfs(r, 0, pac_visited)
        for c in range(Cols):
            dfs(0, c, pac_visited)

        # DFS from all atlantic border cells
        for r in range(Rows):
            dfs(r, Cols - 1, atl_visited)
        for c in range(Cols):
            dfs(Rows - 1, c, atl_visited)
        
        for i, j in pac_visited:
            if (i,j) in atl_visited:
                temp = []
                temp.append(i)
                temp.append(j)
                res.append(temp)

        return res


                    