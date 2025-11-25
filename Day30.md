# 代码随想录算法训练营第三十天 ｜01背包问题二维/一维、Leetcode416 分割等和子集

## 01背包问题二维

> https://programmercarl.com/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.html   
> 
> 视频讲解：https://www.bilibili.com/video/BV1cg411g7Y6   

### 思路

01背包问题简单描述一下，有n件物品和一个最多能背重量为`w `的背包。第i件物品的重量是`weight[i]`，得到的价值是`value[i]` 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。
* 确定dp数组的含义：首先是要用二维数组的方式，`dp[i][j]`:表示的是将`0-i`物品放到容积为`j`的背包中，最大价值是多少。
* 确定递推公式：将第`i`件物品放入背包中时，存在两种情况
  * 不放入`i`：那么`dp[i][j] = dp[i-1][j]`和上一次的状态一致。
  * 放入`i`：背包剩余的容积就变成了`j-weight[i]`,此时要判断最大的价值，要判断`i-1`的情况，因为`i`已经放到背包里了，在判断`i`的情况会重复放入。所以此时`dp[i][j] = dp[i-1][j-weight[i]] + value[i]`
* 初始化dp数组：`dp[0][j]`:当i为0时，表示的是将0号物品放入到容积为j的背包中，如果0号物品的重量小于此时背包的容积，0号物品就能放入到背包中，此时最大的价值就是0号物品的价值,`dp[0][j] = value[0]`.如果0号物品的重量大于背包的容积，就不能放入到背包中，背包的价值就是0.
```python 
for j in range(weight[0], w+1):
    dp[0][j] = value[0]
```
* 确定遍历顺序：两层for循环，可以先遍历物品再背包，也可以先背包再物品。先物品的情况下，for循环[1, n+1),[1, w+1)
* 打印dp数组

### Python代码
```python {.line-numbers}
n, bagweight = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [[0] * (bagweight + 1) for _ in range(n)]

for j in range(weight[0], bagweight + 1):
    dp[0][j] = value[0]

for i in range(1, n):
    for j in range(bagweight + 1):
        if j < weight[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

print(dp[n - 1][bagweight])
```

***

## 01背包问题一维

> https://programmercarl.com/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-2.html   
> 视频讲解：https://www.bilibili.com/video/BV1BU4y177kY   

### 思路

一维数组的方式
* dp数组的含义：dp[j]:表示容积为j的背包，最大的价值
* 确定递推关系：二维的递推关系为：`dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])`,一维就是在此基础上将dp[i-1]拷贝到dp[i]上面：`dp[j] = max(dp[j], dp[j-weight[i]] + value[i])`
* 初始化dp数组：dp[0]表示的是当前背包容积为0时，最大的价值，默认所有物品的最大价值都大于0，所以d`p[0] = 0`
* 确定遍历顺序：同样需要两层for循环，如果按照先物品后背包的正向遍历方式，就会存在重复的情况，不能保证每种物品都被放入一次。所以背包for循环中要采取倒序遍历的方式，保证每种物品只会放入一次。
* 打印dp数组

### Python代码
```python {.line-numbers}
n, bagweight = map(int, input().split())
weight = list(map(int, input().split()))
value = list(map(int, input().split()))

dp = [0] * (bagweight + 1)  # 创建一个动态规划数组dp，初始值为0

dp[0] = 0  # 初始化dp[0] = 0,背包容量为0，价值最大为0

for i in range(n):  # 应该先遍历物品，如果遍历背包容量放在上一层，那么每个dp[j]就只会放入一个物品
    for j in range(bagweight, weight[i]-1, -1):  # 倒序遍历背包容量是为了保证物品i只被放入一次
        dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

print(dp[bagweight])
```

## [416 分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/)

> https://programmercarl.com/0416.%E5%88%86%E5%89%B2%E7%AD%89%E5%92%8C%E5%AD%90%E9%9B%86.html     
> 
> 视频讲解：https://www.bilibili.com/video/BV1rt4y1N7jE 

### 思路

带入到01背包里，背包容积就是列表总和/2，物品的重量和价值就是列表本身。
* 确定dp数组含义：dp[i][j]:表示列表总和为j时，列表中0-i的元素能到达的最大总和。
* 确定递推关系：dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
* 初始化dp数组：dp[0][j]:表示总和为j时，放入第一个元素能达到的最大总和，`j>=nums[0]`的情况下，`dp[0][j] = nums[0]`
* 确定遍历顺序：两层for循环，第一层遍历列表长度（物品）[1, n], 第二层遍历总和（背包容积）[nums[0], target]
* 打印dp数组

### Python代码

二维数组
```python {.line-numbers}
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False
        target = nums_sum //2 
        n = len(nums)

        dp = [[0]* (target +1 ) for _ in range(n)]

        for j in range(nums[0], target+1):
            dp[0][j] = nums[0]
        
        for i in range(1, n):
            for j in range(nums[0], target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
        return dp[n-1][target] == target
```

一维数组
```python {.line-numbers}
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 != 0: return False
        target = nums_sum //2 
        n = len(nums)

        dp = [0] * (target + 1)
        for i in range(1, n):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j-nums[i]] + nums[i])
        return dp[target] == target
```