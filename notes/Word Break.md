---
tags: [2019/11/07]
title: Word Break
created: '2019-11-07T04:52:58.118Z'
modified: '2019-11-07T13:47:46.368Z'
---

# Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

## Solution

### brute force

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        f(i) = f(i-1) and w in words
        """

        words = set(wordDict)
        
        
        def find(w):
            
            if w in words:
                return True
            
            for wd in words:
                if not w.startswith(wd): continue
                    
                if find(w[len(wd):]):
                    return True
        
        return find(s)
```


### dp top-down

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        f(i) = f(i-1) and w in words
        """
        words = set(wordDict)
        
        cache = {w: True for w in wordDict}
        def find(w):
            
            if w in cache:
                return cache[w]
            
            for wd in words:
                if not w.startswith(wd): continue
                    
                if find(w[len(wd):]):
                    cache[w] = True
                    return True
            cache[w] = False
            return False
            
        
        return find(s)
```

### dp bottom-up

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        f(i) = f(i-1) and w in words
        """

    
        size = len(s)
        words = set(wordDict)
        dp = [False] * (size+1)
        dp[0] = True
        for i in range(1, size+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[size]
```

## refs

* [lc](https://leetcode.com/problems/word-break/)
