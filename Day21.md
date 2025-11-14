# 代码随想录算法训练营第二十一天 ｜Leetcode93.复原IP地址 、Leetcode78.子集 、Leetcode90.子集II

## [93 复原IP地址](https://leetcode.cn/problems/restore-ip-addresses/description/)

> 文章讲解：https://www.programmercarl.com/0093.%E5%A4%8D%E5%8E%9FIP%E5%9C%B0%E5%9D%80.html
>
> 状态：AC

### 思路

这道题和分割回文串类似，也是分割问题，没啥特殊的。

### Python代码

```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def isvalidIP(self, s, start, end):
        if end - start > 1 and s[start] == "0":
            return False
        ipnum = int(s[start: end])
        if ipnum >=0 and ipnum <= 255:
            return True
        return False
    def backtracking(self, s, start, res):
        if len(res) == 4 and start >= len(s):
            tmp = ".".join(res)
            self.ans.append(tmp)
            return
        for i in range(start, len(s)):
            tmp = s[start: i + 1]
            if self.isvalidIP(s, start, i + 1):
                print(s[start: i+1])
                res.append(s[start:i+1])
                self.backtracking(s, i+1, res)
                res.pop()
            
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtracking(s, 0, [])
        return self.ans
```

***

## [78 子集](https://leetcode.cn/problems/subsets/description/)

> 文章讲解：https://www.programmercarl.com/0078.%E5%AD%90%E9%9B%86.html、
>
> 状态：AC

### 思路

子集问题不同于组合和分割，没有一个明确的终止条件，比如组合总和的问题，终止条件是列表里的总和满足`target`, 找子集的情况是找到列表的末尾，再返回。而且不同于组合，当满足于终止条件时才可以将`res`暂存的结果放入到`ans`中。子集需要将本身每次遍历的结果存下来，包括空集的情况`[]`.所以与组合问题不同，在终止条件上的写法如下：
* 组合问题：
``` python {.line-numbers}
if (终止条件):
  self.ans.append(res[:])
  return
```

* 子集问题：
```python {.line-numbers}
self.ans.append(res[:])
if (终止条件):
  return
```

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, nums, res, start):
        self.ans.append(res[:])
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            res.append(nums[i])
            self.backtracking(nums, res, i+1)
            res.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, [], 0)
        # self.ans.append([])
        return self.ans
```

***

## [90 子集II](https://leetcode.cn/problems/subsets-ii/description/)

> 文章讲解：https://www.programmercarl.com/0090.%E5%AD%90%E9%9B%86II.html
>
> 状态：AC

### 思路

去重的问题和组合总和II思路是一样的，首先回溯的数组一定要排序，第二点就是used数组的运用，去重的条件判断`if i >=0 and num[i] == num[i-1] and used[i-1] == 0: continue`.

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, nums, res, start, used):
        self.ans.append(res[:])
        if start >= len(nums):
            return
        for i in range(start, len(nums)):
            if i >= 1 and nums[i] == nums[i-1] and used[i-1] == 0:
                continue
            res.append(nums[i])
            used[i] = 1
            self.backtracking(nums, res, i+1, used)
            res.pop()
            used[i] = 0
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        used = [0] * len(nums)
        nums.sort()
        self.backtracking(nums, [], 0, used)
        return self.ans
```
