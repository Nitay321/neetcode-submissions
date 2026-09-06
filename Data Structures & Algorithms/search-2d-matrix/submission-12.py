class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0]) 
        l, r = 0, row * col - 1

        while l<=r:
            m = (l + r) // 2
            j = m % col
            i = m // col
            
            if matrix[i][j] < target:
                l = m + 1
            elif matrix[i][j] > target:
                r = m - 1
            else:
                return True
        return False



        