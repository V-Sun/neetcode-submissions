class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        Rows, Cols = len(board), len(board[0])
        Directions = [[-1,0], [1,0], [0,-1], [0,1]]

        # Helper Function to check if two indeces are valid in the board
        def isValid(i, j):
            if i < 0 or j < 0 or i >= Rows or j >= Cols:
                return False
            return True

        def dfs(i, j):
            if isValid(i, j) is False:
                return
            if board[i][j] == "X" or (i, j) in visited:
                return
            
            visited.add((i,j))
            board[i][j] = "#"
            
            for dr, dc in Directions:
                if isValid(i + dr, j + dc):
                    if board[i+dr][j+dc] == "O":
                        dfs(i + dr, j + dc)
            
        for r in range(Rows):
            dfs(r, 0)
        for c in range(Cols):
            dfs(0, c)
        for r in range(Rows):
            dfs(r, Cols-1)
        for c in range(Cols):
            dfs(Rows - 1, c)

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
                


            
            
            