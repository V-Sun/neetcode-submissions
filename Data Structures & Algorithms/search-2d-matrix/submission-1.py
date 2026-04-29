class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rows, Cols = len(matrix), len(matrix[0])
        l, r = 0, (Rows*Cols) - 1
        while(l <= r):
            mid = l + ((r-l)//2)
            row, col = mid//Cols, mid%Cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
                