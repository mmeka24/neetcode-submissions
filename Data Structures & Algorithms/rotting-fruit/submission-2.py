class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        time = 0
        fresh = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append([r,c])
        
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0:
             
            # this for loop gives me the levels LEVELS ARE V IMPORTANT 
            for i in range(len(q)):
                r,c = q.popleft()
                #directions 
                for dc, dr in directions:
                    n_row = r + dr
                    n_col = dc + c

                    if 0 <= n_row < rows and 0 <= n_col < cols and grid[n_row][n_col] == 1:
                        # markig it to be rotten 
                        grid[n_row][n_col] = 2
                        # decrease the frehs one 
                        fresh -= 1 
                        q.append((n_row,n_col))


            time += 1 

        return time if fresh == 0 else -1   