class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ''' 
        dfs:
        1) iterate through every cell in the grid 
        2) if r,c = 1 then increment the i

        '''
        

        rows = len(grid)
        cols = len(grid[0])

        islands = 0
        q = collections.deque()

        def bfs(r,c):
            
            q.append((r,c))
            grid[r][c] = 0 

            while q:
                r, c = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr = dr + r
                    nc = dc + c
                    if (0 <= nr < rows and 0 <= nc < cols
                            and grid[nr][nc] == '1'):
                        # explore if its 1 
                        q.append((nr, nc))
                        grid[nr][nc] = 0 

        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c):
                    bfs(r,c)
                    islands += 1

        return islands 