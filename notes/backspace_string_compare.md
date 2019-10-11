---
tags: [2019/10/11, leetcode/844, method/2 pointers]
title: Backspace String Compare
created: '2019-09-07T09:29:22.746Z'
modified: '2019-09-26T01:19:27.459Z'
---

# Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

### Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

### Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

### Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

### Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".

## Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.

## Follow up:

Can you solve it in O(N) time and O(1) space?


## Solution

```python
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        n = len(S)
        m = len(T)
        i = n - 1
        j = m - 1
        a = b = 0

        while i >= 0 or j >= 0:
            if i >= 0 and S[i] == '#':
                a += 1
                i -= 1
                continue
            elif j >= 0 and T[j] == '#':
                b += 1
                j -= 1
                continue
            elif i >= 0 and a > 0:
                i -= 1
                a -= 1
                continue
            elif j >= 0 and b > 0:
                j -= 1
                b -= 1
                continue
            elif S[i] != T[j]:
                return False
            else:
                i -= 1
                j -= 1
        return i == j == -1
```

## schedule

* [x] 0 2019/09/15
* [x] 1 2019/09/16
* [x] 1 2019/09/19
* [x] 1 2019/09/26
* [ ] 1 2019/10/11
