# 代码随想录算法训练营第十二天 ｜Leetcode226.翻转二叉树、Leetcode101.对称二叉树、Leetcode104.二叉树的最大深度、Leetcode111.二叉树的最小深度

## [226 翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/description/)

> 文章讲解：https://www.programmercarl.com/0226.%E7%BF%BB%E8%BD%AC%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
>
> 状态：AC

### 思路

翻转二叉树主要还是要通过遍历来实现，前序后序遍历的方式都可以，中序遍历由于是左中右的顺序，在中间节点的时候要进行翻转的操作，如果此时在指向有节点，那就会出现同时指向同一个节点的情况。所以此时，中序遍历要做调整，左中右的处理顺序要变成左中左或者右中右的顺序，具体见代码说明。

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

中序遍历递归的方法：**不可行，中间节点会被翻转两次，需要特殊处理**
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
            node.left, node.right = node.right, node.left  # 处理中间节点
            # 中序遍历是左中右的顺序，先递归左边的节点，在处理中间的节点（左右子节点交换），最后在递归右边的节点，但这时左右子节点已完成互换，右子节点此刻指向的是左子节点。

            # 如果此刻按照左 中 右的顺序来处理，左右实际上指向的是同一个节点。
            # dfs(node.right)  # 右 
            dfs(node.left) # 要按照左中左或者右中右的顺序。
            return node
        return dfs(root)
```

***

## [101 对称二叉树](https://leetcode.cn/problems/symmetric-tree/description/)

> 文章讲解：https://programmercarl.com/0101.对称二叉树.html#其他语言版本
> 状态：AC


### 思路

要判断一个二叉树是否对称，要将二叉树拆分为左子树和右子树分别判断。并且要明确判断条件：
* `if not node.left or not node.right`：左节点或右节点为空，`return False`.
* `if node.left.val != node.right.val`: 左右节点的值不相等，`return False`
* `if not node.left and not node.right`: 左右节点都为空， `return True`
* 其余情况为左右节点都存在，且值相同。

可以用队列或着栈，迭代法，将两个节点分别放入队列（栈）中，再拿出来一一比较。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que = collections.deque()
        que.append(root.left)
        que.append(root.right)
        while que:
            node_left = que.popleft()
            node_right = que.popleft()
            if not node_left and not node_right:
                continue
            if not node_left or not node_right:
                return False
            if node_left.val != node_right.val:
                return False
            que.append(node_left.left)
            que.append(node_right.right)
            que.append(node_left.right)
            que.append(node_right.left)
        return True
```

栈迭代：
``` python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            node_right = stack.pop()
            node_left = stack.pop()
            if not node_left and not node_right:
                continue
            if not node_left or not node_right:
                return False
            if node_left.val != node_right.val:
                return False
            stack.append(node_right.right)
            stack.append(node_left.left)
            stack.append(node_right.left)
            stack.append(node_left.right)
        return True
```

***

## [104 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)

> 文章讲解：https://programmercarl.com/0104.二叉树的最大深度.html#其他语言版本
> 状态：AC


### 思路

n叉树的思路和二叉树是一样的，有疑问的点是如何初始化`max_depth`的值，以及单层递归的时候的判断。

### Python代码

二叉树：
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max_depth = 0
        def dfs(node):
            if not node :
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            max_depth = 1+max(left_depth, right_depth)
            return max_depth
        return dfs(root)
```

n叉树：
```python {.line-numbers}
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        max_depth = 1
        for i in node.children:
            max_depth = max(self.dfs(i)+1, max_depth)
        return max_depth
    def maxDepth(self, root: 'Node') -> int:
        return self.dfs(root)
```

## [111 二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/description/)

>文章讲解：https://programmercarl.com/0111.二叉树的最小深度.html#算法公开课

### 思路

讲解说的对，和最大深度不一样，如果按照最大深度的解法来会出现误区，最小深度指的是到叶子节点。所以要判断：
* 如果左子树为空，右子树不为空，最小深度为右子树 + 1
* 如果左子树不为空，右子树为空，最小深度为左子树 + 1
* 如果左右子树都不为空， 最小深度为两者最小

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
        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)
        if not node.left and node.right:
            min_depth = right_depth + 1
        elif not node.right and node.left:
            min_depth = left_depth + 1
        else:
            min_depth = min(left_depth, right_depth) + 1
        return min_depth

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
```

