# 代码随想录算法训练营第十六天 ｜Leetcode530.二叉搜索树的最小绝对差 、Leetcode 501.二叉搜索树中的众数 、Leetcode 236. 二叉树的最近公共祖先

## [530 二叉搜索树的最小绝对差](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/)

> 题目链接/文章讲解：https://programmercarl.com/0530.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E5%B0%8F%E7%BB%9D%E5%AF%B9%E5%B7%AE.html  
>
> 视频讲解：https://www.bilibili.com/video/BV1DD4y11779  
> 

### 思路

二叉搜索树都可以考虑用中序遍历的方式，将其变为一个递增的数组的方式来进行判断。

### Python代码

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.stack.append(node.val)
        self.dfs(node.right)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        res = float('inf')
        for i in range(len(self.stack)-1):
            res = min(res, self.stack[i+1]-self.stack[i])
        return res
```

***

## [501.二叉搜索树中的众数](https://leetcode.cn/problems/find-mode-in-binary-search-tree/description/)

> 文章讲解：https://programmercarl.com/0501.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E4%BC%97%E6%95%B0.html   
>
> 视频讲解：https://www.bilibili.com/video/BV1fD4y117gp   

### 思路

和上面一道题很类似，就是将二叉搜索树转化为一个递增的数组，在用字典的方式进行判断。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.stack = []
    def dfs(self, node):
        if not node:
            return 
        self.dfs(node.left)
        self.stack.append(node.val)
        self.dfs(node.right)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.dfs(root)
        count = Counter(self.stack)
        most_val = count.most_common(1)[0][1]
        res = []
        for key, freq in count.items():
            if freq == most_val:
                res.append(key)
        return res
```

***

## [236. 二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/)