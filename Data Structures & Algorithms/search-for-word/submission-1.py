class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Rows, Cols = len(board), len(board[0])
        size = len(word)
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = set()

        def isValid(i, j):
            if i < 0 or j <0 or i >= Rows or j >= Cols or (i, j) in visited:
                return False
            return True

        def dfs(i, j, cur):
            if cur == size - 1 and board[i][j] == word[cur]:
                return True
            
            if not isValid(i, j):
                return False
            
            if board[i][j] != word[cur]:
                return False

            visited.add((i,j))
            
            for dr, dc in directions:
                if isValid(i + dr, j + dc):
                    if dfs(i + dr, j + dc, cur+1):
                        return True

            visited.remove((i,j))
            return False
            

        for r in range(Rows):
            for c in range(Cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
