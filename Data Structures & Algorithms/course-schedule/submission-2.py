class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[pre].append(crs)
        
        states = [0] * numCourses
        def dfs(node):
            if states[node] == 1:
                return False
            if states[node] == 2:
                return True

            states[node] = 1
            for nb in adj[node]:
                if not dfs(nb):
                    return False
            states[node] = 2
            return True

        return all(dfs(i) for i in range(numCourses))