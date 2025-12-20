# 代码随想录算法训练营第五十一天 ｜dijkstra（堆优化版）精讲、Bellman_ford算法

## [dijkstra（堆优化版）精讲](https://kamacoder.com/problempage.php?pid=1047)

> 文章讲解：https://www.programmercarl.com/kamacoder/0047.参会dijkstra堆.html#思路

### 思路

dijkstra朴素版是基于点的判断，类似于prim算法。堆优化版是基于边的判断，类似于kruskal算法。
* 找到未访问的节点距离源节点的最近的节点，这一步直接使用最小堆进行优化，将边放入到最小堆中，每次取出的堆顶元素就是最小值
* 标记为已访问
* 更新minDist数组，更新该节点距离已访问节点的距离，这一步需要将找到的边放入到最小堆中。

### Python代码
```python {.line-numbers}
import heapq

def dijkstra(minDist, grid, visited):
    
    minDist[1] = 0
    for _ in range(1, len(minDist)):
        cur = 1
        minval = float('inf')
        for i in range(1, len(minDist)):
            if minval > minDist[i] and visited[i] == False:
                minval = minDist[i]
                cur = i
        visited[cur] = True

        for i in range(1, len(minDist)):
            if grid[cur][i] != float('inf') and minDist[i] > minDist[cur] + grid[cur][i] and visited[i] == False:
                minDist[i] = minDist[cur] + grid[cur][i]
    # print(minDist)
    return minDist[-1]

class Edge:
    def __init__(self, e, val):
        self.e = e
        self.val = val

def heap_dijkstra(minDist, grid, visited):
    minDist[1] = 0

    pq = []
    heapq.heappush(pq, (0, 1))

    while pq:

        # 第一步，找到未访问的节点距离源节点的最小值
        cur_dist, cur_node = heapq.heappop(pq)

        # 标记为访问过的节点
        visited[cur_node] = True

        # 更新minDist
        for edge in grid[cur_node]:
            if visited[edge.e] == False and minDist[edge.e] > cur_dist+ edge.val:
                minDist[edge.e] = cur_dist + edge.val
                heapq.heappush(pq, (minDist[edge.e], edge.e))
    # print(minDist)
    return minDist[-1]

if __name__ == "__main__":
    # n, m = map(int, input().split())
    # grid = [[float('inf')] * (n+1) for _ in range(n+1)]
    # for _ in range(m):
    #     s, e, v = map(int, input().split())
    #     grid[s][e] = v
    # minDist = [float('inf')] * (n+1)
    # visited = [False] * (n+1)
    # res = dijkstra(minDist, grid, visited)
    # if res == float('inf'):
    #     print(-1)
    # else:
    #     print(dijkstra(minDist, grid, visited))

    ### 堆优化 + 邻接表
    n, m = map(int, input().split())
    grid = [[]for _ in range(n+1)]
    for _ in range(m):
        s, e, v = map(int, input().split())
        grid[s].append(Edge(e,v))
    minDist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    res = heap_dijkstra(minDist, grid, visited)
    if res == float('inf'):
        print(-1)
    else:
        print(res)
```

***

## [Bellman_ford算法](https://kamacoder.com/problempage.php?pid=1152)

> 文章讲解：https://www.programmercarl.com/kamacoder/0094.城市间货物运输I.html

### 思路

和dijkstra算法一样都是解决最短路径的问题，bellman-ford优势在于可以边的权值可以是负数（Dijkstra做不到）。主要思想是：**对所有边进行松弛n-1次操作（n为节点数量），从而求得目标最短路**。松弛指的是对所有边进行遍历，更新源节点的最小路径，翻译成核心代码：
```python 
if minDist[src] != float('inf') and minDist[dst] > minDist[src] + weight:
                minDist[dst] = minDist[src] + weight
```
上述过程要进行n-1次循环，因为**对所有边松弛一次，相当于计算 起点到达 与起点一条边相连的节点 的最短距离**，节点数量为n，那么起点到终点，最多是 n-1 条边相连。

### Python代码
```python {.line-numbers}

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

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [] * (m+1)
    for _ in range(m):
        src, dst, val = map(int, input().split())
        grid.append([src, dst, val])
    
    minDist = [float('inf')] * (n+1)
    res = Bellman_ford(grid, minDist)
    if res == float('inf'):
        print("unconnected")
    else:
        print(res)
```
            