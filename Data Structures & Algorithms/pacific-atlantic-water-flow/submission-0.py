class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        
        pacific = set()
        atlantic = set()
        directions = [[0,1], [0, -1], [1,0], [-1,0]]

        def dfs(r, c, visit):
            visit.add((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and          # in bounds
                0 <= nc < cols and          # in bounds  
                (nr, nc) not in visit and # not already visited
                heights[nr][nc] >= heights[r][c]):   # uphill ok
                
                    dfs(nr, nc, visit) 

        
        for r in range(rows):
            dfs(r, 0, pacific) # pacific edge 
            dfs(r, cols - 1, atlantic) # atlantic edge 

        for c in range(cols): 
            dfs(rows - 1, c, atlantic) # lower atlantic 
            dfs(0 ,c, pacific) # upper pacific 

        return [list(cell) for cell in pacific & atlantic]


