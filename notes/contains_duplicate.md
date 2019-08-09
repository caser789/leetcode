---
tags: [application/array/duplicate, data structure/set, method/search/hash]
title: Contains Duplicate
created: '2019-07-30T14:57:06.427Z'
modified: '2019-08-09T04:38:28.901Z'
---

# Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

### Example 1:

```
Input: [1,2,3,1]
Output: true
```

### Example 2:

```
Input: [1,2,3,4]
Output: false
```

### Example 3:

```
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```


## solution

```py
class Solution(object):
    def containsDuplicate(self, nums):
        """
        >>> s = Solution()
        >>> s.containsDuplicate([1, 2, 3, 1])
        True
        >>> s = Solution()
        >>> s.containsDuplicate([1, 2, 3, 4])
        False
        >>> s = Solution()
        >>> s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        True
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
```
