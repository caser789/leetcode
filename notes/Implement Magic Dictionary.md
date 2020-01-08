---
tags: [2020/01/01, data structure/trie, leetcode/676]
title: Implement Magic Dictionary
created: '2019-12-25T09:51:16.392Z'
modified: '2019-12-29T11:28:59.338Z'
---

# Implement Magic Dictionary

Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.


## Solution

```python
class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = Trie()

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in words:
            self.t[word] = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.t.search(word)


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

    def search(self, word):
        if self.root is None:
            return False

        return self._search(self.root, word, 0, 1, [])

    def _search(self, node, query, index, cnt, prefix):
        if index == len(query):
            return cnt == 0 and node.val and ''.join(prefix) != query

        if cnt < 0:
            return False

        c = query[index]
        i = ord(c) - ord('a')

        if node.children[i] is not None:
            prefix.append(c)
            if self._search(node.children[i], query, index+1, cnt, prefix):
                return True
            prefix.pop()

        for i in range(26):
            if node.children[i] is not None:
                c = chr(i+ord('a'))
                prefix.append(c)
                if self._search(node.children[i], query, index+1, cnt-1, prefix):
                    return True
                prefix.pop()
        return False

```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True

class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = T()


    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in words:
            reduce(dict.__getitem__, word, self.t)[END] = word


    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self._search(word, self.t, 0, 0)

    def _search(self, word, node, i, cnt):
        if not isinstance(node, dict):
            return False

        if i == len(word):
            if END not in node:
                return False
            if node[END] == word:
                return False
            return cnt == 1

        c = word[i]
        if c in node:
            if self._search(word, node[c], i+1, cnt):
                return True

        if cnt == 1:
            return False

        cnt += 1
        for d in node.values():
            if self._search(word, d, i+1, cnt):
                return True

        return False


```

## schedule

* [x] 2019/12/25
* [x] 2019/12/26
* [ ] 2020/01/01

## refs

* [lc](https://leetcode.com/problems/implement-magic-dictionary/)
