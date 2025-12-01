# 代码随想录算法训练营第三十五天 ｜LeetCode121. 买卖股票的最佳时机、LeetCode122.买卖股票的最佳时机II、LeetCode123.买卖股票的最佳时机III

## [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

> 视频讲解：https://www.bilibili.com/video/BV1Xe4y1u77q 

### 思路

难点在于dp数组的理解，也是看了讲解才明白dp数组的含义，以及递推公式
* dp数组：dp[i][0]:表示第i天持有股票，最大的现金额度，因为默认初始现金为0， 所以dp[i][0]基本为负数。dp[i][1]:表示第i天不持有股票，最大的现金额度。
* 确定递推公式：dp[i][0] = max(dp[i-1][0], -prices[i]),因为只可以买卖股票一次，如果第i天确定买股票则为-prices[i].dp[i][1] = max(dp[i-1][1], dp[i][0]+prices[i])

### Python代码
```python {.line-numbers}
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]

        if  n <= 1:
            return 0

        dp[0][0] = -prices[0]
        dp[1][1] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i][0] + prices[i])
        print(dp)
        return dp[n-1][1]
```

***

## [122.买卖股票的最佳时机II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/submissions/682004694/)

> 视频讲解：https://www.bilibili.com/video/BV1D24y1Q7Ls 
> 
> https://programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII%EF%BC%88%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%EF%BC%89.html

### 思路

这道题和上一题不同在于可以多次买卖股票，在递推公式上有差别
* dp数组含义：和上面一样
* 递推公式：dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i]),因为可以重复购买，所以第i天持有股票的情况可以是**第i-1天没有持有股票的现金 - 第i天的股票价格**

### Python代码
```python {.line-numbers}
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        if n <= 1:
            return 0
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i][0] + prices[i])
        
        return dp[n-1][1]
```