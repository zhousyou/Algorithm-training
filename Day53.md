# 代码随想录算法训练营第五十三天 ｜Floyd算法、A*算法

## [Floyd 算法](https://kamacoder.com/problempage.php?pid=1155)

> 文章讲解：https://www.programmercarl.com/kamacoder/0097.小明逛公园.html#思路

### 思路

Floyd解决的是多源最短路径的问题，主要的思想是动态规划。重点是dp数组的含义以及遍历顺序：
* dp数组的含义：dp[i][j][k]表示节点i到节点j中间经过[1,k]中任意节点的最短路径。
* 递推公式：
  * 当经过节点k时：dp[i][j][k] = dp[i][k][k-1] + dp[k][j][k-1]
  * 不经过节点k时：dp[i][j][k] = dp[i][j][k-1]
  综上dp[i][j][k] = min(dp[i][k][k-1] + dp[k][j][k-1],dp[i][j][k-1])
* 初始化dp数组：因为求最短距离，所以直接都初始化为极大值。当k = 0时，dp[i][j][0]表示的就是两个节点直接相连的距离
* 遍历dp数组：因为dp数组是一个三维的数组，可以想象成一个xyz三个轴的空间坐标系，我们当前只有k=0时一个平面的值，所以遍历的时候k应该在最外层，i，j在里层。

### Python代码
```python {.line-numbers}
n, m = map(int, input().split())
dp = [[[float('inf')] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    dp[u][v][0] = w
    dp[v][u][0] = w

q = int(input())
start = []
end = []
for _ in range(q):
    s, e = map(int, input().split())
    start.append(s)
    end.append(e)

for k in range(1, n+1):
    for i in range(n+1):
        for j in range(n+1):
            dp[i][j][k] = min(dp[i][k][k-1] + dp[k][j][k-1],
            dp[i][j][k-1])

for i in range(q):
    if dp[start[i]][end[i]][-1] == float('inf'):
        print(-1)
    else:
        print(dp[start[i]][end[i]][-1])
```

***

## [A*算法](https://kamacoder.com/problempage.php?pid=1203)

> 文章讲解：https://www.programmercarl.com/kamacoder/0126.骑士的攻击astar.html#思路

### 思路

A* 算法是优化版的广搜，普通的广搜是遍历图中所有的节点，通过队列不断的入队出队。而优化之后的A*是每次遍历只找到最优的节点，也就是距离目标最近的节点，找到节点的操作是出队的操作，也就是每次都找到队列中最小的值，所以相对于bfs来说，优化的地方就是将队列改为最小堆。
而A*可以实现有方向搜索的关键在于**启发式函数**，这个地方有点说法，目前还不是很理解。感觉就是队列中找到最短的距离，就是通过启发式函数来优化的。

### Python代码
```python {.line-numbers}
import heapq

def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

directions = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]]

n = int(input())

def Astar(start, end):
    q = [(distance(start, end), start)]
    step = {start:0}

    while q:
        dis, cur = heapq.heappop(q)
        if cur == end:
            return step[cur]
        
        for move in directions:
            newmove = (cur[0] + move[0], cur[1] + move[1])
            if 1 <= newmove[0] <= 100 and 1 <= newmove[1] <= 100:
                step_new = step[cur] + 1
                if step_new < step.get(newmove, float('inf')):
                    step[newmove] = step_new
                    heapq.heappush(q, (distance(newmove, end)+step_new , newmove))
    return False

for _ in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    print(Astar((a1, a2), (b1,b2)))
```