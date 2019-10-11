---
tags: [2019/10/22, leetcode/168]
title: Excel Sheet Column Title
created: '2019-09-24T14:47:21.931Z'
modified: '2019-10-08T05:12:05.897Z'
---

# Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...

### Example 1:

Input: 1
Output: "A"

### Example 2:

Input: 28
Output: "AB"

### Example 3:

Input: 701
Output: "ZY"

## Solution

```python
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        
        while n:
            n, c = divmod(n, 26)
            if c == 0:
                c = 26
                n -= 1
            res.append(c)
        
        def num_to_char(n):
            return chr(ord('A') + n - 1)
        
        return ''.join(num_to_char(i) for i in res[::-1])
```

## schedule

* [x] 0 2019/09/26
* [x] 1 2019/09/27
* [x] 1 2019/09/30
* [x] 1 2019/10/07
* [ ] 1 2019/10/22
