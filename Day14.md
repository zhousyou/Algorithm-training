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

113 路径总和II：这道题与上面的区分是递归过程中对返回值的处理，这道题是遇到符合条件的值要记录，最后完成所有递归再返回，所以不需要处理返回值。另外，因为需要记录中间结果，所有`self.path[]`记录要做浅拷贝。之前的写法：
```python {.line-numbers}
if not node.left and not node.right and sum == 0:
            self.res.append(self.path)
            return 
```
这样实际上是`path`的引用传递，当后面进行回溯时，`path`的值被改变，`res`中的`path`值也会同步改变，当完成所有回溯时，`path`会变为[].所以在做回溯相关题目时，遇到要记录中间状态的情况，要进行浅拷贝，不能直接引用传递，正确操作是：
```python {.line-numbers}
if not node.left and not node.right and sum == 0:
            self.res.append(self.path[:]) # 引用传递
            return
```
完整代码如下：
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.path = []
        self.res = []

    def dfs(self, node, sum):

        if not node.left and not node.right and sum == 0:
            self.res.append(self.path[:])
            print(self.res)
            return
        if not node.left and not node.right:
            return
        
        # self.path.append(node.val)
        if node.left:
            sum -= node.left.val
            self.path.append(node.left.val)
            self.dfs(node.left, sum)
            sum += node.left.val
            self.path.pop()
        
        if node.right:
            sum -= node.right.val
            self.path.append(node.right.val)
            self.dfs(node.right, sum)
            sum += node.right.val
            self.path.pop()
        return 

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        # self.res.clear()
        # self.path.clear()
        self.path.append(root.val)
        self.dfs(root, targetSum-root.val)
        return self.res
```

***

## [106.从中序与后序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

> 文章讲解https://www.programmercarl.com/0106.%E4%BB%8E%E4%B8%AD%E5%BA%8F%E4%B8%8E%E5%90%8E%E5%BA%8F%E9%81%8D%E5%8E%86%E5%BA%8F%E5%88%97%E6%9E%84%E9%80%A0%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E6%80%9D%E8%80%83%E9%A2%98

### 思路

这道题还是比较容易想到的一定要有一个后序遍历的数组来确定根节点，在中序遍历的数组里找到根节点后再反复确认左子树和右子树即可。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, inorder, postorder):
        if not postorder:
            return None
        # print(inorder, postorder)
        root_val = postorder[-1]

        root = TreeNode(val = root_val)
        i = inorder.index(root_val)

        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder) : len(postorder)-1]

        root.left = self.dfs(left_inorder, left_postorder)
        root.right = self.dfs(right_inorder, right_postorder)
        return root


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(inorder, postorder)
```

105 从前序与中序遍历序列构造二叉树

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, preorder, inorder):
        if not preorder:
            return None
        # print(preorder, inorder)
        root_val = preorder[0]
        root = TreeNode(val = root_val)

        i = inorder.index(root_val)

        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]

        left_preorder = preorder[1: len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1: ]

        root.left = self.dfs(left_preorder, left_inorder)
        root.right = self.dfs(right_preorder, right_inorder)
        return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.dfs(preorder, inorder)
```
