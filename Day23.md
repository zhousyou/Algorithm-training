# 代码随想录算法训练营第二十三天 ｜Leetcode455.分发饼干 、Leetcode376.摆动序列 、Leetcode53.最大子序和

## [455 分发饼干](https://leetcode.cn/problems/assign-cookies/description/)

> 文章讲解：https://programmercarl.com/0455.分发饼干.html
>

### 思路

贪心的题都感觉像脑筋急转弯，这道题就是把两个列表反向遍历，找到其中一个列表的元素大于等于另一个列表中元素的个数，没太理解到贪心的原理。

### Python代码
```python {.line-numbers}
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        index = len(s)-1
        for i in range(len(g)-1, -1, -1):
            if index >=0 and s[index] >= g[i]:
                res += 1
                index -= 1
        return res
```

***

## [376 摆动序列](https://leetcode.cn/problems/wiggle-subsequence/description/)

> 文章讲解：https://programmercarl.com/0376.摆动序列.html

### 思路

没啥思路，看了讲解才做出来。

### Python代码
```python {.line-numbers}
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        prediff, curdiff, res = 0, 0, 1
        for i in range(len(nums)-1):
            curdiff = nums[i+1] - nums[i]
            if (prediff <= 0 and curdiff > 0) or (prediff >= 0 and curdiff < 0):    
                res += 1
                prediff = curdiff
        return res

```

***

## [53 最大子序和](https://leetcode.cn/problems/maximum-subarray/description/)

> 文章讲解：https://programmercarl.com/0053.最大子序和.html

### 思路

有一点点的思路，遍历求和遇到正数就累加，累加和小于零就清零重新计数

### Python代码
```python {.line-numbers}
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        count = 0 
        for i in range(len(nums)):
            count += nums[i]
            if count >= res:
                res = count
            if count < 0 :
                count = 0
        return res
```
