class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = collections.deque()
        visit = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottens.append((i,j))
                    visit.add((i,j))
        
        minutes = 0
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while rottens:
            for _ in range(len(rottens)):
                x, y = rottens.popleft()
                for dx, dy in directions:
                    x2, y2 = dx + x, dy + y
                    if -1<x2<len(grid) and -1<y2<len(grid[0]):
                        if grid[x2][y2] == 1 and (x2,y2) not in visit:
                            grid[x2][y2] = 2
                            rottens.append((x2,y2))
                            visit.add((x2,y2))
            if rottens:
                minutes += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
            

        return minutes
                    
                





        
        