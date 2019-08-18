---
tags: [2019/08/17, leetcode/9]
title: Palindrome Number
created: '2019-08-18T04:15:08.545Z'
modified: '2019-08-18T04:15:35.565Z'
---

# Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

### Example 1:

```
Input: 121
Output: true
```

### Example 2:

```
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

### Example 3:

```
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

> Coud you solve it without converting the integer to a string?

## Solution

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True
        digits = []
        n = 0
        while x:
            x, r = divmod(x, 10)
            digits.append(r)
            n += 1

        for i in range(n/2):
            if digits[i] != digits[n-1-i]:
                return False
        return True
```
