# 代码随想录算法训练营第二十八天 ｜Leetcode509. 斐波那契数 、Leetcode70. 爬楼梯、Leetcode746. 使用最小花费爬楼梯 

## [509. 斐波那契数](https://leetcode.cn/problems/fibonacci-number/description/)

> https://programmercarl.com/0509.%E6%96%90%E6%B3%A2%E9%82%A3%E5%A5%91%E6%95%B0.html   
> 
> 视频：https://www.bilibili.com/video/BV1f5411K7mo  
>
> 状态：AC

### 思路

动态规划的第一道题，还是很简单的，按照动态规划五部曲：
* 确定dp数组以及下标含义：值为n时的斐波那契数
* 确定递推公式：`dp[n] = dp[n-1] + dp[n-2]`
* dp数组初始化：dp[0], dp[1] = 0, 1
* 确定遍历顺序：从前向后遍历，区间是[2, n+1)
* 打印dp

### Python代码
```python {.line-numbers}
class Solution:
    def fib(self, n: int) -> int:
        if n<=1: return n
        dp = [0] * (n+1)
        dp[0], dp[1] = 0, 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```

***

## [70. 爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)

> https://programmercarl.com/0070.%E7%88%AC%E6%A5%BC%E6%A2%AF.html   
> 
> 视频：https://www.bilibili.com/video/BV17h411h7UH  
>
> 状态：AC

### 思路

这道题应该算是斐波那契的应用，基本一致，按照动规五部曲：
* 确定dp数组的含义：到达第n阶时共有多少种方法
* 确定递推公式：每次爬楼梯只能上一阶或两阶，所以第n阶楼梯是n-1阶上一次，和n-2阶上两次的和，`dp[n] = dp[n-1] + dp[n-2]`
* dp数组初始化：题目中描述n为正整数，dp[1] = 1, dp[2] = 2
* 确定遍历顺序：从前向后遍历，遍历范围[3,n+1)
* 打印dp数组

### Python代码
```python {.line-numbers}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        # 初始化dp数组，dp数组表示到第n阶有多少种方法
        dp = [0] * (n+1)

        #确定递归公式:dp[n] = dp[n-1] + dp[n-2]
        #确定初始化条件
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
```

***

## [746. 使用最小花费爬楼梯](https://leetcode.cn/problems/min-cost-climbing-stairs/description/)

> https://programmercarl.com/0746.%E4%BD%BF%E7%94%A8%E6%9C%80%E5%B0%8F%E8%8A%B1%E8%B4%B9%E7%88%AC%E6%A5%BC%E6%A2%AF.html   
> 
> 视频讲解：https://www.bilibili.com/video/BV16G411c7yZ  
>
> 状态：AC

### 思路

这题也不难，一遍过，按照动规五部曲：
* 确定dp数组含义：到第n阶时的最小花费
* 确定递推公式：和爬楼梯第n阶时的花费要计算第n-1阶和第n-2阶，`dp[n] = min(dp[n-1]+cost[n-1], dp[n-2]+cost[n-2])`
* dp数组初始化：因为起始位置从0，1开始，所有d`p[0],dp[1] = 0, 0`
* 确定遍历顺序：从前向后遍历，[2,n+1)
* 打印dp数组

### Python代码
```python {.line-numbers}
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 1: return 0
        dp = [0] * (n+1)
        dp[0], dp[1] = 0,0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]
```



