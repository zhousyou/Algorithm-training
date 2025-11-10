from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

def dfs(node, p, q):
    if node is None:
        return node
    print(node.val)
    if node.val > p.val and node.val > q.val:
        left = dfs(node.left, p, q)
        print(left.val)
        # if left is not None:
        if left:
            return left
    if node.val < p.val and node.val < q.val:
        right = dfs(node.right, p, q)
        # print(right.val)
        # if right is not None:
        if not right:
            return right
    return node

def solution(root, p, q):
    return dfs(root, p, q)

def createTree(nums):
    que = deque()
    root = TreeNode(nums[0])
    que.append(root)
    i = 1
    while que:
        node = que.popleft()
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            que.append(node.left)
        i += 1

        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            que.append(node.right)
        i += 1
    return root

def show_tree(node):
    res = []
    que = deque()
    que.append(node)
    while que:
        for _ in range(len(que)):
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            res.append(node.val)
    return res

if __name__ == "__main__":

    nums = [6,2,8,0,4,7,9,None,None,3,5]
    root = createTree(nums)
    res = show_tree(root)
    print(res)
    p = TreeNode(val=2)
    q = TreeNode(val=4)
    node = solution(root,p,q)
    print(node.val)

