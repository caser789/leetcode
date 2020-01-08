---
tags: [2020/01/01, data structure/trie, leetcode/1032]
title: Stream of Characters
created: '2019-12-25T14:52:01.346Z'
modified: '2019-12-29T12:55:44.341Z'
---

# Stream of Characters

Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.


## Solution

```python
class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.t = Trie()
        for word in words:
            self.t[word[::-1]] = True

        self.letters = []

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.letters.append(letter)
        return self.t.query(self.letters, len(self.letters)-1)


class Node(object):
    def __init__(self, val, capacity=26):
        self.val = val
        self.children = [None] * capacity


class Trie(object):

    def __init__(self, capacity=26):
        self.capacity = capacity
        self.root = None
        self.n = 0

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

    def query(self, letters, i):
        return self._query(self.root, letters, i)

    def _query(self, node, letters, index):
        if node is None:
            return False

        if node.val:
            return True

        if index == -1:
            return False

        c = letters[index]
        i = ord(c) - ord('a')
        child = node.children[i]
        return self._query(child, letters, index-1)

```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        t = T()
        for word in words:
            reduce(dict.__getitem__, word[::-1], t)[END] = True
        self.t = t
        self.letters = []

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.letters.append(letter)
        i = len(self.letters) - 1
        node = self.t
        
        while i > -1:
            if END in node:
                return True
            
            c = self.letters[i]
            if c not in node:
                return False
            node = node[c]
            i -= 1
        return END in node
        
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
```

## schedule

* [x] 2019/12/25
* [x] 2019/12/29
* [ ] 2020/01/01

## refs

* [lc](https://leetcode.com/problems/stream-of-characters/)
