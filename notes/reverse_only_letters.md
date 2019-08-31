---
tags: [2019/09/01, leetcode/917, TODO]
title: Reverse Only Letters
created: '2019-08-31T08:53:58.864Z'
modified: '2019-08-31T08:54:21.451Z'
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

```python
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
```
