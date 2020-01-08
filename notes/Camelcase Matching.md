---
tags: [2020/01/01, data structure/trie, leetcode/1023]
title: Camelcase Matching
created: '2019-12-24T09:42:52.934Z'
modified: '2019-12-29T15:22:44.907Z'
---

# Camelcase Matching

A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

 
### Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".

### Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".

### Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

## Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters.

## Solution

```python
class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        t = Trie()
        for query in queries:
            t[query] = True
        
        res = t.collect(pattern)
        return [query in res for query in queries]
             
        
class Node(object):
    def __init__(self, val, capacity=60):
        self.val = val
        self.children = [None] * capacity


class Trie(object):

    def __init__(self, capacity=60):
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
        i = ord(c) - ord('A')
        node.children[i] = self._set_node(node.children[i], key, val, index+1)
        return node

    def collect(self, pattern):
        store = set()
        self._collect(self.root, 0, pattern, '', store)
        return store
    
    def _collect(self, node, pi, pattern, prefix, store):
        if pi == len(pattern):
            if node.val:
                store.add(prefix)
                
            for i, m in enumerate(node.children):
                if m is None: continue
                c = chr(i + ord('A'))
                if c.islower():
                    self._collect(m, pi, pattern, prefix+c, store)         
                
        else:
            for i, m in enumerate(node.children):
                if m is None: continue
                c = chr(i + ord('A'))
                if c == pattern[pi]:
                    self._collect(m, pi+1, pattern, prefix+c, store)
                elif c.islower():
                    self._collect(m, pi, pattern, prefix+c, store)

            
        

```

### default dict

```python
from collections import defaultdict

T = lambda: defaultdict(T)
END = True


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        t = T()
        for query in queries:
            reduce(dict.__getitem__, query, t)[END] = True
        
        s = set()
        
        def collect(node, s, pattern, i, prefix):
            if i == len(pattern):
                if END in node:
                    s.add(''.join(prefix))
                for k, v in node.items():
                    if k is END: continue
                    if k.isupper(): return
                    prefix.append(k)
                    collect(v, s, pattern, i, prefix)
                    prefix.pop()
                
                return
            
            c = pattern[i]
            if c in node:
                prefix.append(c)
                collect(node[c], s, pattern, i+1, prefix)
                prefix.pop()
            
            for k, v in node.items():
                if k is END: continue
                if k.isupper(): continue
                prefix.append(k)
                collect(v, s, pattern, i, prefix)
                prefix.pop()
             
        
        collect(t, s, pattern, 0, [])
        
        return [query in s for query in queries]
        
```

## schedule

* [x] 2019/12/24
* [x] 2019/12/29
* [ ] 2020/01/01

## refs

* [lc](https://leetcode.com/problems/camelcase-matching/)

