class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        directions = [[1,0], [-1,0], [0, 1], [0, -1]]
        # find the 0s and run bfs and check if they are 0
        def dfs(r, c):
            visited.add((r,c))
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited
                and board[nr][nc] == 'O'): 
                    dfs(nr, nc)

        # figure out the forders
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0) # left side 
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1) # right side

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c) # top 
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c) # bottom

        for r in range(rows):
            for c in range(cols):
                # not in visited bc visited has the same O's
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'
