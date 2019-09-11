---
tags: [2019/09/16, leetcode/859]
title: Buddy Strings
created: '2019-08-31T09:37:46.330Z'
modified: '2019-09-09T11:31:25.624Z'
---

# Buddy Strings

Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.


### Example 1:

Input: A = "ab", B = "ba"
Output: true

### Example 2:

Input: A = "ab", B = "ab"
Output: false

### Example 3:

Input: A = "aa", B = "aa"
Output: true

### Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true

### Example 5:

Input: A = "", B = "aa"
Output: false


## Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.

## Solution

```python
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        indexes = []
        n = len(A)
        m = len(B)

        if n != m:
            return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        for i in range(m):
            if A[i] != B[i]:
                indexes.append(i)

        if len(indexes) != 2:
            return False

        i, j = indexes
        return A[i] == B[j] and B[i] == A[j]
```

## schedule

* [x] 0 2019/09/05
* [x] 1 2019/09/06
* [x] 0 2019/09/09
* [ ] 0 2019/09/16
