---
tags: [2020/01/05, leetcode/839, method/union find]
title: Similar String Groups
created: '2019-12-02T05:21:54.588Z'
modified: '2020-01-04T11:55:30.776Z'
---

# Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.

## Solution

### brute force

```python
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def is_similar(a, b):
            cnt = 0
            for x, y in zip(a, b):
                if x != y:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 2
        
        
        n = len(A)
        uf = UF(n)
        for i in range(n-1):
            for j in range(i+1, n):
                if is_similar(A[i], A[j]):
                    uf.union(i, j)
        
        return len(uf)
        
        
class UF(object):
    
    def __init__(self, n):
        self.parents = range(n)
        self.size = [0] * n
        self.n = n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        
        if self.size[root_p] < self.size[root_q]:
            self.parents[root_p] = root_q
        elif self.size[root_q] < self.size[root_p]:
            self.parents[root_q] = root_p
        else:
            self.parents[root_p] = root_q
            self.size[root_q] += 1
        
        self.n -= 1
    
    def __len__(self):
        return self.n
        
        

```

### N**2w or NW**2

```python
class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        def is_similar(a, b):
            cnt = 0
            for x, y in zip(a, b):
                if x != y:
                    cnt += 1
                    if cnt > 2:
                        return False
            return cnt == 2
        
        
        n = len(A)
        uf = UF(n)
        m = len(A[0])
        
        word_to_index = {}
        for i, word in enumerate(A):
            word_to_index[word] = i
        
        if n < m:
            for i in range(n-1):
                for j in range(i+1, n):
                    if is_similar(A[i], A[j]):
                        uf.union(i, j)
        else:
            for i in range(n):
                words = list(A[i])
                for x in range(m-1):
                    for y in range(x+1, m):

                        words[x], words[y] = words[y], words[x]
                        
                        w = ''.join(words)
                        if w in word_to_index:
                            uf.union(i, word_to_index[w])
                        
                        words[x], words[y] = words[y], words[x]
                
        
        return len(uf)
        
        
class UF(object):
    
    def __init__(self, n):
        self.parents = range(n)
        self.size = [0] * n
        self.n = n
    
    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p
    
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        
        if self.size[root_p] < self.size[root_q]:
            self.parents[root_p] = root_q
        elif self.size[root_q] < self.size[root_p]:
            self.parents[root_q] = root_p
        else:
            self.parents[root_p] = root_q
            self.size[root_q] += 1
        
        self.n -= 1
    
    def __len__(self):
        return self.n
        
        

```

## refs

* [lc](https://leetcode.com/problems/similar-string-groups/)


## schedule

* [x] 2020/01/04
* [ ] 2020/01/05
