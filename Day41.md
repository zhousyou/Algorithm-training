# 代码随想录算法训练营第四十一天 ｜LeetCode739. 每日温度 、LeetCode496.下一个更大元素 I、LeetCode503.下一个更大元素II

## [739. 每日温度](https://leetcode.cn/problems/daily-temperatures/)

> 文章讲解：https://programmercarl.com/0739.%E6%AF%8F%E6%97%A5%E6%B8%A9%E5%BA%A6.html

### 思路

首次接触单调栈的题目，主要寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置。

### Python代码
```python {.line-numbers}
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * (len(temperatures))
        stack = [0]

        for i in range(1, len(temperatures)):
            if temperatures[stack[-1]] >= temperatures[i]:
                stack.append(i)
            else:
                while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
        return ans
```

***

## [496.下一个更大元素 I](https://leetcode.cn/problems/next-greater-element-i/description/)

> 文章讲解：https://programmercarl.com/0496.下一个更大元素I.html#算法公开课

### 思路

和上一道题类似，但是是两个列表进行排序，思路比较绕。

### Python代码

```python {.line-numbers}
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums1)
        stack = [0]
        for i in range(1,len(nums2)):
            # 情况一情况二
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            # 情况三
            else:
                while len(stack)!=0 and nums2[i]>nums2[stack[-1]]:
                    if nums2[stack[-1]] in nums1:
                        index = nums1.index(nums2[stack[-1]])
                        result[index]=nums2[i]
                    stack.pop()                 
                stack.append(i)
        return result
```

***

## [503.下一个更大元素II](https://leetcode.cn/problems/next-greater-element-ii/)

> 文章讲解：https://programmercarl.com/0503.下一个更大元素II.html

### 思路

和第一题一样，对循环列表的处理只需要将列表复制一遍即可。

### Python代码
``` python {.line-numbers}
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dp = [-1] * len(nums)
        stack = []
        for i in range(len(nums)*2):
            while(len(stack) != 0 and nums[i%len(nums)] > nums[stack[-1]]):
                    dp[stack[-1]] = nums[i%len(nums)]
                    stack.pop()
            stack.append(i%len(nums))
        return dp
```