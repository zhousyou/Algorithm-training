# 代码随想录算法训练营第三十八天 ｜LeetCode1143.最长公共子序列和、LeetCode1035.不相交的线、LeetCode53.最大子数组和、LeetCode392.判断子序列

## [1143.最长公共子序列和](https://leetcode.cn/problems/longest-common-subsequence/submissions/682551487/)

> 文章讲解：https://www.programmercarl.com/1143.%E6%9C%80%E9%95%BF%E5%85%AC%E5%85%B1%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

* 确定dp数组的含义：`dp[i][j]:[0,i-1]`的text1,[0,j-1]的text2的最大公共子序列的长度
* 确定递推公式：`if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1`, 不相等的情况，就要取上一个状态最长的子序列`max(dp[i][j-1],dp[i-1][j])`
* 初始化dp数组：当i=0或j=0时，与空子集的子序列长度为0

### Python代码
```python {.line-numbers}
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0] * (n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        print(dp)
        return dp[-1][-1]
```

***

## [1035.不相交的线](https://leetcode.cn/problems/uncrossed-lines/submissions/682551863/)

> 文章讲解：https://www.programmercarl.com/1035.%E4%B8%8D%E7%9B%B8%E4%BA%A4%E7%9A%84%E7%BA%BF.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

与上一道题一模一样

### Python代码
```python {.line-numbers}
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        dp = [[0]*(n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[-1][-1]
```

***

## [53.最大子数组和](https://leetcode.cn/problems/maximum-subarray/)

> 文章讲解：https://www.programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html

### 思路

* 确定dp数组含义：dp[i]表示[0,i]的最大子数组的和
* 确定递推公式: 首先是`dp[i] = dp[i-1] + nums[i]`，因为是连续子数组所以当nums[i] > dp[i]时，要归零，dp[i] = nums[i]。`dp[i] = max(nums[i], dp[i-1] + nums[i])`

### Python 代码
```python {.line-numbers}
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+1)
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            res = max(res, dp[i])
        print(dp)
        return res
```

***

## [392.判断子序列](https://leetcode.cn/problems/is-subsequence/)

> 文章讲解：https://www.programmercarl.com/0392.%E5%88%A4%E6%96%AD%E5%AD%90%E5%BA%8F%E5%88%97.html

### 思路

* dp数组的含义：`dp[i][j]`表示[0,i-1]的s序列和[0,j-1]的t序列的最大公共子序列的长度
* 确定递推公式：当s[i-1] == t[j-1]时，dp[i][j] = dp[i-1][j-1] + 1.当不相等时，t序列就应该删除当前当前j-1的元素，所以dp[i][j] = dp[i][j-1]

### Python代码

```python {.line-numbers}
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n_s, n_t = len(s), len(t)
        dp = [[0] * (n_t+1) for _ in range(n_s+1)]

        for i in range(1, n_s+1):
            for j in range(1, n_t+1):
                if s[i-1] == t[j-1] :
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        print(dp)
        if dp[-1][-1] == n_s:
            
            return True
        else:
            return False
```
