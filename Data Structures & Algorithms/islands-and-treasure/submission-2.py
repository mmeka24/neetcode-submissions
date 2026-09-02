class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        INF = 2147483647
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: 
                    # its a chest 
                    q.append((r,c))


        directions = [1, 0], [-1, 0], [0, 1], [0, -1]
        while q: 
            # going to find the neightbors of one of the 0 chests
            r, c = q.popleft()
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc 

                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == INF:
                    grid[new_r][new_c] = 1 + grid[r][c]
                    q.append((new_r, new_c))



        