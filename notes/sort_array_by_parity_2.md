---
tags: [2019/08/27, leetcode/922, method/2 pointers]
title: Sort Array By Parity II
created: '2019-08-27T14:34:10.513Z'
modified: '2019-08-27T14:47:42.912Z'
---

# Sort Array By Parity II

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

### Example 1:

```
Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```

> 2 <= A.length <= 20000
> A.length % 2 == 0
> 0 <= A[i] <= 1000

## Solution

### Intuition

```python
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
```

### better intuition

```python
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [None] * n
        res[::2] = [n for n in nums if n %2 == 0]
        res[1::2] = [n for n in nums if n %2 == 1]
        return res
```

### 2 pointers

```python
class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in range(0, len(nums), 2):
            if nums[i] % 2 == 1:
                while nums[j] % 2 == 1:
                    j += 2
                nums[i], nums[j] = nums[j], nums[i]
        return nums
```
