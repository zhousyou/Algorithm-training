# 代码随想录算法训练营第三十二天 ｜完全背包、LeetCode518.零钱兑换II、LeetCode377.组合总和IV、LeetCode70.爬楼梯

## 完全背包

> 文章讲解：https://www.programmercarl.com/%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85.html#%E5%AE%8C%E5%85%A8%E8%83%8C%E5%8C%85

### 思路

和01背包不同，完全背包可以重复放入物品，所以主要区别在于dp的递推公式和初始化顺序，之前在做01背包时已经误做出了完全背包的递推公式了。
* 确定dp数组含义：和01背包一样，`dp[i][j]`表示从`[0,i]`个物品中选出满足背包容积为j的最大价值
* 确定递推公式：`dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i]] + value[i])`,与01背包的区别就是，当判断取i物品时，容积要做减法变成`j-weight[i]`,但是物品还是i不需要变成`i-1`,这样能保证会重复取。
* 初始化dp数组：要分别判断i=0，j=0的情况。
  * 当j=0时，表示背包容积为0时的最大价值，默认所有物品最大价值都大于0，最大价值为0，所以此时`dp[i][0] = 0`.
  * 当i=0时，表示将0号物品放入到容积为j的背包中，最大价值是多少，因为可以重复放入，所以当`j >= weight[0]`时，`dp[0][j] = dp[0][j-weight[0]] + value[0]`
* 确定遍历顺序：两层for循环，二维dp数组既可以先遍历物品又可以先遍历背包。

一维数组的思路基本与01背包类似，主要区别在于确定遍历顺序时，01背包在确定背包时要倒序遍历，保证每种物品只放入一次，而完全背包不需要倒序遍历，正序遍历就可以保证物品可以重复放入。

### Python代码
```python {.line-numbers}

def perfect_bag_twodims(weight, value, v):
    dp = [[0] * (v+1) for _ in range(len(weight))]
    for j in range(v+1):
        if j >= weight[0]:
            dp[0][j] = dp[0][j-weight[0]] + value[0]
    
    for i in range(1, n):
        for j in range(v + 1):
            if j < weight[i]: 
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-weight[i]] + value[i])
    return dp[n-1][v]

def perfect_bag_onedim(weight, value, v):
    dp = [0] * (v+1)
    for i in range(n):
        for j in range(weight[i], v+1):
            dp[j] = max(dp[j], dp[j-weight[i]] + value[i])
    return dp[j]

if __name__ == "__main__":
    n, v = map(int, input().split())
    weight = [0] * n
    value = [0] * n
    for i in range(n):
        weight[i], value[i] = map(int, input().split())

    ans = perfect_bag_twodims(weight, value, v)
    ans2 = perfect_bag_onedim(weight, value, v)
    print(ans2)
```

***

## [518.零钱兑换II](https://leetcode.cn/problems/coin-change-ii/description/)

> 文章讲解：https://www.programmercarl.com/0518.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2II.html

### 思路

完全背包求组合数，和之前的01背包求组合数问题类似
* dp数组含义：`dp[i][j]`表示[0,i]物品满足背包容积j时的组合数
* 递推公式：和01背包一样，`dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]`
* 初始化dp数组：j=0的情况和传统完全背包一样，容积为0的背包组合数是0.i=0时，只有当背包的容积为`coin[0]`的倍数时，`dp[0][j] = 1`，其他情况要么是装不满要么是装不下，都为0.
* 确定遍历顺序与之前一致

### Python代码

二维数组
```python {.line-numbers}
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]* (amount+1) for _ in range(n)]
        for j in range(amount+1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(1, n):
            for j in range(amount+1):
                if j < coins[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        return dp[n-1][amount]
```

一维数组
```python {.line-numbers}
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp = [[0]* (amount+1) for _ in range(n)]
        dp = [0] * (amount + 1)
        dp[0] = 1
        # for j in range(amount+1):
        #     if j % coins[0] == 0:
        #         dp[0][j] = 1
        for i in range(n):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]
```

***

## [377 组合总和II](https://leetcode.cn/problems/combination-sum-iv/)

> 文章讲解：https://www.programmercarl.com/0377.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8C%E2%85%A3.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

不同于上一道题，这道是排列的总和，区别在于遍历的顺序，要外层是容量内层是物品。

### Python代码
```python {.line-numbers}
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp = [[0]* (target + 1) for _ in range(n)]
        # for j in range(target+1):
        #     if j % nums[0] == 0:
        #         dp[0][j] = 1
        dp = [0] *(target + 1)
        dp[0] = 1
        # for j in range(target+1):
        #     for i in range(1, n):
        #         if j < nums[i] : 
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-nums[i]]
        for j in range(target+1):
            for i in range(n):
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[target]
```

***
