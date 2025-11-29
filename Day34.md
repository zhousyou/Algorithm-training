# 代码随想录算法训练营第三十四天 ｜LeetCode198.打家劫舍、LeetCode213.打家劫舍II、LeetCode337.打家劫舍III

## [198.打家劫舍](https://leetcode.cn/problems/house-robber/submissions/681443741/)

> 视频讲解：https://www.bilibili.com/video/BV1Te411N7SX 
> 
> https://programmercarl.com/0198.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8D.html

### 思路

比较简单
* 确定dp数组含义：dp[i]表示[0,i]最大能达到的价值。
* 确定递推公式：
  * 不取第i个物品：此时dp[i] = dp[i-1]
  * 取第i个物品：因为不能连续取，所以要跳过i-1，dp[i] = dp[i-2] + nums[i]
  综上，dp[i] = max(dp[i-1], dp[i-2] + nums[i])
* 初始化dp数组：从递推公式可以看出，dp[i]的状态依赖于dp[i-1],dp[i-2],所以要初始化dp[0]和dp[1]
  ```python {.line-numbers}
  dp[0] = nums[0]
  dp[1] = max(nums[0], nums[1])
  ```
* 确定遍历顺序：for循环范围[2,n]

### Python代码
```python {.line-numbers}
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if i < 2:
                dp[i] = max(dp[0], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp)
        return dp[n-1]
```

***

## [213.打家劫舍II](https://leetcode.cn/problems/house-robber-ii/submissions/681451068/)


> 视频讲解：https://www.bilibili.com/video/BV1oM411B7xq 
> 
> https://programmercarl.com/0213.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DII.html 

### 思路

和上一题比较存在环的判断，基本思路是一样的，只是需要额外判断两种情况，只包含nums[0]和只包含nums[-1]的情况。

### Python代码

```python {.line-numbers}
class Solution:
    def robRange(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        print(dp)
        return dp[-1]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        res1 = self.robRange(nums[:n-1])
        res2 = self.robRange(nums[1:])
        return max(res1, res2)
```

***

## [337.打家劫舍III](https://leetcode.cn/problems/house-robber-iii/submissions/681455687/)

> 视频讲解：https://www.bilibili.com/video/BV1H24y1Q7sY 
> 
> https://programmercarl.com/0337.%E6%89%93%E5%AE%B6%E5%8A%AB%E8%88%8DIII.html 

### 思路

二叉树的动态规划，主要还是用递归的思想
* 确定dp数组：dp数组长度为2，dp[0]表示不取当前节点，dp[1]表示取当前节点。
* 确定递推关系：
  * 不取当前节点时，可以取左右子节点，左右子节点又分取或者不取的情况，所以dp[0] = max(left[0] + left[1]) + max(right[0], right[1])
  * 取当前节点时，不可以取左右子节点，所以dp[1] = left[0] + right[0]
* 遍历顺序：要采取后序遍历的方式，先处理左右节点，在处理中间节点。

### Python代码
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def robTree(self,node):
        if node is None:
            return (0, 0)
        
        left_val = self.robTree(node.left)
        right_val = self.robTree(node.right)

        val_0 = max(left_val[0], left_val[1]) + max(right_val[0], right_val[1])

        val_1 = left_val[0] + right_val[0] + node.val
        return (val_0, val_1)


    def rob(self, root: Optional[TreeNode]) -> int:
        dp = self.robTree(root)
        return max(dp)
```