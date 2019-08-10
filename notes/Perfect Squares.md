---
deleted: true
tags: [2019/08/09, leetcode/279]
title: Perfect Squares
created: '2019-08-10T03:08:34.625Z'
modified: '2019-08-10T03:09:42.420Z'
---

# Perfect Squares


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
