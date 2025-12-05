 # 代码随想录算法训练营第三十九天 ｜LeetCode115.不同的子序列、LeetCode583.两个字符串的删除操作、LeetCode72.编辑距离

 ## [115 不同的子序列]

> 文章讲解：https://programmercarl.com/0115.%E4%B8%8D%E5%90%8C%E7%9A%84%E5%AD%90%E5%BA%8F%E5%88%97.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

这道题是找到s的子序列是t的情况
* 确定dp数组的含义：dp[i][j]:表示的是[0,i-1]的s序列和[0,j-1]的t序列最大的子序列的个数。
* 确定递推公式：还是要分两种情况
  * 当s[i-1] == t[j-1]
  * 当s[i-1] != t[j-1]
  第一种情况，如果用s[i-1]与t[j-1]进行匹配，那么就是正好匹配上，`dp[i][j] = dp[i-1][j-1]`.如果不用s[i-1]进行匹配，相当于需要将最后一个s元素删掉返回上一个状态，也就是dp[i-1][j].综上`dp[i][j] = dp[i-1][j-1] + dp[i-1][j]`
  第二种情况，如果两者不相同，`dp[i][j] = dp[i-1][j]`
* 初始化dp数组：从递推公式来看，需要初始化dp[0][j]和dp[i][0]两种状态。dp[0][j]表示空字符串s可以随便删除元素，出现以j-1为结尾的字符串t的个数，所以dp[0][j]一定是0，因为空字符串无论如何也变不成t。dp[i][0]表示以i-1为结尾的s可以随便删除元素，出现空字符串的个数。所以dp[i][0] = 1

### Python代码
```python {.line-numbers}
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)
        dp = [[0] * (nt+1) for _ in range(ns+1)]

        for i in range(ns+1):
            dp[i][0] = 1
        
        for i in range(1, ns+1):
            for j in range(1, nt+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        # print(dp)
        return dp[-1][-1]
```

***

## [583.两个字符串的删除操作](https://leetcode.cn/problems/delete-operation-for-two-strings/submissions/682819280/)

> 文章讲解：https://programmercarl.com/0583.%E4%B8%A4%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%88%A0%E9%99%A4%E6%93%8D%E4%BD%9C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

本题是要找到删除最少的操作使s,t的子序列相同
* 确定dp数组：dp[i][j]: 表示的是s序列[0,i-1],t序列[0,j-1]需要最少的删除操作使s,t相同。
* 确定递推公式：当word1[i-1] == word2[j-1]时，此时dp[i][j] = dp[i-1][j-1],不需要再做删除操作。当不相等时，要么就删除word1[i-1],要么就删除word2[j-1],所以`dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1`.
* 初始化dp数组：dp[i][0] = i,dp[0][j] = j

### Python代码
```python {.line-numbers}
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)

        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]

        for i in range(word1_len+1):
            dp[i][0] = i
        for j in range(word2_len+1):
            dp[0][j] = j
        # print(dp)
        for i in range(1, word1_len+1):
            for j in range(1, word2_len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        # print(dp)
        return dp[-1][-1]
```

***

## [72.编辑距离](https://leetcode.cn/problems/edit-distance/description/)

> 文章讲解：https://programmercarl.com/0072.%E7%BC%96%E8%BE%91%E8%B7%9D%E7%A6%BB.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

含有多种操作：增加，换位，删除。所以要分别判断
* 确定dp数组含义：p[i][j] 表示以下标i-1为结尾的字符串word1，和以下标j-1为结尾的字符串word2，最近编辑距离为dp[i][j]
* 确定递推公式：
  * 当word1[i-1] == word2[j-1]时：不操作，dp[i][j] = dp[i-1][j-1]
  * 当word1[i-1] != word2[j-1]时：
    * word1删除一个元素，dp[i-1][j],再加上此时的操作，dp[i][j] = dp[i-1][j] + 1
    * word2删除一个元素，同上dp[i][j] = dp[i][j-1] + 1,而且word2删除一个元素等于word1增加一个元素
    * word1替换word1[i-1],使其等于word2[j-1],因为word1[i-1] == word2[j-1]时，相当于此时替换一个元素达到上述状态，也就是dp[i][j] = dp[i-1][j-1] + 1
    综上`dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1`
* 初始化dp数组：和上一题一样dp[i][0] = i,dp[0][j] = j

### Python代码
```python {.line-numbers}
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        return dp[-1][-1]
```
