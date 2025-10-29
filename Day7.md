# 代码随想录算法训练营第七天 ｜Leetcode344.反转字符串   、Leetcode541.反转字符串II 、替换数字

### [344 反转字符串](https://leetcode.cn/problems/reverse-string/)

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
