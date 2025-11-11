# 代码随想录算法训练营第十八天 ｜Leetcode669.修剪二叉搜索树 、Leetcode108.将有序数组转换为二叉搜索树 、Leetcode538.把二叉搜索树转换为累加树

## [669 修剪二叉搜索树](https://leetcode.cn/problems/trim-a-binary-search-tree/)

> 文章讲解：https://www.programmercarl.com/0669.%E4%BF%AE%E5%89%AA%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html
>

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
```

## [108 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)

> 文章讲解：https://programmercarl.com/0108.将有序数组转换为二叉搜索树.html#算法公开课
>

### 思路

这道题还是比较简单的，有序数组可以看作二叉搜索树的中序遍历的结果，根节点可以每次去数组中中间的值，这样就可以用一个中序数组去构建二叉搜索树，思路和之前的通过中序和后序遍历构建树的操作是一样的。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        n = len(nums)
        i = n//2
        root = TreeNode(nums[i])

        left_nums = nums[:i]
        right_nums = nums[i+1:]

        root.left = self.sortedArrayToBST(left_nums)
        root.right = self.sortedArrayToBST(right_nums)
        return root

```

## [538 把二叉搜索树转换为累加树](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

> 文章讲解：https://programmercarl.com/0538.把二叉搜索树转换为累加树.html
>
>

### 思路

解题思路是找到累加的顺序，是从最大的值开始的，也就是整个树的最右边的叶子节点，所以要从最右侧开始遍历，要用反向中序遍历的方式，右中左。另一个重点是，要维护一个值，来记录累加的和，例如当一个节点存在右子树的时候，他的根节点的值不能是右节点 + 根节点，而是根节点 + 右子树的最左侧的节点，所以此时要通过一个值来维护此时累加的和。

### python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def dfs(self, node):
        if not node:
            return None
        right = self.dfs(node.right)
        node.val += self.sum
        self.sum = node.val
        left = self.dfs(node.left)
        return node

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        return self.dfs(root)
```