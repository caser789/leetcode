---
tags: [2020/01/07, leetcode/3, method/sliding-window]
title: Longest Substring Without Repeating Characters
created: '2019-08-01T05:45:43.471Z'
modified: '2020-01-06T13:49:18.074Z'
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

### sliding window

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        st = set()
        res = 0
        
        while i < n and j < n:
            if s[j] not in st:
                st.add(s[j])
                j += 1
                res = max(res, j-i)
            else:
                st.remove(s[i])
                i += 1
        return res
                
```

## schedule

* [x] 2020/01/06
* [ ] 2020/01/07

## refs

* [lc](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
