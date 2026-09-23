class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        def in_range(r, c):
            return 0 <= r < rows and 0 <= c < columns


        def dfs(r, c):
            grid[r][c] = 0

            for dr, dc in vectors:
                nr, nc = dr + r, dc + c
                if in_range(nr, nc) and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        for r in range(rows):
            for c in [0, columns - 1]:
                if grid[r][c] == 1:
                    dfs(r, c)
        
        for c in range(columns):
            for r in [0, rows - 1]:
                if grid[r][c] == 1:
                    dfs(r, c)
        
        return sum(sum(row) for row in grid)



