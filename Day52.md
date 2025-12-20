# 代码随想录算法训练营第五十一天 ｜Bellman_ford 队列优化算法、bellman_ford之判断负权回路、bellman_ford之单源有限最短路

## [Bellman_ford 队列优化算法](https://kamacoder.com/problempage.php?pid=1152)

> 文章讲解：https://www.programmercarl.com/kamacoder/0094.城市间货物运输I-SPFA.html#其他语言版本

### 思路

队列优化的思想就是，在进行每一条边的松弛时，有一些节点的距离是不需要更新的，因为不与源节点相连，所以minDist中的值为极大值。通过队列优化的方式将这些值优化掉。真正有效的松弛，是基于已经计算过的节点在做的松弛。具体的思想是将首先要将图通过邻接表的方式创建，然后将源节点入队，每次更新和源节点相连的节点的最短距离，并将相连的节点再次入队。

### Python代码
```python {.line-numbers}
from collections import deque

class Edge:
    def __init__(self, to, val):
        self.to = to 
        self.val = val

def Bellman_ford(grid, minDist):
    # cur = 1
    minDist[1] = 0

    for _ in range(1, len(minDist)-1):
        updated = False
        for edge in grid:
            # if minDist[edge[0]] != float('inf'):
            #     minDist[edge[1]] = min(minDist[edge[1]], minDist[edge[0]] + edge[2])
            #     updated = True
            if minDist[edge[0]] != float('inf') and minDist[edge[1]] > minDist[edge[0]] + edge[2]:
                minDist[edge[1]] = minDist[edge[0]] + edge[2]
                updated = True
        if not updated:
            break
    return minDist[-1]

def SPFA(grid, minDist, visited):
    minDist[1] = 0
    que = deque()
    que.append(1)
    visited[1] = True
    while que:
        cur = que.popleft()
        visited[cur] = False
        for edge in grid[cur]:
            if minDist[edge.to] > minDist[cur] + edge.val:
                minDist[edge.to] = minDist[cur] + edge.val
            if visited[edge.to] == False:
                que.append(edge.to)
                visited[edge.to] = True
    return minDist[-1]
if __name__ == "__main__":
    n, m = map(int, input().split())
    # grid = [] * (m+1)
    # for _ in range(m):
    #     src, dst, val = map(int, input().split())
    #     grid.append([src, dst, val])
    
    grid = [[] for _ in range(n+1)]
    for _ in range(m):
        src, dst, val = map(int, input().split())
        grid[src].append(Edge(dst, val))

    visited = [False] * (n+1)
    minDist = [float('inf')] * (n+1)
    # res = Bellman_ford(grid, minDist)
    res = SPFA(grid, minDist, visited)
    if res == float('inf'):
        print("unconnected")
    else:
        print(res)
```

***

## [bellman_ford之判断负权回路](https://kamacoder.com/problempage.php?pid=1153)

> 文章讲解：https://www.programmercarl.com/kamacoder/0095.城市间货物运输II.html#思路

### 思路

负权回路的思想在于之前的没有负权回路的bellman_ford算法只需要松弛n-1次，再继续松弛也不会改变最终的结果。但加入了负权回路之后，每次达到n-1次之后，再继续松弛，每次都会在环路里循环，每次都会更新minDist数组，会得到更小的结果。所以只需要判断第n次松弛和n-1次松弛的结果是否一致，就能判断是否存在负权回路。

### Python代码
```python {.line-numbers}

def Bellman_ford(grid, minDist):
    minDist[1] = 0
    flag = False
    for i in range(1, len(minDist)):
        for src, dst, val in grid:
            if i < len(minDist)-1:
                if minDist[dst] > minDist[src] + val and minDist[src] != float('inf'):
                    minDist[dst] = minDist[src] + val
            if i == len(minDist) - 1:
                if minDist[dst] > minDist[src] + val and minDist[src] != float('inf'):
                    flag = True
    if flag:
        print("circle")
    elif minDist[-1] == float('inf'):
        print("unconnected")
    else:
        print(minDist[-1])


if __name__ == "__main__":

    n, m = map(int, input().split())
    grid = []
    for _ in range(m):
        src, dst, val = map(int, input().split())
        grid.append([src, dst, val])
    minDist = [float('inf')] * (n+1)
    Bellman_ford(grid, minDist)
```

*** 

## [bellman_ford之单源有限最短路](https://kamacoder.com/problempage.php?pid=1154)

> 文章讲解：https://www.programmercarl.com/kamacoder/0096.城市间货物运输III.html

### 思路

之前提到的：**对所有边松弛一次，相当于计算 起点到达 与起点一条边相连的节点 的最短距离。** 所以当指定了中间的有限节点n时，就相当于指定了边的个数n+1，也就指定了松弛的次数n+1，表示：起点 与起点n+1条边相连的节点的 最短距离。而且由于导入了负权回路，每次松弛要用一个备用数组minDist_copy在上一次的结果上进行更新。

### Python代码
```python {.line-numbers}

def Bellman_ford(grid, minDist, start, end, k):
    minDist[start] = 0
    for _ in range(k+1):
        minDist_copy = minDist.copy()
        for src, dst, val in grid:
            if minDist_copy[src] != float('inf') and minDist[dst] > minDist_copy[src] + val:
                minDist[dst] = minDist_copy[src] + val
    if minDist[end] == float('inf'):
        print("unreachable")
    else:
        print(minDist[end])

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = []
    for _ in range(m):
        src, dst, val = map(int, input().split())
        grid.append([src, dst, val])

    start, end, k = map(int, input().split())
    minDist = [float('inf')] * (n+1)
    Bellman_ford(grid, minDist, start, end, k)
```