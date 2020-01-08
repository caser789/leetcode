---
tags: [2020/01/01, data structure/trie, leetcode/745]
title: Prefix and Suffix Search
created: '2019-12-28T08:06:06.054Z'
modified: '2019-12-29T13:25:14.865Z'
---

# Prefix and Suffix Search

Given many words, words[i] has weight i.

Design a class WordFilter that supports one function, WordFilter.f(String prefix, String suffix). It will return the word with given prefix and suffix with maximum weight. If no word exists, return -1.

Examples:

Input:
WordFilter(["apple"])
WordFilter.f("a", "e") // returns 0
WordFilter.f("b", "") // returns -1
 

Note:

words has length in range [1, 15000].
For each test case, up to words.length queries WordFilter.f may be made.
words[i] has length in range [1, 10].
prefix, suffix have lengths in range [0, 10].
words[i] and prefix, suffix queries consist of lowercase letters only.

## Solution

### brute force

```python
class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        t = Trie()
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                w = word[j:len(word)] + '{' + word
                t[w] = i
        self.t = t

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        w = suffix + '{' + prefix
        res = self.t.search(w)
        return max(res) if res else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = [None] * 27

class Trie(object):
    def __init__(self):
        self.root = None
        
    def __setitem__(self, k, v):
        self.root = self._set_node(self.root, k, v, 0)
    
    def _set_node(self, node, k, v, i):
        if node is None:
            node = Node(None)
        
        if i == len(k):
            node.val = v
            return node
        
        c = k[i]
        j = ord(c) - ord('a')
        node.children[j] = self._set_node(node.children[j], k, v, i+1)
        return node
    
    def search(self, w):
        node = self._get_node(self.root, w, 0)
        res = []
        self._collect(node, res)
        return res
    
    def _get_node(self, node, k, i):
        if node is None:
            return node
        
        if i == len(k):
            return node
        
        c = k[i]
        j = ord(c) - ord('a')
        return self._get_node(node.children[j], k, i+1)
    
    def _collect(self, node, res):
        if node is None:
            return
        
        if node.val is not None:
            res.append(node.val)
        
        for i in range(27):
            self._collect(node.children[i], res)
```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        t = T()
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                w = word[j:] + '#' + word
                reduce(dict.__getitem__, w, t)[END] = i
        self.t = t
            

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        w = suffix + '#' + prefix
        node = self._get_node(self.t, w, 0)
        res = []
        self._collect(node, res)
        return max(res) if res else -1
    
    def _get_node(self, node, w, i):
        if i == len(w):
            return node
        
        c = w[i]
        return self._get_node(node[c], w, i+1)
    
    def _collect(self, node, res):
        if END in node:
            res.append(node[END])
        
        for k, v in node.items():
            if k is END: continue
            self._collect(v, res)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
```

## schedule

* [x] 2019/12/28
* [x] 2019/12/29
* [ ] 2020/01/01

## refs

* [lc](https://leetcode.com/problems/prefix-and-suffix-search/)
