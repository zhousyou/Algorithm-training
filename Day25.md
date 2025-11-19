# 代码随想录算法训练营第二十五天 ｜Leetcode134.加油站 、Leetcode135.分发糖果 、Leetcode860.柠檬水找零钱、Leetcode406.根据身高重建队列

## [134 加油站](https://leetcode.cn/problems/gas-station/)

> 文章讲解：https://www.programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

没有思路，根本想不出来

### Python代码
```python {.line-numbers}
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        curSum = 0  # 当前累计的剩余油量
        totalSum = 0  # 总剩余油量
        start = 0  # 起始位置
        
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            
            if curSum < 0:  # 当前累计剩余油量curSum小于0
                start = i + 1  # 起始位置更新为i+1
                curSum = 0  # curSum重新从0开始累计
        
        if totalSum < 0:
            return -1  # 总剩余油量totalSum小于0，说明无法环绕一圈
        return start
```

***

## [135 分发糖果](https://leetcode.cn/problems/candy/description/)

> 文章讲解：https://www.programmercarl.com/0135.%E5%88%86%E5%8F%91%E7%B3%96%E6%9E%9C.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

### 思路

这个思路就是分两次进行规划，由前至后遍历一次找到右比左大的情况，由后至前遍历一次找到左比右大的情况。

### Python代码
```python {.line-numbers}
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyres = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]: 
                candyres[i] = candyres[i-1] + 1
        # print(candyres)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candyres[i] = max(candyres[i], candyres[i+1] + 1)
        # print(candyres)
        return sum(candyres)
```

***

## [860 柠檬水找零钱](https://leetcode.cn/problems/lemonade-change/description/)

> 文章讲解：https://www.programmercarl.com/0860.%E6%9F%A0%E6%AA%AC%E6%B0%B4%E6%89%BE%E9%9B%B6.html

### 思路

这道题还是比较简单的，需要判断的情况比较少，分情况判断就可以了

### Python代码
```python {.line-numbers}
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dict1 = collections.defaultdict(int)
        for i in range(len(bills)):
            if bills[i] == 5:
                dict1[5] += 1
            elif bills[i] == 10:
                dict1[10] += 1
                dict1[5] -= 1
                if dict1[5] < 0:return False
            elif bills[i] == 20 and dict1[10] > 0:
                dict1[20] += 1
                dict1[10] -= 1
                dict1[5] -= 1
                if dict1[10]<0 or dict1[5]<0: return False
            else:
                dict1[20] += 1
                dict1[5] -= 3
                if dict1[5] < 0 :return False
        # print(dict1)
        return True
```

***

## [406 根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/description/)

> 文章讲解：https://www.programmercarl.com/0406.%E6%A0%B9%E6%8D%AE%E8%BA%AB%E9%AB%98%E9%87%8D%E5%BB%BA%E9%98%9F%E5%88%97.html

### 思路

这道题和分发糖果思路是一样的，先对身高进行降序排列，在对k值进行升序排列，在将这个列表按照k值的顺序插入到列表中。

### Python代码
```python {.line-numbers}
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))

        res = []
        for i in people:
            res.insert(i[1], i)

        return res
```

***
