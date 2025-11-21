# 代码随想录算法训练营第二十七天 ｜Leetcode56.合并区间 、Leetcode738.单调递增的数字

## [56.合并区间](https://leetcode.cn/problems/merge-intervals/description/)

> 文章讲解：https://www.programmercarl.com/0056.%E5%90%88%E5%B9%B6%E5%8C%BA%E9%97%B4.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

这题和之前的重叠区间思路一样，在首次实现时，遇到了处理边界值的问题，在向`res`列表中放入值时，我是直接放入原列表的值，这样会忽略列表中的第一个或最后一个元素，所以要先将列表第一个元素放入`res`中，然后遍历比较`res`和原列表中的元素。

### Python代码
```python {.line-numbers}
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        res = []
        res.append(intervals[0])
        if len(intervals) <= 1: return intervals
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else: 
                res.append(intervals[i])
        return res
```

***

## [738.单调递增的数字](https://leetcode.cn/problems/monotone-increasing-digits/description/)

> 文章讲解：https://www.programmercarl.com/0738.%E5%8D%95%E8%B0%83%E9%80%92%E5%A2%9E%E7%9A%84%E6%95%B0%E5%AD%97.html

### 思路

主要是如何判断递增，要从后往前遍历，如果前一位的数字比当前数字大，前一位减一，后面的数字全都变成9。

### Python代码
```python {line-numbers}
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        strnum = list(str(n))
        for i in range(len(strnum)-1, 0 ,-1):
            if strnum[i-1] > strnum[i]:
                strnum[i-1] = str(int(strnum[i-1])-1)
                for j in range(i, len(strnum)):
                    strnum[j] = '9'
        return int("".join(strnum))
```

***
