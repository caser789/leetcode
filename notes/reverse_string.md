---
tags: [2019/08/12, leetcode/344, method/recursion]
title: Reverse String
created: '2019-08-12T15:18:51.355Z'
modified: '2019-08-12T15:27:10.467Z'
---

# Reverse String

Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

### Example 1:

```
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

### Example 2:

```
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```

## Solution

```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        >>> s = ["h","e","l","l","o"]
        >>> Solution().reverseString(s)
        ["o", "l", "l", "e", "h"]
        """

        lo = 0
        hi = len(s) - 1
        self.reverse(lo, hi, s)

    def reverse(self, lo, hi, s):
        if lo >= hi:
            return
        s[lo], s[hi] = s[hi], s[lo]
        self.reverse(lo+1, hi-1, s)
```
