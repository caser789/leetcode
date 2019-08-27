---
tags: [2019/08/27, leetcode/1002, method/index]
title: Find Common Characters
created: '2019-08-27T15:06:31.023Z'
modified: '2019-08-27T15:22:40.568Z'
---

# Find Common Characters

Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.


### Example 1:

```
Input: ["bella","label","roller"]
Output: ["e","l","l"]
```

### Example 2:

```
Input: ["cool","lock","cook"]
Output: ["c","o"]
```


> 1 <= A.length <= 100
> 1 <= A[i].length <= 100
> A[i][j] is a lowercase letter

## Solution

```python
class Solution(object):
    def commonChars(self, words):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        lst_a = [100] * 26
        for word in words:
            lst_b = [0] * 26
            for c in word:
                i = ord(c) - ord('a')
                lst_b[i] += 1
            for i in range(26):
                lst_a[i] = min(lst_a[i], lst_b[i])
        res = []
        for i in range(26):
            if lst_a[i]:
                for _ in range(lst_a[i]):
                    res.append(chr(ord('a') + i))
        return res
```
