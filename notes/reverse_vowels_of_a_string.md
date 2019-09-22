---
tags: [2019/09/30, leetcode/345, method/2 pointers, method/3 while]
title: Reverse Vowels of a String
created: '2019-08-31T09:20:02.087Z'
modified: '2019-09-18T05:45:49.326Z'
---

# Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

### Example 1:

Input: "hello"
Output: "holle"

### Example 2:

Input: "leetcode"
Output: "leotcede"

## Note:

* The vowels does not include the letter "y".

## Solution

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        n = len(res)

        i = 0
        j = n - 1
        vowels = set({'a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U'})
        done = False
        while i < j and not done:
            while i < j and res[i] not in vowels:
                i += 1
            while i < j and res[j] not in vowels:
                j -= 1
            if i >= j:
                done = True
            else:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1

        return ''.join(res)
```

## schedule

* [x] 0 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/08
* [x] 1 2019/09/15
* [ ] 1 2019/09/30
