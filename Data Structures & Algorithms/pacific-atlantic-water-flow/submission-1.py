class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac, atl = set(), set()
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            pac.add((r, 0))
            atl.add((r, n - 1))
        for c in range(n):
            pac.add((0, c))
            atl.add((m - 1, c))
        
        def bfs(source):
            q = deque(source)
            while q:
                r, c = q.popleft()
                source.add((r, c))            
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in source and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))

        bfs(pac)
        bfs(atl)

        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
