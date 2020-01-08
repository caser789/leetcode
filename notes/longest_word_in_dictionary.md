---
tags: [2019/12/30, data structure/trie, leetcode/720]
title: Longest Word in Dictionary
created: '2019-09-07T08:44:41.517Z'
modified: '2019-12-29T12:23:05.588Z'
---

# Longest Word in Dictionary

Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.

### Example 1:
Input:
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation:
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

### Example 2:
Input:
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation:
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".

## Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].


## Solution

```python
import collections

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True
        for i, word in enumerate(words):
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        res = ''
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(res) or len(word) == len(res) and word < res:
                    res = word
                stack.extend([cur[letter] for letter in cur if letter != END])
        return res
```

### trie

```python
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """

        t = Trie()
        
        for word in words:
            t[word] = True
            
        stack = []
        stack.append((t.root, ''))
        
        word = ''
        
        while stack:
            n, prefix = stack.pop()
            
            if len(prefix) > len(word):
                word = prefix
            elif len(prefix) == len(word) and prefix < word:
                word = prefix
            
            for i in range(26):
                m = n.children[i]
                if m and m.val:
                    c = chr(ord('a')+i)
                    stack.append((m, prefix+c))
                    
        return word       
        
        
        
class Node(object):
    def __init__(self, val, capacity=26):
        self.val = val
        self.children = [None] * capacity


class Trie(object):

    def __init__(self, capacity=26):
        self.capacity = capacity
        self.root = None
        self.n = 0

    def __getitem__(self, key):
        """
        >>> t = Trie()
        >>> t['a'] is None
        True
        >>> t = Trie()
        >>> node = Node(None)
        >>> node.children[0] = Node(1)
        >>> t.root = node
        >>> t['a'] == 1
        True
        """
        node = self._get_node(self.root, key, 0)
        if node is not None:
            return node.val

    def _get_node(self, node, key, index):
        """
        >>> t = Trie()
        >>> n = t._get_node(t.root, 'a', 1)
        >>> n is None
        True
        >>> t = Trie()
        >>> node = Node('ab')
        >>> n = t._get_node(node, 'cd', 2)
        >>> n is node
        True
        >>> t = Trie()
        >>> node_a = Node('a')
        >>> node_b = Node('b')
        >>> index = ord('e') - ord('a')
        >>> node_a.children[index] = node_b
        >>> n = t._get_node(node_a, 'cde', 2)
        >>> n is node_b
        True
        """
        if node is None:
            return

        if index == len(key):
            return node

        c = key[index]
        i = ord(c) - ord('a')
        return self._get_node(node.children[i], key, index+1)

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

    def __delitem__(self, key):
        """
        >>> t = Trie()
        >>> del t['a']
        >>> t['a'] = 1
        >>> t['a']
        1
        >>> del t['a']
        >>> t['a'] is None
        True
        """
        self.root = self._del_node(self.root, key, 0)

    def _del_node(self, node, key, index):
        """
        >>> t = Trie()
        >>> node = t._del_node(None, 'ab', 2)
        >>> node is None
        True
        >>> t = Trie()
        >>> node = Node(12)
        >>> node = t._del_node(node, 'ab', 2)
        >>> node is None
        True
        >>> t.n
        -1
        >>> t = Trie()
        >>> node = Node(12)
        >>> node_2 = Node(34)
        >>> node.children[0] = node_2
        >>> node3 = t._del_node(node, 'ab', 2)
        >>> node3 is None
        False
        >>> node3 is node
        True
        >>> t.n
        -1
        >>> t = Trie()
        >>> node = Node(12)
        >>> node_2 = Node(34)
        >>> node.children[2] = node_2
        >>> node3 = t._del_node(node, 'abc', 2)
        >>> node3 is node
        True
        >>> node3.children[2] is None
        True
        >>> t.n
        -1
        """
        if node is None:
            return

        if index == len(key):
            if node.val is not None:
                self.n -= 1
                node.val = None
        else:
            c = key[index]
            i = ord(c) - ord('a')
            node.children[i] = self._del_node(node.children[i], key, index+1)

        if node.val is not None:
            return node

        for c in node.children:
            if c is not None:
                return node
        return None


```

## schedule

* [x] 0 2019/09/12
* [x] 1 2019/09/13
* [x] 1 2019/09/16
* [x] 1 2019/09/23
* [x] 1 2019/10/08
* [x] 1 2019/12/23
* [ ] 2 2019/12/30
