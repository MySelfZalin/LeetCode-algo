class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        queue = collections.deque()
        islands = 0
        
        def check_queue():
            while queue:
                r, c = queue.popleft()

                if grid[r][c] == "1":
                    grid[r][c] = "#"
                    
                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        dr, dc = r+dr, c+dc
                        if 0 <= dr < rows and 0 <= dc < columns:
                            queue.append((dr, dc))


        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    queue.append((row,column))
                    check_queue()
        return islands            
