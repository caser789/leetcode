---
tags: [2019/11/17, leetcode/126]
title: Word Ladder II
created: '2019-11-17T08:15:11.940Z'
modified: '2019-11-17T08:16:03.321Z'
---

# Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

## Solution

### brute force

```python
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        
        def is_valid(a, b):
            s = 0
            for i, j in zip(a, b):
                if i != j:
                    s += 1
            return s == 1
        
        res = []
        self.length = len(wordList) + 1
        def collect(pre, seen, tmp):
            if len(tmp) > self.length:
                return
            if pre == endWord:
                res.append(tmp[:])
                self.length = len(tmp)
                return
            
            for word in wordList:
                if word in seen: continue
                if not is_valid(pre, word): continue
                
                seen.add(word)
                tmp.append(word)
                
                collect(word, seen, tmp)
                
                seen.remove(word)
                tmp.pop()
        
        seen = set({beginWord})
        tmp = [beginWord]
        collect(beginWord, seen, tmp)
        return [e for e in res if len(e) == self.length]
        
```

## refs

* [lc](https://leetcode.com/problems/word-ladder-ii/)

