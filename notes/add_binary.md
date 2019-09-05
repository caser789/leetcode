---
tags: [2019/09/08, application/add, leetcode/67]
title: Add Binary
created: '2019-08-31T09:24:18.833Z'
modified: '2019-09-05T14:35:26.403Z'
---

# Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

### Example 1:

Input: a = "11", b = "1"
Output: "100"

### Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


## Solution

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []

        def add(a, b, carry):
            s = ord(a) - ord('0') + ord(b) - ord('0') + ord(carry) - ord('0')
            if s > 1:
                carry = '1'
                x = chr((s - 2) + ord('0'))
            else:
                carry = '0'
                x = chr(s + ord('0'))
            return x, carry

        n = len(a)
        m = len(b)
        i = n - 1
        j = m - 1
        carry = '0'
        while i >= 0 and j >= 0:
            x, carry = add(a[i], b[j], carry)
            res.append(x)
            i -= 1
            j -= 1

        while i >= 0:
            x, carry = add(a[i], '0', carry)
            res.append(x)
            i -= 1

        while j >= 0:
            x, carry = add('0', b[j], carry)
            res.append(x)
            j -= 1

        if carry == '1':
            res.append(carry)

        return ''.join(res[::-1])
```

## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [ ] 1 2019/09/08
