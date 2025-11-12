# 代码随想录算法训练营第十九天 ｜Leetcode77.组合 、Leetcode216.组合III 、Leetcode17.电话号码的字母组合

## 概要

回溯的思想在二叉树中已经介绍过，回溯也就是递归，用暴力穷举的方法找到所有的可能，按照递归的解法逻辑：
* 确定返回值以及形参：回溯一般没有返回值，形参按照实际情况确定
* 终止条件
* 回溯逻辑

## [77 组合](https://leetcode.cn/problems/combinations/description/)

> 文章讲解：https://www.programmercarl.com/0077.%E7%BB%84%E5%90%88.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE
> 状态：AC

### 思路

回溯的思路还是很简单的，这道题做的时候遇到两个问题：
1. 回溯函数的形参`res`存储每次回溯的临时值，当遇到满足条件的情况，终止回溯时，要向`self.ans`中添加`res`，要注意的是res是一个列表，要通过浅拷贝的方式添加到self.ans中，如果直接添加就是引用的方式，最后回溯完是0.
2. 在最开始处理回溯的逻辑的时候，for循环我用的是下面的方式：
   ```python {.line-numbers}
   for i in range(1, n+1):
       res.append(i)
       self.backtracking(res, n, k)
       res.pop()
   ```
   这种方式会有重复的元素，所以在后面处理for循环条件的时候，要判断`startindex`，回溯传入的形参也要增加一个判断条件。
   ```python {.line-numbers}
   for i in range(start, n+1):
       res.append(i)
       self.backtracking(res, n, k, i+1)
       res.pop()
   ```

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, res, n, k, start):
        if len(res) == k:
            self.ans.append(res[:])
            return 
        for i in range(start, n+1):
            res.append(i)
            self.backtracking(res, n, k, i+1)
            res.pop()
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(res, n, k, 1)
        return self.ans
```

***

## [216 组合总和III](https://leetcode.cn/problems/combination-sum-iii/description/)

> 文章讲解：https://www.programmercarl.com/0216.%E7%BB%84%E5%90%88%E6%80%BB%E5%92%8CIII.html
>
> 状态：AC
>

### 思路

和上一题思路一样

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []

    def backtracking(self, k, n, res, nums, start):
        if nums > n or len(res) > k:
            return 
        if nums == n and len(res) == k:
            self.ans.append(res[:])
            return

        for i in range(start, 10):
            res.append(i)
            nums += i
            self.backtracking(k, n, res, nums, i+1)
            res.pop()
            nums -= i

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtracking(k, n, [], 0, 1)
        return self.ans
```

***

## [17 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)

> 文章讲解：https://www.programmercarl.com/0017.%E7%94%B5%E8%AF%9D%E5%8F%B7%E7%A0%81%E7%9A%84%E5%AD%97%E6%AF%8D%E7%BB%84%E5%90%88.html
>
> 状态：AC
>

### 思路

最开始陷入了误区，将`digitals`和字符串的判断同时放在了回溯函数里，并用两个for循环进行判断，这个时候会遇到无法区分不同按键的情况，比如：2：“abc”,3:"def"，输出的结果是ab、ac等。这种情况应该把digital的index拿出来放在回溯函数的形参里，这样就不会产生冲突。

### Python代码
```python {.line-numbers}
class Solution:
    def __init__(self):
        self.ans = []
    def backtracking(self, digits,res,tel_map, index):
        if len(res) == len(digits):
            self.ans.append(res)
            return 
        if index>=len(digits):
            return 
        letters = tel_map[digits[index]]
        # print(letters)
        for s in letters:
            res += s
            self.backtracking(digits, res, tel_map, index+1)
            res = res[:-1]

        
    def letterCombinations(self, digits: str) -> List[str]:
        tel_map = {"2": "abc",
                   "3": "def",
                   "4": "ghi",
                   "5": "jkl",
                   "6": "mno",
                   "7": "pqrs",
                   "8": "tuv",
                   "9": "wxyz"}
        self.backtracking(digits, "",tel_map,0)
        return self.ans
```
