# 代码随想录算法训练营第四十九天 ｜最小生成树之prim、最小生成树之Kruskal

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

## [最小生成树之Kruskal](https://kamacoder.com/problempage.php?pid=1053)

> 文章讲解：https://www.programmercarl.com/kamacoder/0053.寻宝-Kruskal.html#其他语言版本

### 思路

与prim算法不同，kruskal的算法从边的角度出发，prim算法是从点的角度出发。kruskal的主要思想也是贪心的：
* 对边的权值进行排序
* 每次判断最小权值的边的节点，如果不在一个集合中则加入到最小生成树的集合里
因为也是判断两个节点是否在同一个集合的问题，所以也要用并查集的思想。

### Python代码
```python {.line-numbers}
class Edge:
    def __init__(self, l, r, val):
        self.l = l
        self.r = r
        self.val = val
    
class Uionfind:
    def __init__(self, n):
        self.father = list(range(n+1))
    
    def find(self, u):
        if u == self.father[u]:
            return u 
        else:
            self.father[u] = self.find(self.father[u])
            return self.father[u]
    
    def isSame(self, u, v):
        return self.find(u) == self.find(v)
    
    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.father[v] = u

def Kruskal(edges, n):
    edges.sort(key = lambda edge: edge.val)
    obj = Uionfind(n+1)
    res = 0
    for edge in edges:
        if obj.isSame(edge.l, edge.r) == False:
            obj.join(edge.r, edge.l)
            res += edge.val
    return res 

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        l, r, val = map(int, input().split())
        edge = Edge(l, r, val)
        edges.append(edge)
    
    res = Kruskal(edges, n)
    print(res)
    
```