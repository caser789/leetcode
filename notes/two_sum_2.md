---
title: Two Sum II - Input array is sorted
created: '2019-08-03T15:01:15.844Z'
modified: '2019-08-03T15:01:34.173Z'
---

# Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

### Example:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

## Solution

```python
class Solution(object):
    def twoSum(self, numbers, target):
        """
        >>> Solution().twoSum([2, 7, 11, 15], 9)
        [1, 2]
        """
        hi = len(numbers)-1
        for i, num in enumerate(numbers):
            j = self.find(numbers, i+1, hi, target-num)
            if j != -1:
                return [i+1, j+1]

    def find(self, numbers, lo, hi, target):
        while lo <= hi:
            mi = (lo+hi) / 2
            v = numbers[mi]
            if v == target:
                return mi

            elif v < target:
                lo = mi + 1
            else:
                hi = mi - 1
        return -1
```
