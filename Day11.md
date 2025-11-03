# 代码随想录算法训练营第十一天 ｜递归遍历、迭代遍历、统一遍历、层序遍历

### 递归遍历

> **文章讲解：** https://www.programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E9%80%92%E5%BD%92%E9%81%8D%E5%8E%86.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
> 
> **题目链接：**
> * 前序遍历：https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
> * 后序遍历：https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
> * 中序遍历：https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

### 思路

主要要掌握递归的写法：
* 确认递归的参数和返回值
* 确认递归的终止条件
* 确认单层递归的逻辑

其次就是前序，中序，后序的定义了。前序是中左右，中序是左中右，后序是左右中。

### Python代码

前序遍历：

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node == None:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
```

后序遍历：

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node == None:
                return 
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res
```

中序遍历：

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node == None:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res
```

***

### 迭代遍历

> **文章讲解：** https://www.programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E8%BF%AD%E4%BB%A3%E9%81%8D%E5%8E%86.html#%E6%80%9D%E8%B7%AF
>
> **题目链接：**
> * 前序遍历：https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
> * 后序遍历：https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
> * 中序遍历：https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

### 思路

三种遍历方式的迭代思想都不一样，前序的思想是在栈中依次放入中间节点，右子节点，左子节点，并依次弹出。后序遍历和前序遍历是一样的，只不过改变了一下放入顺序，变成中左右，最后弹出入栈，再反向输出，就变成了左右中。中序遍历比较复杂，需要一直将左节点入栈，当没有左节点时，将栈中元素pop()，然后将当前节点指向右节点。

### Python代码

前序遍历：

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
```

中序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
```

后序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
```

### 统一遍历

> **文章讲解:**  https://www.programmercarl.com/%E4%BA%8C%E5%8F%89%E6%A0%91%E7%9A%84%E7%BB%9F%E4%B8%80%E8%BF%AD%E4%BB%A3%E6%B3%95.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
>
> **题目链接：**
> * 前序遍历：https://leetcode.cn/problems/binary-tree-preorder-traversal/description/
> * 后序遍历：https://leetcode.cn/problems/binary-tree-postorder-traversal/description/
> * 中序遍历：https://leetcode.cn/problems/binary-tree-inorder-traversal/description/

### 思路

统一分为两种方法：
* 空指针法
* boolean值法

空指针法是在已经处理过，准备出栈的元素后面加入一个空指针，当遍历到空指针的时候，将元素弹出栈。以前序遍历为例，前序是中左右，当节点在入栈的时候，要倒序入栈，已右左中的顺序。

boolean值法是每次节点入栈的时候要存入一个元组，`(node, visited)`,`node`代表当前节点，`visited`标记当前节点是否处理过，如果为`True`则放入结果栈中。

### Python代码

**空指针法：**

前序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                res.append(node.val)
        return res
```

中序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
                
            else:
                node = stack.pop()
                res.append(node.val)
        return res
```

后序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                
                if node.left:
                    stack.append(node.left)
                
            else:
                node = stack.pop()
                res.append(node.val)
        return res
```

**boolean方法：**

前序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)] if root else []
        res = []
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
                continue
            if node.right:
                stack.append((node.right, False))
            
            if node.left:
                stack.append((node.left, False))
            stack.append((node, True))
        return res
```

中序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)] if root else []
        res = []
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
                continue
            if node.right:
                stack.append((node.right, False))
            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
            
        return res
```

后序遍历

```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(root, False)] if root else []
        res = []
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
                continue
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            
            if node.left:
                stack.append((node.left, False))
            
        return res
```

***

