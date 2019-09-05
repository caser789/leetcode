---
tags: [2019/09/06, application/palindrome, leetcode/680, method/greedy]
title: Valid Palindrome II
created: '2019-08-31T09:28:28.529Z'
modified: '2019-09-05T13:54:17.392Z'
---

# Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

### Example 1:

Input: "aba"
Output: True

### Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

## Note:

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

## Solution

```python
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_pali_range(x, y):
            while x < y:
                if s[x] != s[y]:
                    return False
                x += 1
                y -= 1
            return True

        n = len(s)

        for i in range(n/2):
            if s[i] != s[~i]:
                j = n - 1 - i
                return is_pali_range(i+1, j) or is_pali_range(i, j-1)

        return True


```

## schedule

* [x] 0 2019/09/05
* [ ] 1 2019/09/06
