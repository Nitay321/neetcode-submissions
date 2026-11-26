class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        dp = {}
        self.maxP = 0

        def dfs(r,c):
            if r<0 or r >= ROWS or c<0 or c >= COLS:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            

            A,B,C,D = 0,0,0,0

            if r+1<ROWS and matrix[r][c] < matrix[r+1][c]:
                A = dfs(r+1,c)
            if 0<=r-1 and matrix[r][c] < matrix[r-1][c]:
                B = dfs(r-1,c)
            if c+1<COLS and matrix[r][c] < matrix[r][c+1]:
                C = dfs(r,c+1)
            if 0<=c-1 and matrix[r][c] < matrix[r][c-1]:
                D = dfs(r,c-1)


            
            dp[(r,c)] = 1 + max(A,B,C,D)


            return dp[(r,c)] 




        for r in range(ROWS):
            for c in range(COLS):
                count_path = dp[(r,c)] if (r,c) in dp else dfs(r,c)
                self.maxP = max(self.maxP, count_path)
        return self.maxP
        