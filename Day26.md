# 代码随想录算法训练营第二十六天 ｜Leetcode452. 用最少数量的箭引爆气球 、Leetcode435. 无重叠区间 、Leetcode763.划分字母区间 

## [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/)

> 文章讲解：https://programmercarl.com/0452.%E7%94%A8%E6%9C%80%E5%B0%91%E6%95%B0%E9%87%8F%E7%9A%84%E7%AE%AD%E5%BC%95%E7%88%86%E6%B0%94%E7%90%83.html   

### 思路

重叠区间的问题还是很特殊的，一定要做排序，然后做区间重合的判断。

### Python代码
```python {.line-numbers}
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:
                res += 1
            else:
                points[i][1] = min(points[i][1],points[i-1][1])

        return res
```

***

## [435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/submissions/679551901/)

> 文章讲解：https://programmercarl.com/0435.%E6%97%A0%E9%87%8D%E5%8F%A0%E5%8C%BA%E9%97%B4.html   

### 思路

这道题和上面的很像，但在做的时候遇到一个误区，当遇到区间的时候，我是将更大的区间直接赋值为之前的区间，而不是更改区间的右边界。

### Python代码
```python {.line-numbers}
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                res += 1
            else:
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        return len(intervals) - res
```

***

## [763.划分字母区间](https://leetcode.cn/problems/partition-labels/description/)

> 文章讲解：https://programmercarl.com/0763.划分字母区间.html#其他语言版本

### 思路

没有思路，这道推好巧妙，看了讲解也不是很理解为什么

### Python代码
```python {.line-numbers}
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict1 = collections.defaultdict(int)
        for i in range(len(s)):
            dict1[s[i]] = i
        end = 0
        start = 0
        res = []
        for i , ch in enumerate(s):
            end = max(end, dict1[ch])
            if i == end:
                res.append(end-start +1)
                start = i+1
        return res

```