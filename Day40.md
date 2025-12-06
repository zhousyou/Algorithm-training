# 代码随想录算法训练营第四十天 ｜LeetCode647. 回文子串 、LeetCode516.最长回文子序列

## [647. 回文子串](https://leetcode.cn/problems/palindromic-substrings/submissions/682980190/)

> 文章讲解：https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html  

### 思路

回文子串的问题不同于之前的编辑距离，在dp数组的定义上就有所不同
* dp数组的含义：dp[i][j]表示的是[i,j]这个范围里的子串是否是回文子串。
* 确定递推公式：当s[i]==s[j]时，而且上一个状态，dp[i+1][j-1]为回文子串时，dp[i][j] = True。当s[i]!=s[j]时，为False。
* 初始化dp数组：初始化为False
* 确定遍历顺序：从递推公式可以看出：dp[i][j] = dp[i+1][j-1],所以dp需要从下至上，从左至右进行遍历。

### Python代码
```python {.line-numbers}
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        for i in range(n-1, -1 , -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j-i<=1:
                        res +=1
                        dp[i][j] = True
                    elif dp[i+1][j-1]:
                        res += 1
                        dp[i][j] = True
        # print(dp)
        return res
```

***

## [516.最长回文子序列](https://leetcode.cn/problems/longest-palindromic-subsequence/)

> 文章讲解：https://programmercarl.com/0516.%E6%9C%80%E9%95%BF%E5%9B%9E%E6%96%87%E5%AD%90%E5%BA%8F%E5%88%97.html  

### 思路

和上一道题的状态类似
* dp数组的含义：dp[i][j] 表示的是[i,j]这个范围里最长的回文子序列的长度
* 确定递推公式：当s[i] == s[j]时，dp[i][j] = dp[i+1][j-1] + 2.当不相等时，要在dp[i+1][j]与dp[i][j-1]中取一个较大值。

### Python代码
```python {.line-numbers}
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]
```
