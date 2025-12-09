# 代码随想录算法训练营第四十二天 ｜LeetCode42. 接雨水、LeetCode84.柱状图中最大的矩形


## [42 接雨水](https://leetcode.cn/problems/trapping-rain-water/)

> 文章讲解:https://programmercarl.com/0042.%E6%8E%A5%E9%9B%A8%E6%B0%B4.html 

### Python 
```python {.line-numbers}
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        res = 0
        for i in range(1, len(height)):
            if height[i] < height[stack[-1]] :
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) != 0 and height[i] > height[stack[-1]]:
                    mid = stack[-1]
                    stack.pop()
                    if stack:
                        h = min(height[stack[-1]], height[i]) - height[mid]
                        w = i - stack[-1] - 1
                        res += h * w 
                stack.append(i)

        return res

```

***

## [84.柱状图中最大的矩形](https://leetcode.cn/problems/largest-rectangle-in-histogram/)

> 文章讲解：https://programmercarl.com/0084.柱状图中最大的矩形.html#算法公开课、

### Python代码
```python {.line-numbers}
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0,0)
        heights.append(0)
        stack = [0]
        res = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) != 0 and heights[i] < heights[stack[-1]]:
                    mid = stack[-1]
                    stack.pop()
                    if stack:
                        h = heights[mid]
                        w = i - stack[-1] - 1
                        res = max(res, h*w)
                stack.append(i)
        return res
```