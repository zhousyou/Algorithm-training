# 代码随想录算法训练营第十二天 ｜Leetcode226.翻转二叉树、Leetcode101.对称二叉树、Leetcode104.二叉树的最大深度、Leetcode111.二叉树的最小深度

## [226 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/description/)

> 文章讲解：https://www.programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
>
> 状态：AC

### Python代码

前序遍历递归的方法：
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            return node
        return dfs(root)
```

中序遍历递归的方法：**不可行，中间节点会被翻转两次**
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)   # 左
            node.left, node.right = node.right, node.left  #处理中间节点
            
            dfs(node.right)  #右
            return node
        return dfs(root)
```
