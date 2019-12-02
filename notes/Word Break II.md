---
tags: [2019/11/07, application/split-array, leetcode/140, method/backtrack, method/dp]
title: Word Break II
created: '2019-11-07T14:31:53.441Z'
modified: '2019-11-25T10:45:52.101Z'
---

# Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

## Solution

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        size = len(s)
        if size == 0:
            return []
        
        words = set(wordDict)
        dp = [0] * (size+1)
        dp[0] = 1
        for i in range(1, size+1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
        
        
        if not dp[-1]:
            return []
        
        def dfs(length, res, path):
            if length == 0:
                res.append(' '.join(reversed(path)))
                return
            
            for i in range(length):
                cur = s[i:length]
                
                if dp[i] and cur in words:
                    path.append(cur)
                    dfs(i, res, path)
                    path.pop()
        
        res = []
        path = []
        dfs(size, res, path)
        return res
            
```

### backtrack

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        st = set(wordDict)
        n = len(s)
        
        res = []
        tmp = []
        
        def search(i):
            if i == n:
                res.append(' '.join(tmp))
                return
            
            for j in range(i, n):
                w = s[i:j+1]
                if w not in st: continue
                
                tmp.append(w)
                search(j+1)
                tmp.pop()
        
        search(0)
        return res
```

### dp + backtrack

```python
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        if not n:
            return []
        
        words = set(wordDict)
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(n+1):
            for j in range(i):
                if s[j:i] in words and dp[j]:
                    dp[i] = True
        if not dp[-1]:
            return []
        
        res = []
        tmp = []
        def search(i):
            if i == n:
                res.append(' '.join(tmp))
                return
            
            for j in range(i, n):
                w = s[i:j+1]
                if w not in words: continue
                tmp.append(w)
                search(j+1)
                tmp.pop()
        
        search(0)
        return res
            
```

## refs

* [lc](https://leetcode.com/problems/word-break-ii/)
