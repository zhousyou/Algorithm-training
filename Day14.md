# 代码随想录算法训练营第十四天 ｜Leetcode513.找树左下角的值、Leetcode112.路径总和、Leetcode106.从中序与后序遍历序列构造二叉树

## [513.找树左下角的值](https://leetcode.cn/problems/find-bottom-left-tree-value/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0513.%E6%89%BE%E6%A0%91%E5%B7%A6%E4%B8%8B%E8%A7%92%E7%9A%84%E5%80%BC.html   

### 思路

用迭代层序遍历的方法来做很简单，把每一层的节点记录下来，然后找到`res[-1][0]`的值就可以了。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = collections.deque([root])
        res = []
        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                level.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            res.append(level)
        return res[-1][0]
```

*** 

### [112.路径总和](https://leetcode.cn/problems/path-sum/description/)

> 文章讲解：题目链接/文章讲解/视频讲解：https://programmercarl.com/0112.%E8%B7%AF%E5%BE%84%E6%80%BB%E5%92%8C.html   

### 思路

重点是回溯的思想，以及递归返回值的判断，什么时候要写返回值，什么时候不写返回值。112路径总和，是判断是否有满足条件的路径，遇到就返回，所以是需要对返回值进行判断的。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node, sum):
        if not node.left and not node.right and sum == 0:
            return True 
        if not node.left and not node.right :
            return False
         
        if node.left:
            sum -= node.left.val
            if self.dfs(node.left, sum): 
                return True
            sum += node.left.val
        if node.right:
            sum -= node.right.val
            if self.dfs(node.right, sum):
                return True
            sum += node.right.val
        return False  

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
      

        return self.dfs(root, targetSum-root.val)
```
