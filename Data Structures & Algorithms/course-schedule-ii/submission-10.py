class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        E = collections.defaultdict(list)

        for a,b in prerequisites:
            E[a].append(b)

        
        res = []
        visited = set()
        visit = set()


        def dfs(v):
            if v in visited:
                return True
            
            if v in visit:
                visit.remove(v)
                return False

            visit.add(v)

            for u in E[v]:
                if not dfs(u):
                    return False
            
            res.append(v)
            visited.add(v)
            visit.remove(v)
            return True
        
        for v in range(numCourses):
            if not dfs(v):
                return []

        if len(res) == numCourses:
            return res

        return [] 
        
            





        
    

         

        
        