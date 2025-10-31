# 代码随想录算法训练营第八天 ｜Leetcode151.翻转字符串里的单词 、卡码网：55.右旋转字符串 、Leetcode28. 实现 strStr()、 Leetcode459.重复的子字符串

### [151 翻转字符串里的单词](https://leetcode.cn/problems/reverse-words-in-a-string/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0151.%E7%BF%BB%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2%E9%87%8C%E7%9A%84%E5%8D%95%E8%AF%8D.html   
>状态：AC

### 思路
有点简单，python中可以用strip()来处理字符串前后的空格，split()来处理字符串中间的空格。

### Python代码
```python {.line-numbers}
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        s[:] = s[::-1]
        return " ".join(s)
```

***

### [55 右旋转字符串](https://kamacoder.com/problempage.php?pid=1065)

>https://programmercarl.com/kamacoder/0055.%E5%8F%B3%E6%97%8B%E5%AD%97%E7%AC%A6%E4%B8%B2.html
>状态：AC

### 思路

也很简单，用切片的方式，分别处理倒数k个数，和其余的数。

### Python代码
```python {.line-numbers}

k = int(input())
s = input()
s = s[-k:] + s[:-k]
print(s)

```

***

### [28. 实现 strStr()](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0028.%E5%AE%9E%E7%8E%B0strStr.html  
>状态：AC

### 思路
主要是KMP算法的应用，第一次实现的时候，没有用到KMP算法，很基础的遍历匹配字符串的方法。

###  Python代码
```python {.line-numbers}
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        hay_len = len(haystack)
        if hay_len < needle_len:
            return -1
        record = []
        for i in range(0, hay_len):
            # record.append(haystack[i:i+needle_len])
            # print(record)
            if haystack[i:i+needle_len] == needle:
                return i
        return -1
```
