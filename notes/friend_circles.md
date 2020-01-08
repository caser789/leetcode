---
tags: [2020/01/03, leetcode/547, method/union find]
title: Friend Circles
created: '2019-08-10T13:58:01.047Z'
modified: '2020-01-02T13:58:09.877Z'
---

# Friend Circles

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

### Example 1:

```
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.
```

### Example 2:

```
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
```

> N is in range [1,200].
> M[i][i] = 1 for all students.
> If M[i][j] = 1, then M[j][i] = 1.

## Solution

```python
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        >>> M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
        >>> Solution().findCircleNum(M)
        2
        """
        m = len(M)
        n = len(M[0])
        uf = UF(m)
        for i in range(m):
            for j in range(n):
                if M[i][j] == 0: continue
                uf.union(i, j)
        return uf.n


class UF(object):

    def __init__(self, n):
        self.parents = range(n)
        self.size = [0] * n
        self.n = n

    def union(self, p, q):
        p_parent = self.find(p)
        q_parent = self.find(q)
        if p_parent == q_parent:
            return
        if self.size[p_parent] < self.size[q_parent]:
            self.parents[p_parent] = q_parent
        elif self.size[q_parent] < self.size[p_parent]:
            self.parents[q_parent] = p_parent
        else:
            self.parents[q_parent] = p_parent
            self.size[p_parent] += 1
        self.n -= 1

    def find(self, p):
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)
```

## schedule

* [x] 2020/01/02
* [ ] 2020/01/03

## refs

* [lc](https://leetcode.com/problems/friend-circles/)

