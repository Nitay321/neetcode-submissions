class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        self.maxI = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def bfs(i,j):
            q = collections.deque()

            visit.add((i,j))
            q.append((i,j))
            
            countI = 0
            while q:
                i,j = q.popleft()
                countI += 1
                for i2,j2 in directions:
                    x = i + i2
                    y = j + j2
                    if 0 <= x < rows and 0 <= y < cols and (x,y) not in visit and grid[x][y] == 1:
                        q.append((x,y))
                        visit.add((x,y))

            self.maxI = max(self.maxI, countI)
                


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visit:
                    bfs(i,j)

        return self.maxI

        