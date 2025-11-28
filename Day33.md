# 代码随想录算法训练营第三十三天 ｜LeetCode322.零钱兑换、LeetCode279.完全平方数、LeetCode139.单词拆分

## [322.零钱兑换](https://leetcode.cn/problems/coin-change/)

> 文章讲解：https://www.programmercarl.com/0322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.html#%E6%80%BB%E7%BB%93

### 思路

这道题是找到满足条件的最小的个数，是组合数。
* 确定dp数组的含义：dp[i][j]表示，取[0,i]物品，满足背包容积j时的**最小组合数。**
* 确定递推公式：
  * 不取第i个物品，此时`dp[i][j] = dp[i-1][j]`
  * 取第i个物品，背包容积变为`j-coins[i]`,因为是可以重复取，所以`dp[i][j] = dp[i][j-coins[i]] + 1`
  综上，`dp[i][j]`取两者最小：`dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)`
* 初始化dp数组：当i=0时，只有当满足`j%coins[0]==0`时，也就是背包容积是0号物品的整数倍才可以添加，此时`dp[0][j] = j // coins[0]`, 其他情况下背包都无法正好填满，而且题目要求取最小值，所以其他位置初始化为极大值`float('inf')
* 两层for循环遍历 + 打印dp

### Python代码

二维数组
```python{.line-numbers}
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        for j in range(1,amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = j // coins[0]
            else:
                dp[0][j] = float('inf')
        
        for i in range(1, n):
            for j in range(amount + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]] + 1)
        # print(dp)
        if dp[n-1][amount] == float('inf'):
            return -1
        return dp[n-1][amount]

```

一维数组
```python {.line-numbers}
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # dp = [[0]*(amount+1) for _ in range(n)]
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(n):
            for j in range(amount + 1):
                if j >= coins[i]:
                    dp[j] = min(dp[j], dp[j-coins[i]] + 1)
        if dp[amount] == float('inf'): return -1 
        return dp[amount]
       
```

***

## [279.完全平方数](https://leetcode.cn/problems/perfect-squares/description/)

> 文章讲解：https://www.programmercarl.com/0279.%E5%AE%8C%E5%85%A8%E5%B9%B3%E6%96%B9%E6%95%B0.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

和上一道题差不多，用一维数组会更简单一点，主要是对平方的处理

### Python代码
```python {.line-numbers}
class Solution:
    def numSquares(self, n: int) -> int:
        
        if n <=  3: return n
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        for i in range(1, int(n ** 0.5)+1):
            for j in range(n+1):
                if j >= i*i:
                    dp[j] = min(dp[j], dp[j- i*i] + 1)
        
        return dp[n]
```

***

## [139.单词拆分](https://leetcode.cn/problems/word-break/)

> 文章讲解：https://www.programmercarl.com/0139.%E5%8D%95%E8%AF%8D%E6%8B%86%E5%88%86.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC

### 思路

这道题也是完全背包的思路，但是字符串的处理比较特殊，在递推关系的整理的地方需要看讲解

### Python代码
```python {.line-numbers}
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break
        return dp[n]
```
