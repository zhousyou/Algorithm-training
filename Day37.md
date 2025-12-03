# 代码随想录算法训练营第三十七天 ｜LeetCode300.最长递增子序列、LeetCode674. 最长连续递增序列、LeetCode718. 最长重复子数组

## [300.最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/submissions/682497071/)

> 视频讲解：https://www.bilibili.com/video/BV1ng411J7xP 
> 
> https://programmercarl.com/0300.%E6%9C%80%E9%95%BF%E4%B8%8A%E5%8D%87%E5%AD%90%E5%BA%8F%E5%88%97.html 

### 思路

重点是理解dp数组的含义
* 确定dp数组的含义：`dp[i]`表示的是[0,i]的**以`nums[i]`**结尾的最大子序列的长度,重点是理解要以nums[i]结尾，因为后面会进行不同结尾的子序列长度的比较
* 确定递推公式：当nums[i] > nums[j]的时候，`dp[i] = max(dp[i], dp[j] + 1)`
* 初始化递推数组：dp数组其实的大小应该为1
额外注意的是，要初始化一个res，来保存每次遍历后得到的最大值，最后输出的结果也不是dp[-1], 而是记录最大值的res，因为以nums[-1]结尾的子序列不一定是最大的递增子序列。

### Python代码
```python {.line-numbers}
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        res = 1
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        print(dp)
        return res
```

***

## [LeetCode674. 最长连续递增序列](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/submissions/682498611/)

> 视频讲解：https://www.bilibili.com/video/BV1bD4y1778v 
> 
> https://programmercarl.com/0674.%E6%9C%80%E9%95%BF%E8%BF%9E%E7%BB%AD%E9%80%92%E5%A2%9E%E5%BA%8F%E5%88%97.html

### 思路

与之前的题的区别在于这个是求**最长连续递增的序列**，就不需要两层遍历，只需要判断当`nums[i]>nums[i-1]`的时候，此时`dp[i] = dp[i-1] + 1`

### Python代码
```python {.line-numbers}
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        res = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
            res = max(res, dp[i])
        return res
```

***

## [718. 最长重复子数组](https://leetcode.cn/problems/maximum-length-of-repeated-subarray/submissions/682503633/)

> 视频讲解：https://www.bilibili.com/video/BV178411H7hV
> 
> https://programmercarl.com/0718.%E6%9C%80%E9%95%BF%E9%87%8D%E5%A4%8D%E5%AD%90%E6%95%B0%E7%BB%84.html 

### 思路

这道题需要用二维dp数组进行判断，dp数组的含义为dp[i][j]:nums1中[0,i]与nums2中[0,j]的最长公共子序列长度。判断递推公式：只有当nums1[i] == nums2[j]时，dp[i][j]的结果才会增加，而且一定是在dp[i-1][j-1]的基础上。

### Python代码
```python {.line-numbers}
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0] * (n2+1) for _ in range(n1+1)]

        res = 0
        
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                res = max(dp[i][j], res)
        # print(dp)
        return res
```

