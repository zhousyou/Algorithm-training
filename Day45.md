# 代码随想录算法训练营第四十五天 ｜101.孤岛的总面积、沉没孤岛、水流问题、104.建造最大岛屿

## [101.孤岛的总面积](https://kamacoder.com/problempage.php?pid=1173)

> 文章讲解：https://www.programmercarl.com/kamacoder/0101.孤岛的总面积.html#思路

### 思路：
思路是把边界的值通过dfs转化为0，剩下的就是孤岛的值，最后求和

### Python代码
```python {.line-numbers}
directions = [[0,1], [1,0], [0,-1],[-1,0]]
from collections import deque
def dfs(graph, x, y):
    graph[x][y] = 0
    for i, j in directions:
        next_x = x + i 
        next_y = y + j

        if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
            continue

        if graph[next_x][next_y] == 1:
            # graph[next_x][next_y] == 0
            dfs(graph, next_x, next_y)
            
def bfs(graph, x, y):
    graph[x][y] = 0
    que = deque([])
    que.append([x, y])
    while que:
        cur_x, cur_y = que.popleft()
        for i, j in directions:
            next_x = cur_x + i 
            next_y = cur_y + j
            if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
                continue
            if graph[next_x][next_y] == 1:
                bfs(graph, next_x, next_y)

def main():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    # visited = [[False] * m for _ in range(n)]
    for i in range(n):
        if graph[i][0] == 1:
            bfs(graph, i, 0)
        if graph[i][m-1] == 1:
            bfs(graph, i, m-1)
    
    for j in range(m):
        if graph[0][j] == 1:
            bfs(graph, 0, j)
        if graph[n-1][j] == 1:
            bfs(graph, n-1, j)
    res = 0
    
    for g in graph:
        res += sum(g)
    print(res)
    # print(graph)


main()
```

***

## [沉没孤岛](https://kamacoder.com/problempage.php?pid=1174)

> 文章讲解：https://www.programmercarl.com/kamacoder/0102.沉没孤岛.html#思路

### 思路

和上一道思路类似，先将边缘的值转化为特殊的值，比如转化为2，剩下的值就都是孤岛和海水，都转化成0，在将边缘的值转化为1即可。最开始我的想法是直接找到孤岛的位置将其转化为0，结果行不通

### Python代码
```python {.line-numbers}
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def dfs(graph, x, y):
    graph[x][y] = 2
    for i, j in directions:
        next_x = x + i 
        next_y = y + j

        if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
            continue

        if graph[next_x][next_y] == 1:
            dfs(graph, next_x, next_y)

def main():
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    # visited = [[False] * m for _ in range(n)]
    for i in range(n):
        if graph[i][0] == 1:
            dfs(graph, i, 0)
        if graph[i][m-1] == 1:
            dfs(graph, i, m-1)
    
    for j in range(m):
        if graph[0][j] == 1:
            dfs(graph, 0, j)
        if graph[n-1][j] == 1:
            dfs(graph, n-1, j)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                graph[i][j] = 1
            elif graph[i][j] == 1:
                graph[i][j] = 0
    for i in graph:
        print(" ".join(map(str, i)))
main()
```

***

## [水流问题](https://kamacoder.com/problempage.php?pid=1175)

> 文章讲解：https://www.programmercarl.com/kamacoder/0103.水流问题.html

### 思路

本题的优化思路有想到，就是从两个边界出发找到能到达的点，并求出两个结果的交集

### Python代码
```python {.line-numbers}
directions = [[0,1], [1,0], [0,-1],[-1,0]]
first = set()
second = set()

def dfs(graph, visited, x, y, side):
    if visited[x][y]:
        return
    visited[x][y] = True
    side.add((x,y))
    for i, j in directions:
        next_x = x + i
        next_y = y + j

        # if next_x < 0 or next_x >= len(graph) or next_y < 0 or next_y >= len(graph[0]):
        #     continue
        # if graph[next_x][next_y] >= graph[x][y]:
        #     dfs(graph, visited, next_x, next_y, side)
        if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]) and graph[next_x][next_y] >= graph[x][y]:
            dfs(graph, visited, next_x, next_y, side)

def main():
    global first
    global second
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        dfs(graph, visited, i, 0, first)
    for j in range(m):
        dfs(graph, visited, 0, j, first)

    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        dfs(graph, visited, i, m-1, second)
    for j in range(m):
        dfs(graph, visited, n-1, j, second)
    
    res = first & second
    for x,y in res:
        print(f"{x} {y}")

main()
```

*** 

## [104.建造最大岛屿](https://kamacoder.com/problempage.php?pid=1176)

> 文章讲解：https://www.programmercarl.com/kamacoder/0104.建造最大岛屿.html

### 思路

有点复杂，没有想到思路，看了题解才想清楚，首先要记录每块岛屿的面积，在进行遍历找到每个海水的位置，并将其与周边的岛屿连接，找到最大的结果。

### Python代码
```python {.line-numbers}

directions = [[0,1], [1,0], [0,-1],[-1,0]]
count = 0
from collections import defaultdict
def dfs(graph, visited, x, y, mark):
    global count
    if visited[x][y] :
        return
    visited[x][y] = True
    graph[x][y] = mark
    count += 1

    for i, j in directions:
        next_x = x + i
        next_y = y + j

        if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]) and graph[next_x][next_y] != 0:
            dfs(graph, visited, next_x, next_y, mark)

def main():
    global count 
    n, m = map(int, input().split())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    visited = [[False] * m for _ in range(n)]

    mark = 2
    record = defaultdict(int)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                count = 0
                dfs(graph, visited, i, j, mark)
                record[mark] = count
                mark += 1
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                max_is = 1
                graph[i][j] = 1
                v = set()
                for x, y in directions:
                    next_x = x + i
                    next_y = y + j

                    if 0 <= next_x < len(graph) and 0 <= next_y < len(graph[0]) and graph[next_x][next_y] != 0 and graph[next_x][next_y] not in v:
                        max_is += record[graph[next_x][next_y]]
                        v.add(graph[next_x][next_y])
                res = max(res, max_is)
    if res == 0:
        print(max(record.values()))
    else:
        print(res)
main()

```
