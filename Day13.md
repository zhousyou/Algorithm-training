# 代码随想录算法训练营第十三天 ｜Leetcode110.平衡二叉树、Leetcode257.二叉树的所有路径、Leetcode404.左叶子之和、Leetcode222.完全二叉树的节点个数

## [110 平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/description/)

> 文章讲解：https://www.programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

平衡二叉树的重点是所有子树的**高度**差不超过1，高度不同于深度。深度是叶子节点到根节点的节点数，高度是叶子节点到某个节点的节点数。首次尝试递归的方法很轻易的就写成了判断左右子树的深度差不超过1. 我的思路是递归找到两个子树的高度，在主函数里去判断两个高度差是否超过1.如果二叉树是`[1,2,2,3,null,null,4,null,null,4]`时，就会出现问题。所以要在递归的逻辑就判断高度差，如果递归的结果已经不是平衡二叉树了，那么回溯之后上一层的结果也不是二叉树。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left_nodes = self.dfs(node.left)
        right_nodes = self.dfs(node.right)
        # 如果此时左子树不平衡了，直接返回-1
        if left_nodes == -1:
            return -1
        # 如果此时右子树不平衡了，直接返回 -1
        if right_nodes == -1:
            return -1
        # 如果此时左右子树差距超过1，返回-1
        if abs(left_nodes - right_nodes) > 1:
            return -1
        else:
            
            return max(left_nodes, right_nodes) +1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.dfs(root) == -1:
            return False
        left_nums = self.dfs(root.left)
        # print(left_nums)
        right_nums = self.dfs(root.right)
        # print(right_nums)
        if abs(left_nums - right_nums) <= 1:
            return True
        else:
            return False
```

***

## [257 二叉树的所有路径](https://leetcode.cn/problems/binary-tree-paths/description/)

> 文章讲解：https://www.programmercarl.com/0257.%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E6%89%80%E6%9C%89%E8%B7%AF%E5%BE%84.html#%E6%80%9D%E8%B7%AF


### 思路

同样用递归的算法，需要额外维护两个列表，一个列表存储path路径上的节点，一个列表存储res结果。终止条件判断是遇到叶子节点时停止（同时没有左节点与右节点），不能和之前一样遇到空节点再返回，否则没法判断停止条件，会一直回溯，直到列表为空。

### Python代码

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, path, res):
        path.append(node.val)
        if not node.left and not node.right:
            spath = "->".join(map(str, path))
            res.append(spath)
            return
        if node.left:
            self.dfs(node.left, path, res)
            path.pop()
        if node.right:
            self.dfs(node.right, path, res)
            path.pop()
        

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = []
        res = []
        if not root:
            return res
        self.dfs(root, path, res)
        return res
```

***

## [404 左叶子之和](https://leetcode.cn/problems/sum-of-left-leaves/description/)

> 文章讲解：题目链接/文章讲解/视频讲解：https://programmercarl.com/0404.%E5%B7%A6%E5%8F%B6%E5%AD%90%E4%B9%8B%E5%92%8C.html   


### 思路

重点是理解什么情况下能找到左叶子节点。当前节点有左节点，左子节点没有子节点时，是左叶子节点。`if node.left and not node.left.left and not node.left.right`.

### Python代码

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        leftval = self.dfs(node.left)
        rightval = self.dfs(node.right)
        if node.left and not node.left.left and not node.left.right:
            leftval = node.left.val
        sum = leftval + rightval
        return sum
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
```

***

## [222.完全二叉树的节点个数](https://leetcode.cn/problems/count-complete-tree-nodes/description/)

> 文章讲解：题目链接/文章讲解/视频讲解：https://programmercarl.com/0222.%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%8A%82%E7%82%B9%E4%B8%AA%E6%95%B0.html   

### 思路

这道题和平衡二叉树很像，可以说是平衡二叉树的错误解法，求节点个数就是完全遍历左子树和右子树，相当于求树的深度，比较简单。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left_nums = self.dfs(node.left)
        right_nums = self.dfs(node.right)
        return left_nums + right_nums + 1

    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
```