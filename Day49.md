# 代码随想录算法训练营第四十九天 ｜最小生成树之prim

## [最小生成树之prim](https://kamacoder.com/problempage.php?pid=1053)

> 文章讲解：https://www.programmercarl.com/kamacoder/0053.寻宝-prim.html#其他语言版本

### 思路

最小生成树prim问题主要分三步
* 找到非生成树距离生成树最近的节点
* 加入生成树
* 更新非生成树节点到生成树的最小距离
其中`minDist`数组表示的是非生成树节点到生成树的最小距离。

### Python代码
```python {.line-numbers}
v, e = map(int, input().split())
visited = [False] * (v+1)
minDist = [float('inf')] * (v + 1)
grid = [[float('inf')]*(v+1) for _ in range(v+1)]

for _ in range(e):
    x, y, value= map(int, input().split())
    grid[x][y] = value
    grid[y][x] = value

for i in range(1, v+1):
    cur = 1
    minval = float('inf')
    for j in range(1, v+1):
        if visited[j] == False and minDist[j] < minval:
            minval = minDist[j]
            cur = j
    
    visited[cur] = True
    for j in range(1, v+1):
        if visited[j] == False and grid[cur][j] < minDist[j]:
            # print(f"更新minDist,当前节点{cur},最短距离{grid[cur][j]},minDist中最短距离{minDist[j]}")
            minDist[j] = grid[cur][j]
    # print(minDist)
res = 0

for i in minDist:
    if i == float('inf'):
        continue
    res += i

print(res)

```