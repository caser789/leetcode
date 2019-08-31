---
tags: [2019/09/06, leetcode/859, TODO]
title: Buddy Strings
created: '2019-08-31T09:37:46.330Z'
modified: '2019-08-31T09:37:58.513Z'
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

```
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """

```
