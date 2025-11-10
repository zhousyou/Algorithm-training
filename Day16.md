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

> 文章讲解：https://www.programmercarl.com/0236.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
>

### 思路

首先是要确定二叉树的遍历方式，找到目标节点的公共祖先，要自下而上进行递归回溯，要用后序遍历（左右中）的方式。第二点是递归返回值的判断，在递归函数有返回值的情况下：如果要搜索一条边，递归函数返回值不为空的时候，立刻返回，如果搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，也就是后序遍历中处理中间节点的逻辑（也是回溯）。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q or root is None:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is not None and right is not None:
            return root
        if left is None and right is not None:
            return right
        if left is not None and right is None:
            return left
        else:
            return None
```
