# 代码随想录算法训练营第三天 ｜Leetcode203.移除链表元素、Leetcode707.设计链表、Leetcode206.翻转链表

### [203 移除链表元素](https://leetcode.cn/problems/remove-linked-list-elements/)

>题目链接/文章讲解/视频讲解：：https://programmercarl.com/0203.%E7%A7%BB%E9%99%A4%E9%93%BE%E8%A1%A8%E5%85%83%E7%B4%A0.html



### 思路

链表的思路还是比较清晰的，重点是**虚拟头节点**的使用。另外，我觉得`while`循环条件的判断也是有讲究的，判断条件是` while cur: ` 还是 `while cur.next:`。开始遍历的节点都要从虚拟头节点开始，如果从头节点开始，可能有空节点的`next`指针指向出错的问题。对于循环的判断条件来说，如果是`while cur.next:`，等找到需要删除的节点的值的时候，当前节点正好是被删除节点的上一个，可以直接通过控制`next`指针完成删除。如果是`while cur:`，被删除节点就正好是当前节点，而单链表又不可以倒退，就会出现问题。

### Python代码

```python {.line-numbers}
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummynode = ListNode()
        dummynode.next = head
        cur = dummynode
        while cur.next:
            if cur.next.val == val :
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummynode.next
```

***

### [707 设计链表](https://leetcode.cn/problems/design-linked-list/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0707.%E8%AE%BE%E8%AE%A1%E9%93%BE%E8%A1%A8.html

### 思路

我认为这道题和上面一样，重点都是循环条件的判断，没什么难度。

### Python代码

```python {.line-numbers}
class Listnode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = Listnode()
        self.num = 0

    def get(self, index: int) -> int:
        if index >= self.num or index < 0:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        addnode = Listnode(val = val, next = self.head.next)
        self.head.next = addnode
        self.num += 1


    def addAtTail(self, val: int) -> None:
        addnode = Listnode(val = val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = addnode
        self.num += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # addnode = Listnode(val = val)
        if index > self.num or index < 0:
            return 
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = Listnode(val = val, next = cur.next)
        self.num += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.num or index < 0:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.num -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
```

***

### [206 反转链表](https://leetcode.cn/problems/reverse-linked-list/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0206.%E7%BF%BB%E8%BD%AC%E9%93%BE%E8%A1%A8.html

### 思路

这道题重点是两个指针，一个`pre`指向空，一个`cur`指向头节点，并用一个`tmp`暂存`cur.next`的节点。有一个点要提一下，我在最开始定义`pre`节点的时候是这样定义的，`pre = Listnode()`,这样的话最后的结果链表最后会多一个0，这是因为创建链表节点的时候，默认值就是0，所以要把`pre`定义为`pre=None`。

### Python代码

```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        pre = None
        # 用如下方式定义，最后输出结果会多一个值为零的节点。
        # pre = ListNode() 
        tmp = ListNode()
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
```
