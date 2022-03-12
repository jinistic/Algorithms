from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i, j - 1)
                dfs(i + 1, j)
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count

    """
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    node = [(i, j)]
                    while node:
                        x, y = node.pop()
                        visited[x][y] = True
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if (
                                0 <= nx < m
                                and 0 <= ny < n
                                and grid[nx][ny] == "1"
                                and not visited[nx][ny]
                            ):
                                node.append((nx, ny))
                    cnt += 1
        return cnt
    """


sol = Solution()
print(
    sol.numIslands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
print(
    sol.numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
