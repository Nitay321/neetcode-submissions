class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        V = set([])
        E = set([])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    V.add((i,j))

                    if (i-1,j) in V:
                        E.add( ((i-1,j),(i,j)) )
                    if (i,j-1) in V:
                        E.add( ((i,j-1),(i,j)) )

        
        q = collections.deque([])
        visited = set([])
        count = 0

        for v in V:
            if v in visited:
                continue
            
            q.append(v)
            visited.add(v)

            while q:
                for i in range(len(q)):
                    (i,j) = q.popleft()
                    
                    if ((i,j),(i+1,j)) in E and (i+1,j) not in visited:
                        q.append((i+1,j))
                        visited.add((i+1,j))

                    if ((i-1,j),(i,j)) in E and (i-1,j) not in visited:
                        q.append((i-1,j))
                        visited.add((i-1,j))

                    if ((i,j),(i,j+1)) in E and (i,j+1) not in visited:
                        q.append((i,j+1))
                        visited.add((i,j+1))

                    if ((i,j-1),(i,j)) in E and (i,j-1) not in visited:
                        q.append((i,j-1))
                        visited.add((i,j-1))
            count += 1

        return count


            

        

        