class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating a graph
        E = collections.defaultdict(list)

        for a, b in prerequisites:
            E[b].append(a)
        
        visit = set()
        visited = set()

        def dfs(v): 
            if v in visit:
                return True  # Cycle detected

            visit.add(v)
            

            for u in E[v]:
                if u not in visited and dfs(u):
                    return True  # cycle signal

            visit.remove(v)  # Backtrack
            visited.add(v)
            return False     # No cycle down this path

        for v in range(numCourses):
            if v not in visited and dfs(v):       # If a cycle IS found...
                return False # we can't finish all courses

        return True  # Loop finished with zero cycles found!