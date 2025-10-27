# 代码随想录算法训练营第四天 ｜Leetcode242.有效的字母异位词  、Leetcode349. 两个数组的交集 、Leetcode202. 快乐数、Leetcode1. 两数之和

### [242.有效的字母异位词](https://leetcode.cn/problems/valid-anagram/description/)

>文章讲解：https://programmercarl.com/%E5%93%88%E5%B8%8C%E8%A1%A8%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html   
>状态：AC

### 思路

python哈希的主要方式就是集合`set`和字典`dict`,还有`collections.defaultdict`和`collections.Counter`。python的方式是真的简单。这道题主要就是把两个字符串放到字典里，在比较一下字典就可以了。看了讲解，了解了用数组的方式，也非常巧妙。

### Python代码

**字典`defaultdict`的方式**

```python {.line-numbers}
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for i in s:
            s_dict[i] += 1
        for i in t:
            t_dict[i] += 1
        return s_dict==t_dict
```

**`Counter()`的方式**

```python {.line-numbers}
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cout = Counter(s)
        t_cout = Counter(t)
        return s_cout==t_cout
```

**数组的方式**

```python {.line-numbers}
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            record[ord(i)-ord('a')] += 1
        for i in t:
            record[ord(i)-ord('a')] -= 1
        for i in record:
            if i != 0:
                return False
        return True
```

### [349. 两个数组的交集](https://leetcode.cn/problems/intersection-of-two-arrays/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0349.%E4%B8%A4%E4%B8%AA%E6%95%B0%E7%BB%84%E7%9A%84%E4%BA%A4%E9%9B%86.html   
>状态：AC

### 思路

python真是太方便了，这道题用python真的是简单的夸张，直接秒了

### Python代码

``` python {.line-numbers}
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))
```

### [202. 快乐数](https://leetcode.cn/problems/happy-number/description/)

>题目链接/文章讲解：https://programmercarl.com/0202.%E5%BF%AB%E4%B9%90%E6%95%B0.html 
>状态：AC

### 思路

这道题集合不是难点，感觉处理比较麻烦的地方就是把前面的数字变为每一位相乘的和。感觉python中比较好的方法就是把数字变为字符串，在转化为数字，比较清晰也很简单。

### Python代码

``` python {.line-numbers}
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            n_sum = 0
            for i in str(n):
                n_sum += int(i) ** 2
            if n_sum == 1:
                return True
            else:
                n = n_sum
        return False
```

### [1. 两数之和](https://leetcode.cn/problems/two-sum/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0001.%E4%B8%A4%E6%95%B0%E4%B9%8B%E5%92%8C.html  
>状态：AC

### 思路

当遇到题目出现是否有重复元素的时候就要考虑用哈希的方式，这道题用集合的方式还是很有挑战的，要在一次遍历的过程中，将列表中的元素放入集合，并判断是否有重复的元素。

### Python代码
``` python {.line-numbers}
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen  = set()
        for i, num in enumerate(nums):
            rest = target - num
            if rest in seen:
                return [nums.index(rest), i]
            seen.add(num)
```

