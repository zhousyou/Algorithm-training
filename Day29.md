# 代码随想录算法训练营第二十九天 ｜Leetcode62.不同路径 、Leetcode63.不同路径II、Leetcode343.整数拆分、Leetcode96.不同的二叉搜索树

## [62 不同路径](https://leetcode.cn/problems/unique-paths/description/)

> 文章讲解：https://www.programmercarl.com/0062.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84.html

### 思路

还是比较简单的，按照动归五部曲：
* 确定dp数组含义：dp是一个二维数组，`dp[i][j]`表示机器人到`[i,j]`时有多少种路径。
* 确定递推公式：机器人只能向右向下移动一格，所以`dp[i][j]`的上一个状态就是`dp[i-1][j],dp[i][j-1]`.`dp[i][j] = dp[i-1][j] + dp[i][j-1]`
* 初始化dp数组：主要考虑两条边的情况，dp[i][0]和dp[0][j]这两种情况下都是1.
* 确定遍历顺序：两层for循环，从前向后遍历，从1开始。
* 打印dp数组

### Python代码
```python{.line-numbers}
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n]*m
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
```

***

## [63 不同路径II](https://leetcode.cn/problems/unique-paths-ii/description/)

> 文章讲解：https://www.programmercarl.com/0063.%E4%B8%8D%E5%90%8C%E8%B7%AF%E5%BE%84II.html

### 思路

和上一道一样，只不过需要判断障碍物的情况，障碍物又分为两种，一种是在边上，也就是`dp[i][0],dp[0][j]`上存在障碍物。另一种是在中间存在障碍物。
* 边上存在障碍物的情况，当初始化dp数组时，如果遇到障碍物的情况，`dp[i][0] = 0`, `dp[0][j] = 0`,并终止循环，后续都为0
* 中间存在障碍物的情况，进行遍历时，遇到障碍物，`dp[i][j] = 0` 即可.

在初始化dp数组时遇到一个问题需要说明下，二维数组我是按照下面这种方式初始化的：
`dp = [[0]*n]*m`
这种方式存在问题，**这是对m个同一个列表的引用**，当修改其中一个可变列表时，其他列表也会被修改。比如：
```python {.line-numbers}
n = 1
m = 2
dp = [[0]*n]*m  # dp: [[0],[0]]
# 检查是否是同一个对象
print(f"dp[0] is dp[1]: {dp[0] is dp[1]}")  # True - 是同一个对象！

# 当 i=0 时
dp[0][0] = 1
print(f"修改后: {dp}")  # [[1], [1]] - 两个都改变了！
```
所以，正确的二维数组初始化的方式应该用列表推导式的方式来创建独立的子列表：
```python
dp = [[0]*n for _ in range(m)]
```

### Python代码
```python {.line-numbers}
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # print(m,n)
        dp = [[0]*n for _ in range(m)]
        # print(dp)
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                # print("2:",dp)
                break
            else:
                dp[i][0] = 1
                # print("1:",dp)
                # print(obstacleGrid[i][0], obstacleGrid[1][0])
        # print(dp)
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                dp[0][j] = 1
        # print(dp)
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[m-1][n-1]
```

***

## [343 整数拆分](https://leetcode.cn/problems/integer-break/description/)

> 文章讲解：https://www.programmercarl.com/0343.%E6%95%B4%E6%95%B0%E6%8B%86%E5%88%86.html

### 思路

这道题还是比较难，按照动归五部曲来总结：
* 确定dp数组的含义：dp[n]即为题目所求，分拆数字n，可以得到的最大乘积dp[n]
* 确定递推公式：一个正整数`i`，可以被拆分为`j`和`i-j`.所得到的乘积为`i*(i-j)`,同时`i-j`也可以表示为`dp[i-j]`,另一个可能的结果是`i*dp[i-j]`.所以递推公式为`dp[i] = max(i*(i-j),i*dp[i-j],dp[i])`
* 初始化dp数组，题中强调了拆分的正整数大于等于2，所以只需要初始化`dp[2] = 1` 即可。
* 确定遍历顺序，两层for循环，第一层`[3,n+1]`,第二层`[1,i]`.
* 打印dp数组

### Python代码
```python {.line-numbers}
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i+1):
                dp[i] = max(j*dp[i-j] , j*(i-j),dp[i])
        return dp[n]
```

***

## [96 不同的二叉搜索树](https://leetcode.cn/problems/unique-binary-search-trees/description/)

> 文章讲解：https://www.programmercarl.com/0096.%E4%B8%8D%E5%90%8C%E7%9A%84%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

这道题同样存在难点，重点是如何找到递推关系
* 确定dp数组的含义：dp[n]同样为题目所求，节点为n个，共有多少个二叉搜索树。
* 确定递推公式：要分节点判断，以n = 3为例，
    * 当1为头节点时，左子树为0，右子树为2，共有2种情况: `dp[0] * dp[2]`
    * 当2位头节点时，左子树为1，右子树为1，共有1种情况：`dp[1] * dp[1]`
    * 当3为头节点时，左子树为2，右子树为0，共有2种情况：`dp[2] * dp[0]`
  所以如果有i个节点，可以被拆分为j-1和i-j,那么归纳为递推公式就是：`dp[i] += dp[j-1] * dp[i-j]`
* 初始化dp数组：dp[0] = 1
* 确定遍历顺序：两层for循环、
* 打印dp数组

### Python代码
```python {.line-numbers}
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        print(dp)
        return dp[n]
```
