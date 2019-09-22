---
tags: [2019/09/29, application/add, leetcode/415]
title: Add Strings
created: '2019-08-31T09:16:40.741Z'
modified: '2019-09-16T14:43:50.629Z'
---

# Add Strings

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

## Note:

* The length of both num1 and num2 is < 5100.
* Both num1 and num2 contains only digits 0-9.
* Both num1 and num2 does not contain any leading zero.
* You must not use any built-in BigInteger library or convert the inputs to integer directly.

## Solution


## intuitive

```python
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def add(a, b, carry):
            s = ord(a) - ord('0') + ord(b) - ord('0') + ord(carry) - ord('0')
            if s >= 10:
                carry = 1
                i = s - 10
            else:
                carry = 0
                i = s
            return chr(carry + ord('0')), chr(i + ord('0'))

        n = len(num1)
        m = len(num2)
        carry = '0'

        i = n - 1
        j = m - 1
        res = []
        while i >=0 and j >= 0:
            carry, s = add(num1[i], num2[j], carry)
            res.append(s)
            i -= 1
            j -= 1

        while i >=0:
            carry, s = add(num1[i], '0', carry)
            res.append(s)
            i -= 1

        while j >=0:
            carry, s = add(num2[j], '0', carry)
            res.append(s)
            j -= 1

        if carry == '1':
            res.append(carry)

        return ''.join(res[::-1])
```

## schedule

* [x] 0 2019/09/03
* [x] 1 2019/09/04
* [x] 1 2019/09/07
* [x] 1 2019/09/14
* [ ] 1 2019/09/29
