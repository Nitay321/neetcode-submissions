class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(x,y):
            q = collections.deque([(x,y)])
            visit = set()
            while q:
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                x, y = q.popleft()

                for dx, dy in directions:
                    x2, y2 = x+dx, y+dy
                    if -1<x2<len(grid) and -1<y2<len(grid[0]) and 0<grid[x2][y2]:
                        if (x2, y2) not in visit:
                            if 1 + grid[x][y] < grid[x2][y2]: 
                                grid[x2][y2] = 1 + grid[x][y]
                                q.append((x2,y2))
                                visit.add((x2,y2))
                            
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    bfs(x,y)
             



            



        

        