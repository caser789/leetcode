---
tags: [2019/11/09, application/combination, data structure/bst, data structure/tree, leetcode/96, method/dp]
title: Unique Binary Search Trees
created: '2019-11-09T08:53:01.526Z'
modified: '2019-12-01T11:58:04.334Z'
---

# Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

### Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## Solution

### brute force

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        1 -- 1
        2 -- 2
        3 -- 5
        f(n) = f(0) * f(n-1)
        g(i, n) = f(i-1) * f(n-i)
        """
        
        if n == 0:
            return 1
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        if n == 3:
            return 5
        
        res = 0
        for i in range(1, n+1):
            left = self.numTrees(i-1)
            right = self.numTrees(n-i)
            res += left * right
        
        return res
```

### dp top-down

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        1 -- 1
        2 -- 2
        3 -- 5
        f(n) = f(0) * f(n-1)
        g(i, n) = f(i-1) * f(n-i)
        """
        cache = {0: 1, 1: 1, 2: 2, 3: 5}
        
        
        def find(n):
            if n in cache:
                return cache[n]
            
            res = 0
            for i in range(1, n+1):
                left = find(i-1)
                right = find(n-i)
                res += left * right
            cache[n] = res
            return cache[n]
        
        return find(n)
```

### dp bottom-up

```python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        1 -- 1
        2 -- 2
        3 -- 5
        f(n) = f(0) * f(n-1)
        g(i, n) = f(i-1) * f(n-i)
        """
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        dp[3] = 5
        
        for i in range(4, n+1):
            res = 0
            for j in range(1, i+1):
                left = j-1
                right = i-j
                res += dp[left] * dp[right]
            
            dp[i] = res
                       
        return dp[n]
```


## refs

* [lc](https://leetcode.com/problems/unique-binary-search-trees/)

