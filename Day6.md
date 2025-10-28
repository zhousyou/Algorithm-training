# 代码随想录算法训练营第六天 ｜Leetcode454.四数相加II   、Leetcode383. 赎金信 、Leetcode15. 三数之和 、Leetcode18. 四数之和

### [454 四数相加II ](https://leetcode.cn/problems/4sum-ii/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0454.%E5%9B%9B%E6%95%B0%E7%9B%B8%E5%8A%A0II.html   
>状态：AC

### 思路

这道题用字典实现还是很简单的，思路很清晰：
* 将`nums1`和`nums2`的和建立字典，`key`是两者之和，`value`是出现的次数。
* 在`nums3`和`nums4`中找到满足条件的情况：`0-（nums1+nums2）`，如果字典中存在则把次数记录下来。
这道题简单在于不需要考虑去重的情况，也不需要输出符合条件的数据，只需要输出符合条件的次数。

### Python代码
```python {.line-numbers}
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        record = defaultdict(int)
        ans = 0
        for i in nums1:
            for j in nums2:
                record[i+j] += 1
        for i in nums3:
            for j in nums4:
                if -(i+j) in record.keys():
                    ans += record[-(i+j)]
        return ans
```

### [383. 赎金信](https://leetcode.cn/problems/ransom-note/description/)

>题目链接/文章讲解：https://programmercarl.com/0383.%E8%B5%8E%E9%87%91%E4%BF%A1.html  
>状态：AC

### 思路

这道题和之前的题很类似，都是找字典中是否重复出现过某个字符。看讲解的时候看到用`Counter()`计算差集的方法很巧妙，代码放到下面了。

### Python代码

```python {.line-numbers}
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_count = Counter(magazine)
        for i in ransomNote:
            if i not in mag_count.keys():
                return False
            mag_count[i] -= 1
            if mag_count[i] < 0 :
                return False
        return True
```
用`Counter()`计算差集的方式
```python {.line-numbers}
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
```

### [15. 三数之和](https://leetcode.cn/problems/3sum/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0015.%E4%B8%89%E6%95%B0%E4%B9%8B%E5%92%8C.html  

### 思路

用集合的方法不是很方便，用双指针的方法很清晰。

### Python代码
```python {.line-numbers}
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums)):
            # 如果第一个元素已经大于0，不需要进一步检查
            if nums[i] > 0:
                return result
            
            # 跳过相同的元素以避免重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while right > left:
                sum_ = nums[i] + nums[left] + nums[right]
                
                if sum_ < 0:
                    left += 1
                elif sum_ > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # 跳过相同的元素以避免重复
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    while right > left and nums[left] == nums[left + 1]:
                        left += 1
                        
                    right -= 1
                    left += 1
                    
        return result
```

### [18. 四数之和](https://leetcode.cn/problems/4sum/description/)

>题目链接/文章讲解/视频讲解：https://programmercarl.com/0018.%E5%9B%9B%E6%95%B0%E4%B9%8B%E5%92%8C.html  

### 思路

这道题是三数之和的升级版，用双指针的方式同样可以做出来，用字典的方式的话，需要O(n*3)的时间复杂度。

### Python代码
```python {.line-numbers}
```