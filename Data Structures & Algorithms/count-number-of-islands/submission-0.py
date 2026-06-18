from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        n = len(grid)
        m = len(grid[0])
        visited = set()

        def bfs(r, c):
            displacements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((r, c))
            cola = deque([(r, c)])
            while cola:
                current_r, current_c = cola.popleft()
                for d in displacements:
                    new_r = current_r + d[0]
                    new_c = current_c + d[1]
                    if new_r < 0 or new_r >= n: continue
                    if new_c < 0 or new_c >= m: continue
                    if grid[new_r][new_c] == "1" and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        cola.append((new_r, new_c))
            return
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in visited:
                    counter += 1
                    bfs(i, j)

        return counter






        