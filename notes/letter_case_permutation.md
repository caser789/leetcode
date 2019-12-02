---
tags: [2019/08/12, application/permutation, leetcode/784, method/backtrack]
title: Letter Case Permutation
created: '2019-08-12T03:54:45.147Z'
modified: '2019-11-24T11:04:33.204Z'
---

# Letter Case Permutation


Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

### Examples:

```
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
```


> S will be a string with length between 1 and 12.
> S will consist only of letters or digits.

## Solution

### backtrack 1

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        >>> S = "a1b2"
        >>> Solution().letterCasePermutation(S)
        ["a1b2", "a1B2", "A1b2", "A1B2"]
        >>> S = "3z4"
        >>> Solution().letterCasePermutation(S)
        ["3z4", "3Z4"]
        >>> S = "12345"
        >>> Solution().letterCasePermutation(S)
        ["12345"]
        """
        res = []
        index = 0
        length = len(S)
        self._letterCasePermutation(res, S, index, length)
        return res

    def _letterCasePermutation(self, res, S, index, length):
        if not index < length:
            return

        upp = S[:index] + S[index].upper() + S[index+1:]
        if upp not in res:
            res.append(upp)
        self._letterCasePermutation(res, upp, index+1, length)
        low = S[:index] + S[index].lower() + S[index+1:]
        if low not in res:
            res.append(low)
        self._letterCasePermutation(res, low, index+1, length)
```

### backtrack 2

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        >>> S = "a1b2"
        >>> Solution().letterCasePermutation(S)
        ["a1b2", "a1B2", "A1b2", "A1B2"]
        >>> S = "3z4"
        >>> Solution().letterCasePermutation(S)
        ["3z4", "3Z4"]
        >>> S = "12345"
        >>> Solution().letterCasePermutation(S)
        ["12345"]
        """
        res = set()
        lst = list(S)
        index = 0
        length = len(S)
        self._letterCasePermutation(res, lst, index, length)
        return list(res)

    def _letterCasePermutation(self, res, lst, index, length):
        res.add(''.join(lst))
        if not index < length:
            return
        lower = lst[:]
        lower[index] = lower[index].lower()
        self._letterCasePermutation(res, lower, index+1, length)

        upper = lst[:]
        upper[index] = upper[index].upper()
        self._letterCasePermutation(res, upper, index+1, length)
```
### backtrack

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        n = len(S)
        tmp = []
        res = []
        
        def search(i):
            if i == n:
                res.append(''.join(tmp))
                return
            
            tmp.append(S[i].upper())
            search(i+1)
            tmp.pop()
            if not S[i].isdigit():
                tmp.append(S[i].lower())
                search(i+1)
                tmp.pop()
        
        search(0)
        return res
```

### bfs

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        >>> S = "a1b2"
        >>> Solution().letterCasePermutation(S)
        ["a1b2", "a1B2", "A1b2", "A1B2"]
        >>> S = "3z4"
        >>> Solution().letterCasePermutation(S)
        ["3z4", "3Z4"]
        >>> S = "12345"
        >>> Solution().letterCasePermutation(S)
        ["12345"]
        """
        root = (S, 0)
        q = [root]
        res = set()
        while q:
            next_q = []
            for s, index in q:
                res.add(s)
                for nei in self.neighbours(s, index):
                    next_q.append(nei)
            q = next_q
        return list(res)

    def neighbours(self, s, index):
        if index >= len(s):
            return
        yield s[:index] + s[index].upper() + s[index+1:], index+1
        yield s[:index] + s[index].lower() + s[index+1:], index+1
```

### from xue yan

```python
class Solution(object):
    def letterCasePermutation(self, S):
        """
        >>> S = "a1b2"
        >>> Solution().letterCasePermutation(S)
        ["a1b2", "a1B2", "A1b2", "A1B2"]
        >>> S = "3z4"
        >>> Solution().letterCasePermutation(S)
        ["3z4", "3Z4"]
        >>> S = "12345"
        >>> Solution().letterCasePermutation(S)
        ["12345"]
        """
        res = ['']
        for c in S:
            tmp = []
            for s in res:
                if c.isdigit():
                    tmp.append(s + c)
                else:
                    tmp.append(s + c.lower())
                    tmp.append(s + c.upper())
            res = tmp
        return res
```
