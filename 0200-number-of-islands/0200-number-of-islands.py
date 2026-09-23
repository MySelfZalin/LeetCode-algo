class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_range(r, c):
            return 0 <= r < rows and 0 <= c < columns

        def fill(r, c):
            grid[r][c] = "0"

            for dr, dc in vectors:
                nr, nc = dr + r, dc + c
                if in_range(nr, nc) and grid[nr][nc] == "1":
                    fill(nr, nc)

        
        res = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    res += 1
                    fill(r, c)
        
        return res
