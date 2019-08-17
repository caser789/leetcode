---
tags: [2019/08/17, leetcode/1108]
title: Defanging an IP Address
created: '2019-08-17T03:35:23.627Z'
modified: '2019-08-17T03:36:09.107Z'
---

# Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

### Example 1:

```
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"


Constraints:

The given address is a valid IPv4 address.
```

## Solution

```python
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = []
        for c in address:
            if c.isdigit():
                res.append(c)
            else:
                res.append('[.]')
        return ''.join(res)
```
