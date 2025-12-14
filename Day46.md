# 代码随想录算法训练营第四十五天 ｜字符串接龙、有向图的完全可达性、岛屿的周长

## [字符串接龙](https://kamacoder.com/problempage.php?pid=1183)

### Python代码
```python {.line-numbers}
from collections import deque

def judge(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1

if __name__ == "__main__":
    n = int(input())
    beginStr, endStr = input().split()
    strList = []
    for _ in range(n):
        strList.append(input().strip())
    
    visited = [False for _ in range(n)]
    que = deque([])
    que.append((beginStr, 1))
    while que:
        cur_str, step = que.popleft()
        if judge(cur_str, endStr):
            print(step + 1)
            exit(0)
        for i in range(n):
            if not visited[i] and judge(cur_str, strList[i]):
                visited[i] = True
                que.append((strList[i], step + 1))
    print(0)
```

***

## [有向图的完全可达性](https://kamacoder.com/problempage.php?pid=1177)


### Python代码
```python {.line-numbers}

import collections

path = set()  # 纪录 BFS 所经过之节点

def bfs(root, graph):
    global path
    
    que = collections.deque([root])
    while que:
        cur = que.popleft()
        path.add(cur)
        
        for nei in graph[cur]:
            que.append(nei)
        graph[cur] = []
    return

def main():
    N, K = map(int, input().strip().split())
    graph = collections.defaultdict(list)
    for _ in range(K):
        src, dest = map(int, input().strip().split())
        graph[src].append(dest)
    
    bfs(1, graph)
    if path == {i for i in range(1, N + 1)}:
        return 1
    return -1
        

if __name__ == "__main__":
    print(main())
```

***

## [岛屿的周长](https://kamacoder.com/problempage.php?pid=1178)

### Python代码
```python {.line-numbers}
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # 读取 n 和 m
    n = int(data[0])
    m = int(data[1])
    
    # 初始化 grid
    grid = []
    index = 2
    for i in range(n):
        grid.append([int(data[index + j]) for j in range(m)])
        index += m
    
    sum_land = 0    # 陆地数量
    cover = 0       # 相邻数量

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                sum_land += 1
                # 统计上边相邻陆地
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    cover += 1
                # 统计左边相邻陆地
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    cover += 1
                # 不统计下边和右边，避免重复计算
    
    result = sum_land * 4 - cover * 2
    print(result)

if __name__ == "__main__":
    main()
```