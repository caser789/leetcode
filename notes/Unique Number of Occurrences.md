---
tags: [2019/11/04, leetcode/1207]
title: Unique Number of Occurrences
created: '2019-10-08T15:06:34.293Z'
modified: '2019-10-23T11:57:49.840Z'
---

# Unique Number of Occurrences

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

## Solution

```python
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = {}
        for num in arr:
            counter.setdefault(num, 0)
            counter[num] += 1
        
        n = len(counter)
        m = len(set(counter.values()))
        return n == m
```
### index

```python
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        counter = {}
        n = 0
        for num in arr:
            counter.setdefault(num, 0)
            counter[num] += 1
            n += 1
        
        lst = [1] * (n+1)
        for k, v in counter.items():
            if lst[v] < 0:
                return False
            lst[v] = -1
        return True
```


## schedule

* [x] 0 2019/10/09
* [x] 1 2019/10/10
* [x] 1 2019/10/13
* [x] 1 2019/10/20
* [ ] 1 2019/11/04
