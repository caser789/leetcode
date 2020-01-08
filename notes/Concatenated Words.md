---
tags: [2019/12/27, data structure/trie, leetcode/472]
title: Concatenated Words
created: '2019-12-26T13:44:58.474Z'
modified: '2019-12-29T09:37:00.875Z'
---

# Concatenated Words

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:
The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

## Solution

```python
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        t = Trie()
        for word in words:
            t[word] = True

        res = []
        for word in words:
            if t.search(word):
                res.append(word)
        return res


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = None

    def __setitem__(self, key, val):
        self.root = self._set_node(self.root, key, val, 0)

    def _set_node(self, node, key, val, i):
        if node is None:
            node = Node(None)

        if i == len(key):
            node.val = val
            return node

        c = key[i]
        j = ord(c) - ord('a')
        node.children[j] = self._set_node(node.children[j], key, val, i+1)
        return node

    def search(self, word):
        return self._search(self.root, word, 0, 0)

    def _search(self, node, word, i, root):
        if node is None:
            return False

        if i == len(word):
            return node.val is True and root > 0

        if root > i:
            return False

        c = word[i]
        j = ord(c) - ord('a')
        n = node.children[j]

        a = self._search(n, word, i+1, root)

        if node.val:
            a = a or self._search(self.root, word, i, root+1)
        return a


```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        t = T()
        for word in words:
            reduce(dict.__getitem__, word, t)[END] = True
        
        res = set()
        def collect(res, node, word, i, cnt):
            if cnt > i:
                return
            if i == len(word):
                if END not in node:
                    return
                if cnt:
                    res.add(word)
                return
            
            if END in node:
                if word[i:] in res:
                    res.add(word)
                    return
                collect(res, t, word, i, cnt+1)
            
            c = word[i]
            collect(res, node[c], word, i+1, cnt)
            
        
        for word in words:
            collect(res, t, word, 0, 0)
        
        return list(res)
```

## schedule

* [x] 2019/12/26
* [x] 2019/12/27
* [ ] 2019/01/01

## refs

* [lc](https://leetcode.com/problems/concatenated-words/)
