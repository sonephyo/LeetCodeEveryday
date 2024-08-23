class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == "1":

                    count += 1
                    self.do_dfs(grid, i,j)
        return count


    def do_dfs(self, grid, x, y):
        if (x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])):
            return
        if (grid[x][y] == "0"):
            return

        grid[x][y] = "0"

        self.do_dfs(grid, x+1, y)
        self.do_dfs(grid, x-1, y)
        self.do_dfs(grid, x, y+1)
        self.do_dfs(grid, x, y-1)
            