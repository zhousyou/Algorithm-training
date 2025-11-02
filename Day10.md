# 代码随想录算法训练营第十天 ｜Leetcode150. 逆波兰表达式求值  、Leetcode239. 滑动窗口最大值 、Leetcode 347.前 K 个高频元素

### [150 逆波兰表达式求值](https://leetcode.cn/problems/evaluate-reverse-polish-notation/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html   
>状态：AC

### 思路
栈的基本应用，没什么难度，第一遍实现的时候运算符的实现是分情况列举的，看了讲解之后才了解到，也可以直接使用python中内置的函数方法，`from operator import add, mul, sub`,这样实现起来会更简单。

### Python代码
```python {.line-numbers}
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        record = []
        operand = ['+','-','*','/']
        for i in tokens:
            if i in operand:
                if i == '+':
                    tmp1 = record.pop()
                    tmp2 = record.pop()
                    tmp_res = tmp1 + tmp2
                    record.append(tmp_res)
                elif i == '-':
                    tmp1 = record.pop()
                    tmp2 = record.pop()
                    tmp_res = tmp2 -tmp1
                    record.append(tmp_res)
                elif i=='*':
                    tmp1 = record.pop()
                    tmp2 = record.pop()
                    tmp_res = tmp2 * tmp1
                    record.append(tmp_res)
                elif i=='/':
                    tmp1 = record.pop()
                    tmp2 = record.pop()
                    tmp_res = int(tmp2 / tmp1)
                    record.append(tmp_res)
            else:        
                record.append(int(i))
        return record[0]
```

用内置函数的方法

```python {.line-numbers}
from operator import add, sub, mul
def div(num1, num2):
        return int(num1/num2) if num1*num2 > 0 else -(abs(num1) // abs(num2))
class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        record = []
        opera = {'+': add, '-':sub, '*':mul, '/':div}
        for i in tokens:
            if i in opera.keys():
                tmp1 = record.pop()
                tmp2 = record.pop()
                record.append(opera[i](tmp2, tmp1))
            else:
                record.append(int(i))
        return record.pop()
```

***

### [239 滑动窗口最大值](https://leetcode.cn/problems/sliding-window-maximum/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html  
>状态：没做出来

### 思路

一开始用的是滑动窗口暴力的解法，每次滑动的时候，判断新增元素与之前记录最大元素的大小，在进行入栈的操作，但这种方法最后超时了，不可取。看了讲解后，用单调队列的方法，感觉很巧妙，保证队列为单调递减的顺序，入队操作为当前入队元素如果大于队尾元素，就一直pop，直到满足条件。

### Python代码
```python {.line-numbers}
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        record = deque()
        ans = []

        for i in range(len(nums)):
            self.update_nums(record, nums[i])
            if i >=k and nums[i-k]== record[0]:
                record.popleft()
            if i >=k-1:
                ans.append(record[0])
        return ans

    def update_nums(self, kept_nums, nums) :
        while kept_nums and nums > kept_nums[-1]:
            kept_nums.pop()
        kept_nums.append(nums)
```

***

### [347.前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html  
>状态：没做出来

### 思路
用小顶堆的思路，将`(freq, key)`传入小顶堆当中，按照`freq`的大小进行排序。保留前k个元素，多余的元素从堆顶弹出。

### Python代码
```python {.line-numbers}

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {} #nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1
        
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que = [] #小顶堆
        
        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k: #如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)
        
        #找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
```
