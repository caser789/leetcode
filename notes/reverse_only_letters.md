---
tags: [2019/09/12, data structure/stack, leetcode/917, method/2 pointers, method/3 while]
title: Reverse Only Letters
created: '2019-08-31T08:53:58.864Z'
modified: '2019-09-05T15:32:23.016Z'
---

# Reverse Only Letters

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.


### Example 1:

Input: "ab-cd"
Output: "dc-ba"

### Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

### Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


## Note:

* S.length <= 100
* 33 <= S[i].ASCIIcode <= 122
* S doesn't contain \ or "


## Solution

### 2 pointers
### 3 while

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        n = len(S)
        i = 0
        j = n - 1
        res = list(S)
        done = False
        while not done and i < j:
            while i < j and not S[i].isalpha():
                i += 1
            while i < j and not S[j].isalpha():
                j -= 1
            if i >= j:
                done = True
            else:
                res[i], res[j] = res[j], res[i]
                i += 1
                j -= 1
        return ''.join(res)
```

### stack

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = [c for c in S if c.isalpha()]
        res = []

        for c in S:
            if c.isalpha():
                res.append(stack.pop())
            else:
                res.append(c)
        return ''.join(res)
```

## schedule

* [x] 0 2019/09/01
* [x] 1 2019/09/02
* [x] 3 2019/09/05
* [ ] 3 2019/09/12
