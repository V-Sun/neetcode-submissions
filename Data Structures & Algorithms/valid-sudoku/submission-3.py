class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Create hashMaps with sets for each row, col, and square

        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        squares = {(r,c):set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):

                

                # Store our current value for more readable code
                curr = board[r][c]
                if curr == ".":
                    continue
                if curr in rows[r]:
                    return False
                if curr in cols[c]:
                    return False
                if curr in squares[(r//3,c//3)]:
                    return False
                
                rows[r].add(curr)
                cols[c].add(curr)
                squares[(r//3,c//3)].add(curr)


        return True
