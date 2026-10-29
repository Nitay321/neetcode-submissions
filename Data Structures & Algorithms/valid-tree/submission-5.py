class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # connectity 
        # no-circle
        # output: Bool
        E = collections.defaultdict(list)

        for a,b in edges:
            E[a].append(b)
            E[b].append(a)


        q = collections.deque([(0, -1)])
        visit = set() 

        while q:
            v, father = q.popleft()

            if v in visit:
                return False

            visit.add(v)

            for u in E[v]:
                if u != father:
                    q.append((u,v))

        
        return len(visit) == n
          






