# 代码随想录算法训练营第五十天 ｜拓扑排序、dijkstra（朴素版）精讲

## [拓扑排序](https://kamacoder.com/problempage.php?pid=1191)

> 文章讲解：https://www.programmercarl.com/kamacoder/0117.软件构建.html#其他语言版本

### 思路

主要还是bfs的思想，判断拓扑顺序，也就是找到有向图的线形结构，主要思想是：
* 找到入度为0的节点，入队。入度为0说明该节点是根节点
* 在bfs循环处理队列中，将入度为0 的节点出队放入到结果集中，并将该节点的边删掉，更新入度的列表
* 遍历入度的列表，找到入度为0的节点，再次将其放入结果集中。
另外，需要注意的是，最后输出的结果集的大小应该与节点个数一致，如果不一致说明存在环。

### Python代码
```python {.line-numbers}
from collections import defaultdict,deque

def tpsort(filedict, indegree):
    que = deque()
    for i in range(len(indegree)):
        if indegree[i] == 0:
            que.append(i)
    res = []
    while que:
        cur = que.popleft()
        res.append(cur)
        # print(f"每次加入入度为0的节点的res{res}")
        cur_record = filedict[cur]
        if cur_record:
            for i in cur_record:
                indegree[i] -= 1
                # print(f"每次更新入度：{indegree}")
                if indegree[i] == 0:
                    que.append(i)
    return res

if __name__ == "__main__":
    n, m = map(int, input().split())
    filedict = defaultdict(list)
    indegree = [0] * n
    for _ in range(m):
        s, t = map(int, input().split())
        filedict[s].append(t)
        indegree[t] += 1
    # print(filedict, indegree)
    res = tpsort(filedict, indegree)
    if len(res) != n:
        print(-1)
    else:
        print(" ".join(map(str, res)))
```

***

## [dijkstra（朴素版）精讲](https://kamacoder.com/problempage.php?pid=1047)

> 文章讲解：https://www.programmercarl.com/kamacoder/0047.参会dijkstra朴素.html#其他语言版本

### 思路

dijkstra算法和prim算法的很类似，区别在于prim算法在更新minDist数组时，是非生成树节点到生成树的最小值，而dijkstra是未访问的节点到源节点的最小值，是在累加的。整体思路还是一样的：
* 找到未访问的节点距离源节点的最近的节点
* 标记为已访问
* 更新minDist数组，更新该节点距离已访问节点的距离

### Python代码
```python {.line-numbers}
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

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [[float('inf')] * (n+1) for _ in range(n+1)]
    for _ in range(m):
        s, e, v = map(int, input().split())
        grid[s][e] = v
    minDist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    res = dijkstra(minDist, grid, visited)
    if res == float('inf'):
        print(-1)
    else:
        print(dijkstra(minDist, grid, visited))
```