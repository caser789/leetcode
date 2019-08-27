---
tags: [2019/08/27, data structure/array, leetcode/1051, method/index]
title: Height Checker
created: '2019-08-27T14:08:10.670Z'
modified: '2019-08-27T14:34:46.493Z'
---

# Height Checker


Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)


### Example 1:

```
Input: [1,1,4,2,1,3]
Output: 3
Explanation:
Students with heights 4, 3 and the last 1 are not standing in the right positions.
```

> 1 <= heights.length <= 100
> 1 <= heights[i] <= 100

## Solution

### Intuition

```python
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        lst = heights[:]
        lst.sort()
        cnt = 0
        for i, j in zip(lst, heights):
            if i != j:
                cnt += 1
        return cnt
```

### map

```python
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        frequencies = [0] * 101
        for num in heights:
            frequencies[num] += 1

        cnt = 0
        current = 0
        for num in heights:
            while frequencies[current] == 0:
                current += 1
            if num != current:
                cnt += 1
            frequencies[current] -= 1
        return cnt
```
