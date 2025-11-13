# 代码随想录算法训练营第二十天 ｜Leetcode38.组合总和 、Leetcode40.组合总和II 、Leetcode131.分割回文串

## [38 组合总和](https://leetcode.cn/problems/combination-sum/description/)

> 题目链接/文章讲解：https://programmercarl.com/0039.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C.html  
>
> 视频讲解：https://www.bilibili.com/video/BV1KT4y1M7HJ   
>
> 状态：AC

### 思路

这道题重点是在`for`循环中`startindex`的判断，因为允许有重复的元素，所以每次循环可以遍历的元素应该从本身元素开始。

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, candidates, target, res, sum,start):
        if sum > target:
            return 
        if sum == target:
            self.ans.append(res[:])

        for i in range(start, len(candidates)):
            res.append(candidates[i])
            sum += candidates[i]
            self.backtracking(candidates, target, res, sum, i)
            res.pop()
            sum -= candidates[i]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.backtracking(candidates, target, [], 0,0)
        return self.ans

```

***

## [40 组合总和II](https://leetcode.cn/problems/combination-sum-ii/description/)

> 题目链接/文章讲解：https://programmercarl.com/0040.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CII.html    
>
> 视频讲解：https://www.bilibili.com/video/BV12V4y1V73A 

### 思路

这道题和上一道题不同，需要去重，在第一遍做的时候，我有想到如果去重需要对数组进行排序，找到满足`if i>0 and candidates[i] == candidates[i-1]`的条件的值，然后跳过。但是依然得不到正确的答案，去重依然有问题。看了讲解后，才明白需要再规划一个列表来存储列表中元素的使用状态，在上面条件满足的基础上，仍需满足`used[i-1] == 0`.

### Python代码
``` python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, candidates, target, res, sum, start, used):
        if sum > target:
            return 
        if sum == target:
            self.ans.append(res[:])
            return
        for i in range(start, len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1] and used[i-1] == 0:
                continue
            res.append(candidates[i])
            sum += candidates[i]
            used[i] = 1
            self.backtracking(candidates, target, res, sum, i + 1, used)
            res.pop()
            sum -= candidates[i]
            used[i] = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        used = [0] * len(candidates)
        candidates.sort()
        # print(candidates)
        self.backtracking(candidates, target, [], 0, 0, used)
        return self.ans
```

***

## [131 分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/)

>https://programmercarl.com/0131.%E5%88%86%E5%89%B2%E5%9B%9E%E6%96%87%E4%B8%B2.html   

>视频讲解：https://www.bilibili.com/video/BV1c54y1e7k6  

### 思路

这道题难点在于分割的思想，分割其实也就是列表下标的遍历，而且分割讲究顺序，不能重复切割。

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def isPartition(self, s, start, end):
        while start <= end:
            if s[start] != s[end] :
                return False
            start += 1
            end -= 1
        return True
    def backtracking(self, s, start, res):
        if start == len(s):
            self.ans.append(res[:])
            return 
        for i in range(start, len(s)):
            if self.isPartition(s, start, i):
                # print(s[i:index])
                res.append(s[start: i+1])
                # print(res)
                self.backtracking(s, i + 1, res)
                res.pop()
            
    def partition(self, s: str) -> List[List[str]]:
        self.backtracking(s, 0, [])
        return self.ans
```

