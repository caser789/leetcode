---
tags: [2019/11/06, data structure/stack, leetcode/1047]
title: Remove All Adjacent Duplicates In String
created: '2019-10-08T15:02:11.953Z'
modified: '2019-10-22T05:25:49.266Z'
---

# Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
 

## Note:

1 <= S.length <= 20000
S consists only of English lowercase letters.

## Solution

```python
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S:
            flag = True
            while stack and c == stack[-1]:
                stack.pop()
                flag = False
            if flag:
                stack.append(c)
        return ''.join(stack)      
```

## schedule

* [x] 0 2019/10/11
* [x] 1 2019/10/12
* [x] 1 2019/10/15
* [x] 1 2019/10/22
* [ ] 1 2019/11/06
