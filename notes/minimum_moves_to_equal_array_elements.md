---
tags: [2019/09/28, leetcode/453]
title: Minimum Moves to Equal Array Elements
created: '2019-09-24T15:09:26.210Z'
modified: '2019-09-24T15:09:54.997Z'
---

# Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

## Solution

```
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```
