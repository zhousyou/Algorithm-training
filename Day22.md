# 代码随想录算法训练营第二十一天 ｜Leetcode491.递增子序列 、Leetcode46.全排列 、Leetcode47.全排列II、Leetcode332.重新安排行程、Leetcode51.N皇后、Leetcode37.解数独

## [491 递增子序列](https://leetcode.cn/problems/non-decreasing-subsequences/description/)

>https://programmercarl.com/0491.%E9%80%92%E5%A2%9E%E5%AD%90%E5%BA%8F%E5%88%97.html  

>视频讲解：https://www.bilibili.com/video/BV1EG4y1h78v   

### 思路

首次做这道题时确实踩坑了，这道题和子集II不同，原列表是不可以重新排序的，如果和之前一样使用used数组进行管理，就会出现重复的情况，比如`[4,6,7,6]。所以used的状态要通过集合维护，当每一层进行遍历的时候，如果层的元素在集合中出现过，那就跳过。而且集合的也是在for循环层中进行维护的，每一次回溯都会清零。

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, nums, res, start):
        if len(res) >= 2:
            self.ans.append(res[:])
        if start >= len(nums):
            return
        used = set()
        for i in range(start, len(nums)):
            if len(res) > 0 and nums[i] < res[-1]:
                continue
            # if i >= 1 and nums[i] == nums[i-1] and used[i-1] == 0:
            #     continue
            if nums[i] in used:
                continue
            res.append(nums[i])
            used.add(nums[i])
            self.backtracking(nums, res, i+1)
            res.pop()
            # used[nums[i]] = 0
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # used = set()
        self.backtracking(nums, [], 0)
        return self.ans
```

***

## [46 全排列](https://leetcode.cn/problems/permutations/description/)

>本题重点感受一下，排列问题 与 组合问题，组合总和，子集问题的区别。 为什么排列问题不用 startIndex 
https://programmercarl.com/0046.%E5%85%A8%E6%8E%92%E5%88%97.html    
>
>视频讲解：https://www.bilibili.com/video/BV19v4y1S79W    

### 思路

排列问题和组合问题不一样，首先满足的返回条件应该是`len(res) == len(nums)`,当暂存结果中的数据与愿列表长度相同时才会返回。其次是for循环的起始条件不再是start可变的，而是0，这样才会保证将之前的遍历的元素加入结果中。

要注意的是，排列是不能重复的，和子集II一样需要用used列表进行去重。

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, nums, res, used):
        if len(res) == len(nums):
            self.ans.append(res[:])
            return
        for i in range(0, len(nums)):
            if used[i]:
                continue
            res.append(nums[i])
            used[i] = True
            self.backtracking(nums, res, used)
            res.pop()
            used[i] = False
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.backtracking(nums, [],used)
        return self.ans
```

***

## [47 全排列II](https://leetcode.cn/problems/permutations-ii/description/)

>https://programmercarl.com/0047.%E5%85%A8%E6%8E%92%E5%88%97II.html      
>
>视频讲解：https://www.bilibili.com/video/BV1R84y1i7Tm 


### 思路

遇到去重的问题和之前一样的，需要used数组来进行维护

### Python代码
``` python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, nums, res, used):
        if len(res) == len(nums):
            self.ans.append(res[:])
            return
        for i in range(0, len(nums)):
            if used[i] == 1:
                continue
            if i >= 1 and nums[i] == nums[i-1] and used[i-1] ==0:
                continue
            res.append(nums[i])
            used[i] = 1
            self.backtracking(nums, res,used)
            res.pop()
            used[i] =0
            
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [0] * len(nums)
        nums.sort()
        self.backtracking(nums, [], used)
        return self.ans
```
