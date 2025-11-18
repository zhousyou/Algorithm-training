# 代码随想录算法训练营第二十四天 ｜Leetcode122.买卖股票的最佳时机 、Leetcode55.跳跃游戏 、Leetcode45.跳跃游戏II、Leetcode1005.K次取反后最大化的数组和

## [122 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/description/)

> 文章讲解：https://www.programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

没想到解法，看讲解才理解，找到所有为正数的差值的和就可以，每个为正数的差值就是一次买卖，就是局部最优的情况，所有的累加在一起就是全局最优。

### Python代码
```python {.line-numbers}

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)-1):
            res += max(0, prices[i+1] - prices[i])
        return res
```

***

## [55 跳跃游戏](https://leetcode.cn/problems/jump-game/description/)

> 文章讲解：https://www.programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html

### 思路

也是没有思路，看完讲解才理解，局部最优的情况就是每一步所能覆盖的最大范围，当累加的范围超过数组长度时就是True，反之就是False。只要知道覆盖范围能够cover就可以，不需要关注具体是怎么移动的

### Python代码
```python {.line-numbers}
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        if len(nums) == 1 :return True
        i = 0
        while i <= cover:
            cover = max(cover, i + nums[i])
            if cover >= len(nums)-1:
                return True
            i+=1
        return False
```

***

## [45 跳跃游戏II](https://leetcode.cn/problems/jump-game-ii/description/)

> 文章讲解：https://www.programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html

### 思路

和上一题一样，局部最优的情况就是每一步都是最大的范围，当超过当前最优的情况时，在考虑下一步最大的范围，只要最大范围能够超过数组长度就一定能cover，同样是不需要关注具体是怎么移动的

### Python代码

```python {.line-numbers}
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        cur_distance = 0
        ans = 0
        next_distance = 0
        for i in range(len(nums)):
            next_distance = max(next_distance, nums[i] + i)
            if i == cur_distance:
                cur_distance = next_distance
                ans += 1
            if cur_distance >= len(nums)-1:
                return ans
        return ans
```

***

## [1005 K次取反后最大化的数组和](https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/description/)

> 文章讲解：https://www.programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html

### 思路

这道题有点思路，首先要将数据排序，优先反转数组中的负数，如果还剩余步数，在反转数组中的最小的数。

### Python代码
```python {.line-numbers}
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k >0:
            if nums[i] < 0: 
                nums[i] = -nums[i]
                k -= 1
            i += 1
        if k > 0:
            nums.sort()
        while k > 0:
            nums[0] = -nums[0]
            k -= 1
        return sum(nums)
```

***
