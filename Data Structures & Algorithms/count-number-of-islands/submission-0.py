class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visit = set()
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit
                            and grid[nr][nc] == '1'):
                        # explore if its 1 
                        visit.add((nr,nc))
                        q.append((nr, nc))

        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1

        return islands 