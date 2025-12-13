from collections import deque

directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
count = 0

def dfs(grid, visited, x, y):
    global count
    for i, j in directions:
        next_x, next_y = x + i, y + j
        if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
            continue
        if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
            visited[next_x][next_y] = True
            count += 1
            dfs(grid, visited, next_x, next_y)

def bfs(grid, visited, x, y):
    global count
    que = deque([])
    que.append([x, y])
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in directions:
            next_x, next_y = cur_x + i, cur_y + j
            if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                count += 1
                bfs(grid, visited, next_x, next_y)

def main():
    global count
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    visited = [[False for _ in range(m)] for _ in range(n)]
    max_island_size = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                count = 1
                bfs(grid, visited, i, j)

                max_island_size = max(max_island_size, count)
    print(max_island_size)
if __name__ == "__main__":
    main()