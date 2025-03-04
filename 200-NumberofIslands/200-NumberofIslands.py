from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0  # Edge case: empty grid
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: Stop if out of bounds or at water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark current cell as visited
            grid[r][c] = '0'
            
            # Explore all 4 possible directions (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Scan the entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found an island
                    island_count += 1
                    dfs(r, c)  # Mark entire island as visited
        
        return island_count
