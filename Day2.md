# 代码随想录算法训练营第一天 ｜Leetcode209.长度最小的子数组、Leetcode59.螺旋矩阵II、区间和、开发商购买土地

### [Leetcode209.长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)

> 题目链接：https://leetcode.cn/problems/minimum-size-subarray-sum/
> 文章讲解：https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html
> 视频讲解：https://www.bilibili.com/video/BV1tZ4y1q7XE
> 状态：没做出来

### 思路

没有理清`while`循环的条件判断，以及边界值的判断。我用的条件判断是`while slow<fast`，并用`if else`条件判断区间和是否大于`target`。看了题解之后，区间和的判断可以用`while`条件完成。

### Python代码

**错误代码**

```python {.line-numbers}
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast = 0,0
        sublistadd = nums[0]
        ans = len(nums) + 1
        while slow<fast:
            if sublistadd <= target:
                fast += 1
                sublistadd += nums[fast]
            else:
                ans = fast - slow + 1
                slow += 1
                sublistadd -= nums[slow]
            print(slow, fast, sublistadd, ans)
        if ans > len(nums):
            return 0
        else:
            return ans
```

**正确代码**

```python {.line-numbers}
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow, fast = 0, 0
        ans = len(nums) + 1
        sublistadd = 0
        while fast < len(nums):
            sublistadd += nums[fast]
            while sublistadd >= target:
                ans = min(ans, fast - slow+1)
                sublistadd -= nums[slow]
                slow += 1
            fast += 1
        if ans > len(nums):
            return 0
        else:
            return ans  
```

* 时间复杂度：`O（N）`
* 空间复杂度：`O（1）`

### [Leetcode59.螺旋矩阵II](https://leetcode.cn/problems/spiral-matrix-ii/)

> 题目链接：https://leetcode.cn/problems/spiral-matrix-ii/
文章讲解：https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html
视频讲解：https://www.bilibili.com/video/BV1SL4y1N7mV/
状态： AC

### 思路

刚看题目完全没有思路，看了讲解之后做出来了，重点是分清四条边的遍历以及对应的边界值。每条边存在一个偏移值，每轮循环都要加1，以及当n为奇数时，要单独处理中间的值。

### Python代码

```python {.line-numbers}
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        startx, starty = 0,0
        nums = [[0] * n for _ in range(n)]
        loop = n//2
        offset = 1
        mid = n//2
        count = 1
        while loop:
            for i in range(starty, n-offset):
                nums[startx][i] = count
                count += 1
            for i in range(startx, n-offset):
                nums[i][n-offset] = count 
                count += 1
            for i in range(n-offset, starty, -1):
                nums[n-offset][i] = count
                count += 1
            for i in range(n-offset, startx, -1):
                nums[i][starty] = count
                count += 1
            loop -= 1
            offset += 1
            startx += 1
            starty += 1
        if n%2 != 0:
            nums[mid][mid] = count
        return nums
```

### [区间和](https://kamacoder.com/problempage.php?pid=1070)

> 文章讲解：https://www.programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html 

### 思路

主要是熟悉ACM模式，python处理数据输入输出还是很简单的。

### Python代码

```python {.line-numbers}
import sys
input = sys.stdin.read

def main():
    data = input().split()
    index = 0
    n = int(data[index])
    index += 1
    vec = []
    for i in range(n):
        vec.append(int(data[index + i]))
    index += n

    p = [0] * n
    presum = 0
    for i in range(n):
        presum += vec[i]
        p[i] = presum

    results = []
    while index < len(data):
        a = int(data[index])
        b = int(data[index + 1])
        index += 2

        if a == 0:
            sum_value = p[b]
        else:
            sum_value = p[b] - p[a - 1]

        results.append(sum_value)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
```

**更新后的代码**

```python {.line-numbers}
def main():
    n = int(input())
    sum = 0
    pre = [0] * n
    for i in range(n):
        sum += int(input())
        pre[i] = sum
    # print(pre)
    while True:
        try:
            tmp = list(map(int, input().split()))
            if tmp[0] == 0:
                res = pre[tmp[1]] - 0
            else:
                res = pre[tmp[1]] - pre[tmp[0]-1]
            print(res)
        except:
            break
if __name__ == "__main__":
    main()
```
