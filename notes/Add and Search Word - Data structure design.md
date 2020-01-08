---
tags: [2019/12/26, leetcode/211]
title: Add and Search Word - Data structure design
created: '2019-12-25T14:28:29.347Z'
modified: '2019-12-29T07:55:50.317Z'
---

# Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.

## Solution

```python
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        self.t[word] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return bool(self.t.keys_with_pattern(word))


class Node(object):
    def __init__(self, val, capacity=26):
        self.val = val
        self.children = [None] * capacity


class Trie(object):

    def __init__(self, capacity=26):
        self.capacity = capacity
        self.root = None
        self.n = 0

    def __setitem__(self, key, val):
        """
        >>> t = Trie()
        >>> t['ab'] = 12
        >>> t['ab']
        12
        """
        self.root = self._set_node(self.root, key, val, 0)

    def _set_node(self, node, key, val, index):
        """
        >>> t = Trie()
        >>> node = t._set_node(t.root, 'ab', 12, 2)
        >>> node.val == 12
        True
        >>> t = Trie()
        >>> node = t._set_node(t.root, 'ab', 12, 0)
        >>> node.children[0].children[1].val == 12
        True
        """
        if node is None:
            node = Node(None)

        if index == len(key):
            if node.val is None:
                self.n += 1
            node.val = val
            return node

        c = key[index]
        i = ord(c) - ord('a')
        node.children[i] = self._set_node(node.children[i], key, val, index+1)
        return node

    def keys_with_pattern(self, pattern):
        """
        >>> t = Trie()
        >>> t['a'] = 1
        >>> t['ab'] = 2
        >>> t['ac'] = 3
        >>> t['acd'] = 3
        >>> t.keys_with_pattern('a.')
        ['ab', 'ac']
        >>> t.keys_with_pattern('acd')
        ['acd']
        """
        res = []
        self._collect_with_pattern(self.root, [], pattern, res)
        return res

    def _collect_with_pattern(self, node, chars, pattern, res):
        """
        >>> t = Trie()
        >>> node = t._collect_with_pattern(None, ['a', 'c'], 'ac', [])
        >>> node is None
        True
        >>> t = Trie()
        >>> node = Node(1)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'de', res)
        >>> res
        ['ac']
        >>> t = Trie()
        >>> node = Node(None)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'de', res)
        >>> res
        []
        >>> t = Trie()
        >>> node = Node(None)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'def', res)
        >>> res
        []
        >>> t = Trie()
        >>> node = Node(None)
        >>> node.children[5] = Node(1)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'def', res)
        >>> res
        ['acf']
        >>> t = Trie()
        >>> node = Node(None)
        >>> node.children[5] = Node(1)
        >>> node.children[6] = Node(1)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'de.', res)
        >>> res
        ['acf', 'acg']
        """
        if node is None:
            return

        d = len(chars)
        if d == len(pattern):
            if node.val is not None:
                res.append(''.join(chars))
            return

        c = pattern[d]
        if c == '.':
            for i in range(len(node.children)):
                ch = chr(ord('a')+i)
                chars.append(ch)
                self._collect_with_pattern(node.children[i], chars, pattern, res)
                chars.pop()
        else:
            chars.append(c)
            i = ord(c) - ord('a')
            self._collect_with_pattern(node.children[i], chars, pattern, res)
            chars.pop()

```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = T() 

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        reduce(dict.__getitem__, word, self.t)[END] = True        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._get_node(self.t, word, 0)
    
    def _get_node(self, node, word, i):
        if node is True:
            return False
        
        if i == len(word):
            return END in node
        
        c = word[i]
        if c != '.':
            if c in node:
                return self._get_node(node[c], word, i+1)
            return False
        
        for v in node.values():
            if self._get_node(v, word, i+1):
                return True
        return False
        
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

## schedule

* [x] 2019/12/25
* [x] 2019/12/29
* [ ] 2019/12/30

## refs

* [lc](https://leetcode.com/problems/add-and-search-word-data-structure-design/)
