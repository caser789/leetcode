---
tags: [2019/11/21]
title: 132 Pattern
created: '2019-11-21T05:23:12.654Z'
modified: '2019-11-21T05:48:59.532Z'
---

# 132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

## Solution

### O(n*n*n)
```python
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] < nums[k] and nums[k] < nums[j]:
                        return True
        return False

```

### O(n*n)

```python
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        m = float('inf')
        for j in range(n):
            m = min(m, nums[j])
            if m == nums[j]:
                continue
            for k in range(n-1, j, -1):
                if m < nums[k] and nums[k] < nums[j]:
                    return True
        return False

```

### O(n)

```python
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        arr = nums[:]

        for i in range(1, n):
            arr[i] = min(nums[i-1], arr[i-1])

        top = n
        for j in range(n-1, -1, -1):
            if nums[j] <= arr[j]:
                continue
            while top < n and arr[top] <= arr[j]:
                top += 1
            if top < n and nums[j] > arr[top]:
                return True
            top -= 1
            arr[top] = nums[j]
        return False

```

## refs

* [lc](https://leetcode.com/problems/132-pattern/submissions/)
* [leetcode4fun](https://leetcode.com/problems/132-pattern/discuss/94089/Java-solutions-from-O(n3)-to-O(n)-for-%22132%22-pattern-(updated-with-one-pass-slution))
