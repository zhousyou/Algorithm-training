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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node, p, q):
        if node is None:
            return node
        if node.val > p.val and node.val > q.val:
            left = self.dfs(node.left, p, q)
            if left:
                return left
        if node.val < p.val and node.val < q.val:
            right = self.dfs(node.right, p, q)
            if right:
                return right
        return node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)
```

## [701 二叉搜索树中的插入操作](https://leetcode.cn/problems/insert-into-a-binary-search-tree/description/)

> 题目链接/文章讲解：https://programmercarl.com/0701.%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E6%8F%92%E5%85%A5%E6%93%8D%E4%BD%9C.html   
>
> 视频讲解：https://www.bilibili.com/video/BV1Et4y1c78Y   

### 思路

这道题用递归的方式，重点是判断停止的条件：
* 当前节点没有左节点，并且`val`小于节点的值：插入左子节点
* 当前节点没有右节点，并且`val`大于节点的值：插入右子节点
* 当前节点为空，直接插入并返回

### Python代码
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
            node = TreeNode(val)
            return node 

        if not node.left and node.val > val:
            node.left = TreeNode(val)
            return node
        if not node.right and node.val < val:
            node.right = TreeNode(val)
            return node
                
        if node.val > val:
            self.dfs(node.left, val)
        if node.val < val:
            self.dfs(node.right, val)
        return node 
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)
        
```

***

## [450 删除二叉搜索树中的节点](https://leetcode.cn/problems/delete-node-in-a-bst/description/)

>题目链接/文章讲解：https://programmercarl.com/0450.%E5%88%A0%E9%99%A4%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html  
>
>视频讲解：https://www.bilibili.com/video/BV1tP41177us   

### 思路

相比于增加节点，删除节点需要判断的情况更多，而且需要改变树的结构：
* 当前树没有删除的节点，返回空
* 当前树有需要删除的节点：
  * 删除的节点没有左右子树，删除节点返回空
  * 删除的节点有左子树，没有右子树，删除节点，返回左子树的根节点
  * 删除的节点有右子树，没有左子树，删除节点，返回右子树的根节点
  * 删除的节点左右子树都存在，找到右子树的最左侧的叶子节点，把左子树的根节点放到右子树最左侧的叶子节点。
  
### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, key):
        if not node:
            return node
        if node.val == key:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                cur = node.right
                while cur.left:
                    cur = cur.left
                cur.left = node.left
                return node.right
        if node.val > key:
            node.left = self.dfs(node.left, key)
        if node.val < key:
            node.right = self.dfs(node.right, key)
        return node
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.dfs(root, key)
```