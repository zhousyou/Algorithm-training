# 代码随想录算法训练营第一天 ｜Leetcode704.二分查找、Leetcode27.移除元素、Leetcode997.有序数组的平方

### [704 二分查找](https://leetcode.cn/problems/binary-search/) 
> 题目链接：https://leetcode.cn/problems/binary-search/
> 文章讲解：https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
> 视频讲解：https://www.bilibili.com/video/BV1fA4y1o715
> 状态： AC

### 思路
重点理解**左闭右闭** `[left, right]` 和**左闭右开** `[left,right)`的两种写法。
**左闭右闭** `[left, right]` 时，left和right值都可以取到，while条件判断应为`left <= right`，同时`right`值更新为`mid-1`。
**左闭右开** `[left,right)`时，right值不可以取到，`while`条件判断应为`left < right`，同时right值更新为`mid`。

### Python代码实现
``` python {.line-numbers}
# 左闭右闭
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

#左闭右开
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1
```

### 拓展题目

**[35 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)**

简单。二分法的变种，都是找到目标值的位置，如果没有目标输出，`left`将指向需要插入的位置。

```python {.line-numbers}
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return left
```

**[34 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/)**

这道题首先想到的不是二分法，而是双指针的方式，用`left`和`right`分别指向列表的头和尾，在`while`循环中不断向中间收缩，直至满足条件`nums[left] == target and nums[right] == target`，输出此时的`left`和`right`。

```python {.line-numbers}
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right -= 1
            elif nums[left] == target and nums[right] == target:
                return [left, right]
        return [-1, -1]
```
* 时间复杂度：`O(log N)`
* 空间复杂度：`O(1)`

看讲解使用二分法找双边界值的方法，感觉重点在于如何确定**左边界**和**右边界**，当`target==nums[mid]`时，同样进行`left`或者`right`值的更新，直到不满足循环条件。嵌套函数中返回的`left`或`right`的边界值是有偏差的，`left+1`和`right-1`的结果是实际的值，所以要判断当条件满足`(rightboud - 1) < (leftbound + 1)`以及`(rightboud - 1) < 0 or (leftbound + 1) < 0`时，需要返回[-1,-1]。

```python {.line-numbers}
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def rightbounder(nums, target):
            left, right = 0, len(nums)-1
            # ans = -1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid +1
                    # ans = left
            return left
        def leftbounder(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right
        rightboud = rightbounder(nums, target)
        leftbound = leftbounder(nums, target)
        
        if (rightboud - 1) < (leftbound + 1):
            return [-1, -1]
        elif (rightboud - 1) < 0 or (leftbound + 1) < 0:
            return [-1, -1]
        else:
            return [leftbound + 1, rightboud - 1]
```

* 时间复杂度：`O(log N)`
* 空间复杂度：`O(1)`

***

### [27 移除元素](https://leetcode.cn/problems/remove-element/description/) 
> 题目链接：https://leetcode.cn/problems/remove-element/ 
>文章讲解：https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html
>视频讲解：https://www.bilibili.com/video/BV12A4y1Z7LP 
> 状态： AC

### 思路

快慢指针的方式，只需要遍历一遍数组，当`nums[i]==val`时，继续遍历，当`nums[i]!=val`时，将当前索引的值赋值给`nums[k]`，原地修改数组,最后返回k的值。

### Python代码

```python {.line-numbers}
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

### 拓展题目

**[26 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/)**

和上面的一样，只不过要删除的目标值变为了列表中的元素，条件改为`nums[i]!=nums[k]`,当满足条件时，需要更新的值为k的下一个位置的值。

```python {.line-numbers}
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[k] != nums[i]:
                k += 1
                nums[k] = nums[i]
        return k+1
```

**[238 移动零](https://leetcode.cn/problems/move-zeroes/description/)**

和上面思路一样，用快慢指针的方式，当i遇到非零值的时候，**将`nums[i]`与`nums[k]`的值进行交换**,k与i同时移动，当遇到0的时候，i继续移动，k原地等待，所以每次交换，必会有一个0。而且交换的时候一定是`nums[i]`与`nums[k]`进行交换，不可以是`nums[k], nums[i] = nums[i], 0`。

```python {.line-numbers}
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        # tmp = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
```

**[844 比较含退格的字符串](https://leetcode.cn/problems/backspace-string-compare/description/)**

这道题用双指针的方法没有想到，看到题解后才明白要从列表末尾开始逆向遍历，感觉有困难。

相比之下，用出栈入栈的方式更好理解，将两个字符串一个字符一个字符的放入栈中，遇到‘#’时弹出，最后比较两个列表即可。两种方式的时间复杂度都是`O(N+M)`,但双指针的空间复杂度时`O(1)`，另一种是`O(N+M)`.

```python {.line-numbers}
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s):
            ans = []
            for i in s:
                if i != '#':
                    ans.append(i)
                elif i == '#' and len(ans) != 0:
                    ans.pop()
            return ans
        return build(s) == build(t)
```

***

### [977 有序数组的平方](https://leetcode.cn/problems/squares-of-a-sorted-array/) 
>题目链接：https://leetcode.cn/problems/squares-of-a-sorted-array/
>文章讲解：https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html
>视频讲解： https://www.bilibili.com/video/BV1QB4y1D7ep 
>状态：AC

### 思路

快慢指针，需要新建一个列表存储新的值，原地修改尝试了下，不太现实。一个指针指向头，一个指向尾，每次循环都对比下平方值，大的放入新的列表尾，还是比较简单的。

### Python代码

```python {.line-numbers}
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i,j,k = 0,len(nums)-1,len(nums)-1
        ans = [0]*len(nums)
        while i<=j:
            if nums[i]*nums[i] < nums[j]*nums[j]:
                ans[k] = nums[j]*nums[j]
                j -= 1
            else:
                ans[k] = nums[i]*nums[i]
                i += 1
            k -= 1
        return ans
```