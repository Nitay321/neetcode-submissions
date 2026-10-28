class Solution:
    def solve(self, board: List[List[str]]) -> None:
        safe = set()

        def dfs(r, c): # find all the safe Os
            if (r, c) in safe or not (-1 < r <ROWS and -1 < c < COLS) or board[r][c] == "X":
                return
            safe.add((r,c))

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs(r,0)
            if board[r][COLS-1] == "O":
                dfs(r,COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                 dfs(0,c)
                
            if board[ROWS-1][c] == "O":
                 dfs(ROWS-1,c)  

        for r in range(ROWS):      
            for c in range(COLS):
                if board[r][c] == "O" and (r,c) not in safe:
                     board[r][c] = "X"
            

        