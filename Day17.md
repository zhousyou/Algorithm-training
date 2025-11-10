# 代码随想录算法训练营第十七天 ｜Leetcode235.二叉搜索树的最近公共祖先 、Leetcode 701.二叉搜索树中的插入操作 、Leetcode 450.删除二叉搜索树中的节点

### [235 二叉搜索树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

> 文章讲解：https://www.programmercarl.com/0235.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E7%9A%84%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88.html
>

### 思路

可以利用二叉搜索树的性质，中间节点一定大于左子树的节点，并小于右子树的节点，当从上至下进行遍历时，第一个遇到的符合区间`[p.val, q.val]`的值就是最近的公共祖先。在递归的返回值上，这道题和之前的不同，是遍历到正确的边在返回，所以对返回值的判断上是：
```python
if (dfs(root.left)) return
if (dfs(root.right)) return
```

### Python代码

迭代法

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if (root.val < p.val and root.val < q.val):
                root = root.right
            elif (root.val > p.val and root.val > q.val):
                root = root.left
        
            else:
                return root
```

递归法

``` python {.line-numbers}



