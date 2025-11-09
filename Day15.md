# 代码随想录算法训练营第十五天 ｜Leetcode654.最大二叉树、Leetcode617.合并二叉树、Leetcode700.二叉搜索树中的搜索、Leetcode98.验证二叉搜索树

## [654 最大二叉树](https://leetcode.cn/problems/maximum-binary-tree/description/)

> 文章讲解：题目链接/文章讲解：https://programmercarl.com/0654.%E6%9C%80%E5%A4%A7%E4%BA%8C%E5%8F%89%E6%A0%91.html 
> 
> 视频讲解：https://www.bilibili.com/video/BV1MG411G7ox   

### 思路

这道题和之前通过中序遍历与后序遍历构造二叉树是类似的，通过前序遍历的方式，每次优先找到数组中最大的值作为根节点，再划分数组，通过递归的方式找到左节点与右节点，比较简单。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, nums):
        if not nums:
            return
        root = TreeNode(max(nums))
        i = nums.index(root.val)
        left_tree = nums[:i]
        right_tree = nums[i+1:]
        root.left = self.dfs(left_tree)
        root.right = self.dfs(right_tree)
        return root
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.dfs(nums)
```

***

## [617 合并二叉树](https://leetcode.cn/problems/merge-two-binary-trees/description/)

> 题目链接/文章讲解：https://programmercarl.com/0617.%E5%90%88%E5%B9%B6%E4%BA%8C%E5%8F%89%E6%A0%91.html 
>
> 视频讲解：https://www.bilibili.com/video/BV1m14y1Y7JK   

### 思路

这道题也不是很难，用递归方法的话，难点是如何处理节点为空的情况。最开始我想的方法是分别判断递归中传入的两个节点：
* node1为空，node2不为空
* node2为空，node1不为空
* node1，node2均为空
并分不同情况处理不同的递归，这样会有些麻烦。看了讲解发现，可以直接判断节点情况：
* `if not node1: root = node2`
* `if not node2: root = node1`
而此时，如果node1和node2都为空，返回值也为空
### Python代码

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return
        if not node1:
            root = TreeNode(node2.val)
            root.left = self.dfs(None, node2.left)
            root.right = self.dfs(None, node2.right)
        elif not node2:
            root = TreeNode(node1.val)
            root.left = self.dfs(None, node1.left)
            root.right = self.dfs(None, node1.right)
        else:
            root = TreeNode(node1.val + node2.val)
            root.left = self.dfs(node1.left , node2.left)
            root.right = self.dfs(node1.right , node2.right)
        return root
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root1, root2)
```
迭代法：
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        que = collections.deque()
        que.append(root1)
        que.append(root2)
        while que:
            node1 = que.popleft()
            node2 = que.popleft()
            if node1.left and node2.left:
                que.append(node1.left)
                que.append(node2.left)
            if node1.right and node2.right:
                que.append(node1.right)
                que.append(node2.right)
            node1.val += node2.val

            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
        return root1
```

***

## [700 二叉搜索树中的搜索](https://leetcode.cn/problems/search-in-a-binary-search-tree/description/)

> 题目链接/文章讲解: https://programmercarl.com/0700.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%90%9C%E7%B4%A2.html   
>
>视频讲解：https://www.bilibili.com/video/BV1wG411g7sF    

### 思路

用递归的方法还是比较简单的,迭代的方法也是一样，通过一个队列来维护就可以。

### python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, val):
        if not node:
            return 
        if node.val == val:
            return node
        if val < node.val:
            res = self.dfs(node.left, val)
        if val > node.val:
            res = self.dfs(node.right, val)
        return res
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)
```
迭代的方法
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root :
            return None
        que = collections.deque()
        que.append(root)
        while que:
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            if node.val == val:
                return node
        return None
```

***

## [98 验证二叉搜素树](https://leetcode.cn/problems/validate-binary-search-tree/description/)

>题目链接/文章讲解：https://programmercarl.com/0098.%E9%AA%8C%E8%AF%81%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html  
>
>视频讲解：https://www.bilibili.com/video/BV18P411n7Q4   

### 思路

这道题可以用中序遍历的思想，将节点通过中序遍历放到一个列表中，如果二叉树是一个二叉搜索树，那么列表应该是严格递增的。

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return 
        self.dfs(root)
        print(self.stack)
        for i in range(len(self.stack)-1):
            if self.stack[i] >= self.stack[i+1]:
                return False
        return True
```