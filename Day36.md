# 代码随想录算法训练营第三十六天 ｜LeetCode188.买卖股票的最佳时机IV、LeetCode309.最佳买卖股票时机含冷冻期、LeetCode714.买卖股票的最佳时机含手续费

## [188.买卖股票的最佳时机IV](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/)

> 视频讲解：https://www.bilibili.com/video/BV16M411U7XJ 
https://programmercarl.com/0188.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIV.html 

### 思路

和上一道题一致，只不过从最多买两次变成最多k次

### Python代码
```python {.line-numbers}
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(2*k+1) for _ in range(n)]

        for j in range(2*k+1):
            if j % 2 != 0:
                dp[0][j] = -prices[0]
        
        for i in range(1, n):
            for j in range(1, 2*k, 2):
                dp[i][j] = max(dp[i-1][j-1] - prices[i], dp[i-1][j])
                dp[i][j+1] = max(dp[i-1][j] + prices[i], dp[i-1][j+1])
        print(dp)
        return dp[-1][-1]
```

***

## [309.最佳买卖股票时机含冷冻期](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/)

> 视频讲解：https://www.bilibili.com/video/BV1rP4y1D7ku 
> 
> https://programmercarl.com/0309.%E6%9C%80%E4%BD%B3%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E6%97%B6%E6%9C%BA%E5%90%AB%E5%86%B7%E5%86%BB%E6%9C%9F.html  

### 思路
这道题需要额外判断冷冻期的状态

### Python代码
```python {.line-numbers}
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 4 for _ in range(n)]

        dp[0][0] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], max(dp[i-1][3] - prices[i], dp[i-1][1] - prices[i]))
            dp[i][1] = max(dp[i-1][1], dp[i-1][3])
            dp[i][2] = dp[i-1][0] + prices[i]
            dp[i][3] = dp[i-1][2]
        return max(dp[n-1][3], dp[n-1][2], dp[n-1][1])
```
