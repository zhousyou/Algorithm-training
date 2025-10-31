# 代码随想录算法训练营第九天 ｜Leetcode232.用栈实现队列 、Leetcode225.用队列实现栈 、Leetcode20.有效的括号、 Leetcode1047.删除字符串中的所有相邻重复项

### [232 用栈实现队列](https://leetcode.cn/problems/implement-queue-using-stacks/description/)

>题目讲解：https://www.programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
>状态：AC

### 思路
主要考察对栈和队列的理解，最开始没有想到如何用两个栈实现队列，看了讲解后了解到要一个栈作为入队的操作，另一栈作为出队的操作，`pop()`时要将入栈的数据放到出栈里，在出栈里抛出数据。

### Python代码

```python {.line-numbers}
class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        print(self.stack_out)
        if self.stack_out:
            return self.stack_out.pop()
        else:
            if self.stack_in:
                for i in range(len(self.stack_in)):
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
            else:
                return None

    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        else:
            # print(self.stack_in)
            return self.stack_in[0]

    def empty(self) -> bool:
        if len(self.stack_in)==0 and len(self.stack_out)==0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

***

### [225.用队列实现栈](https://leetcode.cn/problems/implement-stack-using-queues/description/)

> 题目讲解：https://www.programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html
> 状态：AC

### 思路

最开始的思路和上面一样，用两个队列模拟入栈和出栈，结果发现不行，队列先进先出，入栈复制到出栈里顺序是相同的。发现一个队列其实就可以实现栈的效果，两个队列只需要繁琐一点，每次要`pop()`时，需要将其中一个队列的数据全部复制到另一个队列，抛出数据之后，再将数据复制回来。

### Python代码
```python {.line-numbers}
from collections import deque
class MyStack:

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x: int) -> None:
        self.que1.append(x)

    def pop(self) -> int:
        for i in range(len(self.que1)-1):
            self.que2.append(self.que1.popleft())
        ans = self.que1.popleft()
        for _ in range(len(self.que2)):
            self.que1.append(self.que2.popleft())
        return ans

    def top(self) -> int:
        return self.que1[-1]

    def empty(self) -> bool:
        return len(self.que1)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

***

### [20.有效的括号](https://leetcode.cn/problems/valid-parentheses/description/)

> 题目讲解：https://www.programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html
> 状态：AC

### 思路
栈的应用，当遍历到左括号'(','[','{'时，要将其变为右括号存入栈中，当遇到右括号时，将其与栈顶的元素比较，相同就`pop()`,不同就False.
这道题有三种情况需要判断：
* 栈顶元素与右括号不同时，False
* 有右括号要进行比较时，栈里没有元素，False
* 所有的右括号都比较完成，栈里依然有元素，False

### Python代码
```python {.line-numbers}
class Solution:
    def isValid(self, s: str) -> bool:
        record = []
        for i in s:
            if i=='(':
                record.append(')')
            elif i=='[':
                record.append(']')
            elif i=='{':
                record.append('}')
            elif i==')' or i==']' or i=='}':
                if len(record) == 0 or record[-1]!=i:
                    return False
                else:
                    record.pop()
        return len(record)==0
```

***

### [1047.删除字符串中的所有相邻重复项](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/description/)

> 题目链接：https://www.programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html
> 状态：AC

### 思路

和上一道题一样，遍历一遍，元素入栈，与栈顶元素相同再出栈。

### Python代码
```python {.line-numbers}
class Solution:
    def removeDuplicates(self, s: str) -> str:
        record = []
        for i in s:
            if len(record)!=0 and record[-1] == i:
                record.pop()
            else:
                record.append(i)
        return "".join(record)
```
