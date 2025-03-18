from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        inDegree = [0] * numCourses
        adj = defaultdict(list)
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        for nodes in adj.values():
            for node in nodes:
                inDegree[node] += 1
        
        q = deque([i for i in range(numCourses) if inDegree[i] == 0])
        ans = []
        
        while q:
            node = q.popleft()
            ans.append(node)
            for ngbr in adj[node]:
                inDegree[ngbr] -= 1
                if inDegree[ngbr] == 0:
                    q.append(ngbr)
        
        ans.reverse()
        return ans if len(ans) == numCourses else []