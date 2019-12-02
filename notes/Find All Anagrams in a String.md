---
tags: [2019/11/03, leetcode/438]
title: Find All Anagrams in a String
created: '2019-11-02T14:10:37.740Z'
modified: '2019-11-02T14:36:34.195Z'
---

#  Find All Anagrams in a String

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


## Solution

### brute force

```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        fingerprint = [0] * 26
        n = len(p)
        for c in p:
            i = ord(c) - ord('a')
            fingerprint[i] += 1
        
        m = len(s)
        
        def match(i):
            if i + n > m:
                return False
            lst = [0] * 26
            for j in range(n):
                c = s[i+j]
                index = ord(c) - ord('a')
                if fingerprint[index] == 0:
                    return False
                lst[index] += 1
            
            return lst == fingerprint
                
            
        res = []
        for i in range(m):
            if match(i):
                res.append(i)
        return res
```


### sliding window

```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        
        counter = {}
        for c in p:
            counter.setdefault(c, 0)
            counter[c] += 1
        
        i = 0
        length = 0
        d = {}
        res = []
        while i < n:
            c = s[i]
            if c in counter:
                d.setdefault(c, 0)
                d[c] += 1
                length += 1
                if length == m:
                    if d == counter:
                        res.append(i-m+1)
                    length -= 1
                    cc = s[i-m+1]
                    d[cc] -= 1
                    
            else:
                d = {}
                length = 0
            i += 1
        return res
            
        
```

### index

```python
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        fp = [0] * 26
        for c in p:
            i = ord(c) - ord('a')
            fp[i] += 1
        
        
        i = 0
        length = 0
        d = [0] * 26
        res = []
        while i < n:
            c = s[i]
            index = ord(c) - ord('a')
            if fp[index] == 0:
                d = [0] * 26
                length = 0
            else:
                d[index] += 1
                length += 1
                if length == m:
                    if d == fp:
                        res.append(i-m+1)
                    length -= 1
                    cc = s[i-m+1]
                    d[ord(cc)-ord('a')] -= 1


            i += 1
        return res
            
        
```


## schedule

* [x] 2019/11/02
* [ ] 2019/11/03

## refs

* [lc](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
