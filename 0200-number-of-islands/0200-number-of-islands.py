class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        queue = collections.deque()
        islands = 0
        
        def check_queue():
            while queue:
                r, c = queue.popleft()
                if r < 0 or c < 0 or r >= rows or c >= columns:
                    continue

                if grid[r][c] == "1":
                    grid[r][c] = "#"
                    queue.append((r+1,c))
                    queue.append((r-1,c))
                    queue.append((r,c+1))
                    queue.append((r,c-1))

        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    queue.append((row,column))
                    check_queue()
        return islands            
