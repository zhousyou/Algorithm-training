# 代码随想录算法训练营第四十四天 ｜99.岛屿数量 深搜、岛屿数量 广搜、100.岛屿的最大面积 

## [岛屿数量 深搜](https://kamacoder.com/problempage.php?pid=1171)

> 文章讲解：https://www.programmercarl.com/kamacoder/0099.岛屿的数量深搜.html#思路

### 思路

深搜dfs的思路之前在回溯还有二叉树的遍历中有讲过，基本思路是类似的。在这道题里要定义一个visited数组来记录遍历过的节点。

### Python代码
```python {.line-numbers}
directions = [[0,1],[1,0],[0,-1],[-1,0]]
def dfs(graph, visited, x, y):
    for i, j in directions:
        next_x = x + i
        next_y = y + j

        if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
            continue
        
        if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
            visited[next_x][next_y] = True
            dfs(graph, visited, next_x, next_y)

if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]

    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                res += 1
                visited[i][j] = True
                dfs(graph, visited, i, j)
    print(res)
    # print(visited)
    # print(graph)
```

***

## [岛屿数量 深搜](https://kamacoder.com/problempage.php?pid=1171)

> 文章讲解：https://www.programmercarl.com/kamacoder/0099.岛屿的数量广搜.html

### 思路
在二叉树的遍历中，bfs是要用一个队列来记录根节点，在本题中也是一样的，用队列FIFO的特性来记录遍历过的元素。

### Python代码
```python {.line-numbers}
from collections import deque
directions = [[0,1],[1,0],[0,-1],[-1,0]]
def bfs(graph, visited, x, y):
    que = deque([])
    que.append([x,y])
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        for i, j in directions:
            next_x = x + i
            next_y = y + j
            if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
                continue
            if not visited[next_x][next_y] and graph[next_x][next_y] == 1:
                visited[next_x][next_y] = True
                bfs(graph, visited, next_x, next_y)

def main():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]

    res = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                res += 1
                visited[i][j] = True
                bfs(graph, visited, i, j)
    print(res)

main()
```

***

## [100.岛屿的最大面积 ](https://kamacoder.com/problempage.php?pid=1172)

> 文章讲解：https://www.programmercarl.com/kamacoder/0100.岛屿的最大面积.html

### 思路

和上面的题一致，只不过改了一下处理节点的逻辑，需要定一个全局变量来记录遍历过的节点的数量。

### Python代码
``` python {.line-numbers}
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
```
