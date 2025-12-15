# 代码随想录算法训练营第四十七天 ｜107. 寻找存在的路径

## [107. 寻找存在的路径](https://kamacoder.com/problempage.php?pid=1179)

> 文章讲解：https://www.programmercarl.com/kamacoder/0107.%E5%AF%BB%E6%89%BE%E5%AD%98%E5%9C%A8%E7%9A%84%E8%B7%AF%E5%BE%84.html 

### 思路

并查集问题的模板思路，详细看代码了

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
    n, m = map(int, input().split())

    obj = Uionfind(n + 1)
    for _ in range(m):
        s, t = map(int, input().split())
        obj.join(t, s)
    
    src, det = map(int, input().split())
    if obj.isSame(src, det):
        print(1)
    else:
        print(0)
```
