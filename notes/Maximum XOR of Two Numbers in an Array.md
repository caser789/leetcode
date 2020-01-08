---
tags: [2019/12/30, data structure/trie, leetcode/421]
title: Maximum XOR of Two Numbers in an Array
created: '2019-12-25T11:50:31.618Z'
modified: '2019-12-29T14:14:47.610Z'
---

# Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

## Solution

```python
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        00101
        11001
        """
        root = TrieNode()

        for num in nums:
            node = root
            for i in range(31, -1, -1):
                tmp = num & 1 << i
                if tmp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero

        res = 0
        for num in nums:
            tmp_val = 0
            node = root
            for i in range(31, -1, -1):
                tmp = num & 1 << i
                if node.one and node.zero:
                    if tmp:
                        node = node.zero
                    else:
                        node = node.one
                    tmp_val += 1 << i
                else:
                    if (node.zero and tmp) or (node.one and not tmp):
                        tmp_val += 1 << i
                    node = node.one or node.zero
            res = max(res, tmp_val)
        return res



class TrieNode(object):
    def __init__(self):
        self.one = None
        self.zero = None

```

## schedule

* [x] 2019/12/25
* [x] 2019/12/29
* [ ] 2019/12/30

## refs

* [lc](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)
