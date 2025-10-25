# 代码随想录算法训练营第四天 ｜Leetcode24. 两两交换链表中的节点 、Leetcode19.删除链表的倒数第N个节点、面试题 02.07. 链表相交、Leetcode142.环形链表II 

### [Leetcode24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/description/)

>题目链接/文章讲解/视频讲解： https://programmercarl.com/0024.%E4%B8%A4%E4%B8%A4%E4%BA%A4%E6%8D%A2%E9%93%BE%E8%A1%A8%E4%B8%AD%E7%9A%84%E8%8A%82%E7%82%B9.html
状态： AC

### 思路

这道题画图出来思路会清晰很多，首次做容易出错的点有两个，一个是虚拟头节点的使用，一个是用一个`tmp`节点暂存要交换的节点。前者在做的时候，使用的是`cur=head`,在最后返回的时候，`cur`并没有指向头节点会出问题。后者是我发现用`tmp`复制其中一个节点的时候，`tmp`是对引用的拷贝，`cur`和`tmp`是对同一个对象的引用，修改其中一个都会对对象本身产生修改。

### Python代码

```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(next = head)
        cur = dummyhead
        while cur.next and cur.next.next:
            tmp = cur.next
            tmp1 = cur.next.next.next
            cur.next = cur.next.next
            cur.next.next = tmp
            tmp.next = tmp1
            cur = cur.next.next
        return dummyhead.next
```

### [Leetcode19.删除链表的倒数第N个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

> 题目链接/文章讲解/视频讲解：https://programmercarl.com/0019.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E5%80%92%E6%95%B0%E7%AC%ACN%E4%B8%AA%E8%8A%82%E7%82%B9.html
> 状态： AC

### 思路
初见没有很好的思路，只有想到遍历两次，第一次找到链表长度，第二次找到被删除的元素。看完讲解之后，发现可以用快慢指针的方式，快指针比慢指针快走`n`步，还是很巧妙的。

### Python代码

```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyhead = ListNode(next = head)
        fast = slow = dummyhead
        while n:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummyhead.next
```

### [面试题 02.07. 链表相交](https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/description/)

>题目链接/文章讲解：https://programmercarl.com/%E9%9D%A2%E8%AF%95%E9%A2%9802.07.%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4.html
>状态：AC

### 思路

这题也很简单，一遍直接AC。求出两个链表的长度，末尾对齐就可以了。

### Python代码

```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curA = dummyA = ListNode(next = headA)
        curB = dummyB = ListNode(next = headB)
        numA = numB = 0
        while curA:
            curA = curA.next
            numA += 1
        while curB:
            curB = curB.next
            numB += 1
        curA = dummyA
        curB = dummyB
        if numA > numB:
            n = numA - numB
            while n:
                curA = curA.next
                n -= 1
        else:
            n = numB -numA
            while n:
                curB = curB.next
                n -= 1
        while curB:
            curA = curA.next
            curB = curB.next
            if curA == curB:
                return curA
            
        return null
```

### [Leetcode142.环形链表II](https://leetcode.cn/problems/linked-list-cycle-ii/description/) 

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html

### 思路

快慢指针的方法很巧妙，做法不是很容易想出来。集合的方法确实很方便，也很容易，后面遇到类似的题目，找重复的值，可以优先考虑集合。

### Python代码

快慢指针

```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
```

集合的方法

```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = set()
        while head:
            if head in ans:
                return head
            ans.add(head)
            head = head.next
        return None
```


