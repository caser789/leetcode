---
tags: [2019/11/09, leetcode/208]
title: Implement Trie (Prefix Tree)
created: '2019-11-09T07:29:13.682Z'
modified: '2019-11-09T07:30:11.286Z'
---

# Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


## Solution


```python
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = MyTrie()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        self.t[word] = 2

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        return self.t[word] is not None
        
        
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return prefix in self.t
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode(object):

    def __init__(self, val, r=26):
        self.val = val
        self.children = [None] * r


class MyTrie(object):

    def __init__(self):
        self.root = TrieNode(None)
        self.n = 0

    def __setitem__(self, key, val):
        if val is None:
            del self[key]

        self.root = self._setnode(self.root, key, val, 0)

    def _setnode(self, node, key, val, i):
        if node is None:
            node = TrieNode(None)

        if len(key) == i:
            if node.val is None:
                self.n += 1
            node.val = val
            return node

        j = ord(key[i]) - ord('a')
        node.children[j] = self._setnode(node.children[j], key, val, i+1)
        return node

    def __getitem__(self, key):
        node = self._getnode(self.root, key, 0)
        if node:
            return node.val

    def _getnode(self, node, key, i):
        if node is None:
            return

        if i == len(key):
            return node

        j = ord(key[i]) - ord('a')

        return self._getnode(node.children[j], key, i+1)

    def __delitem__(self, key):
        self.root = self._delnode(self.root, key, 0)

    def _delnode(self, node, key, i):
        if node is None:
            return

        if i == len(key):
            if node.val is not None:
                self.n -= 1
            node.val = None
        else:
            j = ord(key[i]) - ord('a')
            node.children[j] = self._delnode(node.children[j], key, i+1)

        if node.val is not None:
            return node

        for i in range(len(node.children)):
            if node.children[i] is not None:
                return node

    def __len__(self):
        return self.n

    def __contains__(self, key):
        node = self._getnode(self.root, key, 0)
        return node is not None

    def keys(self):
        return self.keys_with_prefix("")

    def keys_with_prefix(self, prefix):
        """
        >>> t = Trie()
        >>> t['a'] = 1
        >>> t['apple'] = 2
        >>> t['application'] = 2
        >>> t['b'] = 2
        >>> t[''] = 2
        >>> t['']
        2
        >>> t.keys()
        ['', 'a', 'apple', 'application', 'b']
        >>> t.keys_with_prefix("app")
        ['apple', 'application']
        """
        keys = []
        node = self._getnode(self.root, prefix, 0)
        tmp = [prefix]
        self.collect(node, tmp, keys)
        return keys

    def collect(self, node, tmp, keys):
        if node is None:
            return
        if node.val is not None:
            keys.append(''.join(tmp))

        for i in range(len(node.children)):
            tmp.append(chr(ord('a')+i))
            self.collect(node.children[i], tmp, keys)
            tmp.pop()

```

## refs

* [lc](https://leetcode.com/problems/implement-trie-prefix-tree/)


