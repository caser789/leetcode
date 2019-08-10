---
tags: [2019/08/10, data structure/stack, leetcode/394]
title: Decode String
created: '2019-08-10T10:08:18.172Z'
modified: '2019-08-10T10:27:22.786Z'
---

# Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

### Examples:

```
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
```

## Solution

```python
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        >>> s = '3[a]2[bc]'
        >>> Solution().decodeString(s)
        'aaabcbc'
        >>> s = '3[a2[c]]'
        >>> Solution().decodeString(s)
        'accaccacc'
        >>> s = '2[abc]3[cd]ef'
        >>> Solution().decodeString(s)
        'abcabccdcdcdef'
        >>> s = '3[z]2[2[y]pq4[2[jk]e1[f]]]ef'
        >>> Solution().decodeString(s)
        'zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef'
        """
        stack = []
        for c in s:
            if c == '[':
                num = 1
                s = 0
                while stack and isinstance(stack[-1], (str, unicode)) and stack[-1].isdigit():
                    s += int(stack.pop()) * num
                    num *= 10
                stack.append(s)
            elif c == ']':
                chars = []
                while stack and isinstance(stack[-1], (str, unicode)):
                    chars.append(stack.pop())
                stack.append(''.join(chars[::-1]) * stack.pop())
            else:
                stack.append(c)
        return ''.join(stack)
```
