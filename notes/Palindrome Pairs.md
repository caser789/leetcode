---
tags: [2019/12/29, data structure/trie, leetcode/336]
title: Palindrome Pairs
created: '2019-12-27T15:15:45.939Z'
modified: '2019-12-28T04:49:48.821Z'
---

# Palindrome Pairs

Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

```
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
```

Example 2:

```
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
```


## Solution

### brute force

```python
class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26

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

    def __getitem__(self, k):
        keys = []
        self._collect(self.root, keys, k, 0)
        return keys

    def _collect(self, node, keys, k, i):
        if node is None:
            return

        if i == len(k):
            self._collect2(node, [], keys)
            return

        if node.val is not None:
            if self._is_par(k, i, len(k)-1):
                keys.append(node.val)

        c = k[i]
        j = ord(c) - ord('a')
        self._collect(node.children[j], keys, k, i+1)

    def _collect2(self, node, prefix, keys):
        if node is None:
            return

        if node.val is not None:
            if self._is_par(prefix, 0, len(prefix)-1):
                keys.append(node.val)

        for i in range(26):
            c = chr(ord('a') + i)
            prefix.append(c)
            self._collect2(node.children[i], prefix, keys)
            prefix.pop()


    def _is_par(self, lst, i, j):
        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        t = Trie()
        for i, word in enumerate(words):
            t[word[::-1]] = i

        res = []
        for i, word in enumerate(words):
            for j in t[word]:
                if j != i:
                    res.append([i, j])
        return res


```

### past

```python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        t = Trie()

        for i, word in enumerate(words):
            t[word[::-1]] = i

        res = set()
        for i, word in enumerate(words):
            for e in t.search(word, i):
                res.add(e)
        return [list(e) for e in res]


class Node(object):
    def __init__(self, val):
        self.val = val
        self.children = [None] * 26
        self.indexes = set()


class Trie(object):

    def __init__(self):
        self.root = None

    def __setitem__(self, k, v):
        self.root = self._set_node(self.root, k, v, 0)

    def _set_node(self, node, k, v, i):
        if node is None:
            node = Node(None)

        if self._is_par(k, i, len(k)-1):
            node.indexes.add(v)

        if i == len(k):
            node.val = v
            return node

        c = k[i]
        j = ord(c) - ord('a')
        node.children[j] = self._set_node(node.children[j], k, v, i+1)
        return node

    def _is_par(self, word, i, j):
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True

    def search(self, k, j):
        res = set()
        self._collect(self.root, k, 0, j, res)
        return res

    def _collect(self, node, k, i, j, res):
        if node is None:
            return

        if node.val is not None:
            if node.val != j and self._is_par(k, i, len(k)-1):
                res.add((j, node.val))

        if i == len(k):
            for c in node.indexes:
                if c != j:
                    res.add((j, c))
            return

        c = k[i]
        a = ord(c) - ord('a')
        self._collect(node.children[a], k, i+1, j, res)


```

## schedule

* [x] 2019/12/28
* [ ] 2019/12/29

## refs

* [lc](https://leetcode.com/problems/palindrome-pairs/)
