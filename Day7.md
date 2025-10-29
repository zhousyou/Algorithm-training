# 代码随想录算法训练营第七天 ｜Leetcode344.反转字符串   、Leetcode541.反转字符串II 、替换数字

### [344 反转字符串](https://leetcode.cn/problems/reverse-string/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0344.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.html   
>状态：AC

### 思路

用Python的方式反转字符串有点太简单了，可以用双指针的方式，可以用列表切片的方式。

### Python代码

切片的方式
```python {.line-numbers}
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left, right = 0, len(s)-1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1
        s[:] = s[::-1]
```

双指针的方式
```python {.line-numbers}
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # s[:] = s[::-1]
```

***

### [541 反转字符串II](https://leetcode.cn/problems/reverse-string-ii/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0541.%E5%8F%8D%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2II.html   
>状态：AC

### 思路

这道题和上面一样，也是用切片的方式会很简单，注意的是循环的时候要每隔2k跳一步，再把前k个进行反转。字符串可以先用list()方法转换为列表，会很轻松。

### Python代码

```python {.line-numbers}
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        # print(s)
        for i in range(0,len(s)-1,2*k):
            s[i:i+k] = s[i:i+k][::-1]
            # print(s)
        return "".join(s)
```

***

### [替换数字](https://kamacoder.com/problempage.php?pid=1064)

### 思路

感觉没什么难点，把字符串转化为列表，通过`ord()`找到数字的区间，并将其转化为`number`即可.

### Python代码

```python {.line-numbers}
data = list(input())
for i in range(len(data)):
    if data[i] >= '0' and data[i] <= '9':
        data[i] = 'number'
print("".join(data))
```
