class Solution:

  def validTree(self, n: int, edges: List[List[int]]) -> bool:
    # A tree with n nodes MUST have exactly n - 1 edges
    if len(edges) != n - 1:
      return False

    E = collections.defaultdict(list)
    for a, b in edges:
      E[a].append(b)
      E[b].append(a)

    # With the edge count check, if it's connected, it is guaranteed to have no cycles!
    q = collections.deque([0])
    visited = {0}

    while q:
      node = q.popleft()
      for neighbor in E[node]:
        if neighbor not in visited:
          visited.add(neighbor)
          q.append(neighbor)

    # If we reached all n nodes, it is connected
    return len(visited) == n