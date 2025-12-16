# 代码随想录算法训练营第四十八天 ｜冗余连接、冗余连接II

## [冗余连接](https://kamacoder.com/problempage.php?pid=1181)

> 文章讲解：https://www.programmercarl.com/kamacoder/0108.冗余连接.html

### 思路

这道题也是并查集的一种应用

### Python代码
```python {.line-numbers}
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
 
if __name__ == "__main__":
    n = int(input())
    obj = Uionfind(n+1)
    for _ in range(n):
        s, t = map(int, input().split())
        if obj.isSame(s, t):
            print(s, t)
        else:
            obj.join(t,s)
```

***

## [冗余连接II](https://kamacoder.com/problempage.php?pid=1182)

> 文章讲解：https://www.programmercarl.com/kamacoder/0109.冗余连接II.html

### 思路

有点复杂，需要考虑的情况比较多，从有向图每个节点的度上分析，分为三种情况：
* 如果我们找到入度为2的点，那么删一条指向该节点的边就行了
* 只能删特定的一条边
* 如果没有入度为2的点，说明 图中有环了（注意是有向环

### Python代码
```python {.line-numbers}
from collections import defaultdict
class Uionfind:
    def __init__(self, n):
        self.father = list(range(n + 1))
        self.edges = []
        self.inDegree = defaultdict(int)
        self.size = n
        self.vec = []
 
     
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
 
    def isTree(self):
        for i in range(len(self.edges)):
            if i == self.vec[0]:
                continue
            s, t = self.edges[i]
            if self.isSame(s, t):
                return False
            else:
                self.join(s,t)
        return True
     
    def getRemoveEdge(self):
        for i in range(len(self.edges)):
            s, t = self.edges[i]
            if self.isSame(s,t):
                print(s, t)
                return
            else:
                self.join(s,t)
 
 
 
if __name__ == "__main__":
 
    n = int(input())
    obj = Uionfind(n)
    for _ in range(n):
        s, t = map(int, input().split())
        obj.edges.append([s,t])
        obj.inDegree[t] += 1
 
    for i in range(n-1, -1, -1):
        if obj.inDegree[obj.edges[i][1]] == 2:
            obj.vec.append(i)
     
    if len(obj.vec) > 0:
        if obj.isTree():
            print(obj.edges[obj.vec[0]][0], obj.edges[obj.vec[0]][1])
        else:
            print(obj.edges[obj.vec[1]][0], obj.edges[obj.vec[1]][1])
    else:
        obj.getRemoveEdge()
```