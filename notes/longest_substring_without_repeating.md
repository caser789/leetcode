---
tags: [hash, string]
title: Longest Substring Without Repeating Characters
created: '2019-08-01T05:45:43.471Z'
modified: '2019-08-02T05:34:55.908Z'
---

#  Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

### Example 1:

```
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:

```
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.  Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Solution

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        >>> Solution().lengthOfLongestSubstring('abcabcbb')
        3
        >>> Solution().lengthOfLongestSubstring('bbbbb')
        1
        >>> Solution().lengthOfLongestSubstring('pwwkew')
        3
        >>> Solution().lengthOfLongestSubstring('abba')
        2
        """
        c_to_index = {}
        start = -1
        m = 0

        for i, c in enumerate(s):
            if c in c_to_index:
                start = max(c_to_index[c], start)
            d = i - start
            m = max(m, d)
            c_to_index[c] = i
        return m
```
