---
tags: [2019/08/17, leetcode/709]
title: To Lower Case
created: '2019-08-17T03:50:20.233Z'
modified: '2019-08-17T03:50:45.764Z'
---

# To Lower Case

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

### Example 1:

```
Input: "Hello"
Output: "hello"
```

### Example 2:

```
Input: "here"
Output: "here"
```

### Example 3:

```
Input: "LOVELY"
Output: "lovely"
```

## Solution

```python
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = []
        for c in str:
            res.append(c.lower())
        return ''.join(res)
```
