# 代码随想录算法训练营第四十三天 ｜LeetCode98. 所有可达路径

## [98. 所有可达路径](https://leetcode.cn/problems/all-paths-from-source-to-target/submissions/683994205/)

> 文章讲解：https://www.programmercarl.com/kamacoder/0098.%E6%89%80%E6%9C%89%E5%8F%AF%E8%BE%BE%E8%B7%AF%E5%BE%84.html  

### 思路

主要是深度搜索的思想，也就是之前回溯的方式。还是比较简单的

### Python代码

leetcode ：
```python {.line-numbers}
class Solution:
    def dfs(self, graph, path, x, n, res):
        if x==n:
            res.append(path[:])
            # print(res)
            return
        
        for i in range(len(graph[x])):
            path.append(graph[x][i])
            self.dfs(graph, path, graph[x][i], n, res)
            path.pop()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = [0]
        self.dfs(graph, path, 0, len(graph)-1, res)
        return res
```

ACM:
```python {.line-numbers}

def dfs(graph, res, path, x, n):
    if x == n:
        res.append(path[:])
        return
    
    for i in range(n+1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph, res, path, i, n)
            path.pop()

def main():
    n, m = map(int,input().split())
    graph = [[0] * (n+1) for _ in range(n+1)]

    for i in range(m):
        s, t = map(int, input().split())
        graph[s][t] = 1
    
    res = []
    path = [1]

    dfs(graph, res, path, 1, n)
    
    if not res:
        print(-1)
    else:
        for path in res:
            print(' '.join(map(str, path)))

main()
```

***