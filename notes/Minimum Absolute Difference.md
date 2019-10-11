---
tags: [2019/10/13, leetcode/1200]
title: Minimum Absolute Difference
created: '2019-10-08T15:05:50.289Z'
modified: '2019-10-10T13:28:01.828Z'
---

# Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6


## Solution

```python
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        
        n = len(arr)
        m = 99999999
        s = set()
        for i in range(1, n):
            m = min(m, arr[i]-arr[i-1])
            s.add(arr[i])
        
        return [[arr[i], arr[i]+m] for i in range(n) if arr[i] + m in s]
  
```

## schedule

* [x] 0 2019/10/09
* [x] 1 2019/10/10
* [ ] 1 2019/10/13
