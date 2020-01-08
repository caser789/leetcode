---
tags: [2020/01/01, data structure/trie, leetcode/677]
title: Map Sum Pairs
created: '2019-12-25T10:15:09.845Z'
modified: '2019-12-29T12:00:54.260Z'
---

# Map Sum Pairs

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5


## Solution

```python
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.t[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.t.keys_with_prefix(prefix)


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

    def keys_with_prefix(self, prefix):
        """
        >>> t = Trie()
        >>> t['abc'] = 1
        >>> t['abcd'] = 2
        >>> t['abce'] = 3
        >>> t['ax'] = 4
        >>> t.keys_with_prefix('ab')
        ['abc', 'abcd', 'abce']
        """
        node = self._get_node(self.root, prefix, 0)
        res = []
        self._collect(node, list(prefix), res)
        return sum(res)

    def _collect(self, node, chars, res):
        """
        >>> t = Trie()
        >>> res = []
        >>> t._collect(None, ['a', 'b'], res)
        >>> not res
        True
        >>> t = Trie()
        >>> node = Node(12)
        >>> res = []
        >>> t._collect(node, ['a', 'b'], res)
        >>> res
        ['ab']
        >>> t = Trie()
        >>> res = []
        >>> node = Node(None)
        >>> node.children[2] = Node(11)
        >>> t._collect(node, ['a', 'b'], res)
        >>> res
        ['abc']
        """
        if node is None:
            return

        if node.val is not None:
            res.append(node.val)

        for i in range(len(node.children)):
            c = chr(ord('a') + i)
            chars.append(c)
            self._collect(node.children[i], chars, res)
            chars.pop()

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



```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = T()


    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        reduce(dict.__getitem__, key, self.t)[END] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """

        res = []
        self._collect(self.t, prefix, 0, res)
        return sum(res)

    def _collect(self, node, prefix, i, res):
        if i < len(prefix):
            c = prefix[i]
            if c not in node:
                return
            self._collect(node[c], prefix, i+1, res)
            return
        if END in node:
            res.append(node[END])

        for k, v in node.items():
            if k == END:
                continue
            self._collect(v, prefix, i, res)


```

## schedule

* [x] 2019/12/25
* [x] 2019/12/26
* [ ] 2020/01/01

## refs

* [lc](https://leetcode.com/problems/map-sum-pairs/)
