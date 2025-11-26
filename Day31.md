# 代码随想录算法训练营第三十一天 ｜LeetCode1049.最后一块石头的重量II、LeetCode494.目标和、LeetCode474.一和零

## [1049 最后一块石头的重量II](https://leetcode.cn/problems/last-stone-weight-ii/description/)

> 文章讲解：https://www.programmercarl.com/1049.%E6%9C%80%E5%90%8E%E4%B8%80%E5%9D%97%E7%9F%B3%E5%A4%B4%E7%9A%84%E9%87%8D%E9%87%8FII.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC
>
> 状态：AC

### 思路

和分割等和子集思路一样，重点是如何处理最后的dp[target]

### Python代码

二维数组
```python {.line-numbers}
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = stones_sum//2
        n = len(stones)
        dp = [[0]* (target+1) for _ in range(n)]

        for j in range(stones[0], target+1):
            dp[0][j] = stones[0]
        for i in range(1, n):
            for j in range(target + 1):
                if j < stones[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]] + stones[i])
        print(dp)
        return stones_sum - 2 * dp[n-1][target]
```

一维数组
```python {.line-numbers}
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = stones_sum//2
        n = len(stones)
        # dp = [[0]* (target+1) for _ in range(n)]
        dp = [0] *(target +1)

        for i in range(n):
            for j in range(target, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]] + stones[i])
        return stones_sum - 2 * dp[target]
```

***
 
## [494.目标和](https://leetcode.cn/problems/target-sum/description/)

> 文章讲解：https://www.programmercarl.com/0494.%E7%9B%AE%E6%A0%87%E5%92%8C.html#%E6%80%9D%E8%B7%AF

### 思路

这道题和01背包还是有差别的，传统的01背包是处理背包能达到的最大价值，这道题是背包能拿到最大价值的个数。
* 确定dp数组的含义：`dp[i][j]`表示前i个物品，背包容量为j时，能达到的情况总数
* 确定递推公式：分析递推公式时，最好是能够将穷举一下二维列表的情况，同样是处理第i个物品时，拿或不拿的情况
  * 不拿第i个物品，`dp[i][j] = dp[i-1][j]`
  * 拿第i个物品，首先背包容积要先去掉i，`j-nums[i]`,`dp[i][j] = dp[i-1][j-nums[i]]`
  最终的递推公式`dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]`
* 初始化dp数组：与01背包不同，dp[0][0]表示容积为0的背包放0号物品有几种方法，如果0号物品价值大于0，那么就有一种方式，就是不装物品。当j=0的其他情况下，只有当i==nums[0]时，才有一种情况，其他情况要么是装不满，要么是装不下，都是0。
  ```python
  dp[0][0] = 1
        for j in range(nums_target + 1):
            if j == nums[0]: dp[0][nums[0]] = 1
  ```
  当j=0的情况下，向容积为0的背包里放入物体，只有一种，但是如果物品有为0的情况，需要特殊处理，这时的总数就是为0的元素个数的组合总数，`pow(2, zero_nums)`.
* 确定遍历顺序：也是两层for循环，没啥特殊

### Python代码

二维数组
```python {.line-numbers}
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        if (nums_sum + target) % 2 != 0: return 0
        if abs(target) > nums_sum : return 0
        nums_target = (nums_sum + target) // 2
        n = len(nums)
        dp = [[0] *(nums_target + 1) for _ in range(n)]

        dp[0][0] = 1
        for j in range(nums_target + 1):
            if j == nums[0]: dp[0][nums[0]] = 1
        num_zero = 0
        for i in range(n):
            if nums[i] == 0:
                num_zero += 1
            dp[i][0] = pow(2, num_zero)

        for i in range(1, n):
            for j in range(nums_target+1):
                if j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        print(dp)
        return dp[n-1][nums_target] 
```

一维数组
```python {.line-numbers}
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums_sum = sum(nums)
        if (nums_sum + target) % 2 != 0: return 0
        if abs(target) > nums_sum : return 0
        nums_target = (nums_sum + target) // 2
        n = len(nums)
        # dp = [[0] *(nums_target + 1) for _ in range(n)]
        dp = [0] * (nums_target + 1)
        dp[0] = 1
        
        # for j in range(nums_target + 1):
        #     if j == nums[0]: dp[0][nums[0]] = 1
        # num_zero = 0
        # for i in range(n):
        #     if nums[i] == 0:
        #         num_zero += 1
        #     dp[i][0] = pow(2, num_zero)

        for i in range(n):
            for j in range(nums_target, nums[i]-1, -1):
                dp[j] += dp[j-nums[i]]
        print(dp)
        return dp[nums_target] 
```

***

## [474.一和零](https://leetcode.cn/problems/ones-and-zeroes/description/)

> 文章讲解：https://www.programmercarl.com/0474.%E4%B8%80%E5%92%8C%E9%9B%B6.html#%E5%85%B6%E4%BB%96%E8%AF%AD%E8%A8%80%E7%89%88%E6%9C%AC

### 思路

有点难，i，j是两个维度，不同于正常的01背包

### Python代码

```python {.line-numbers}
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zeronums = s.count('0')
            onenums = len(s) - zeronums
            for i in range(m, zeronums-1, -1):
                for j in range(n, onenums-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeronums][j-onenums] +1)
        return dp[m][n]
```
