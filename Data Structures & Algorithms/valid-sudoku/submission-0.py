class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        squares = {(r,c):set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):
                temp = board[r][c]
                if board[r][c] == ".":
                    continue
                
                if (temp in rows[r] or temp in cols[c] or temp in squares[(r // 3, c//3)]):
                    return False
                
                rows[r].add(temp)
                cols[c].add(temp)
                squares[(r//3,c//3)].add(temp)
            
        return True