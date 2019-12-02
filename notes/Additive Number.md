---
tags: [2019/11/17, application/split-array, leetcode/306, method/backtrack]
title: Additive Number
created: '2019-11-17T06:45:00.590Z'
modified: '2019-11-25T10:16:27.181Z'
---

# Additive Number

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

 

Example 1:

Input: "112358"
Output: true
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
 

Constraints:

num consists only of digits '0'-'9'.
1 <= num.length <= 35
Follow up:
How would you handle overflow for very large input integers?

## Solution

```python
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        res = []
        def collect(i, tmp):
            if len(tmp) > 2:
                if tmp[-1] != tmp[-2] + tmp[-3]:
                    return
            if i == n:
                if len(tmp) > 2:
                    res.append(tmp[:])
                return
            
            for j in range(i+1, n+1):
                w = num[i:j]
                if len(w) > 1 and num[i] == '0': continue
                
                tmp.append(int(w))
                collect(j, tmp)
                tmp.pop()
        
        collect(0, [])
        return len(res) > 0
```

### backtrack

```python
class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        tmp = []
        
        def search(i):
            if len(tmp) > 2 and tmp[-1] != tmp[-2] + tmp[-3]:
                return False
            if i == n:
                if len(tmp) < 3:
                    return False
                return True
            
            for j in range(i, n):
                if num[i] == '0' and j > i: return False
                
                w = int(num[i:j+1])
                tmp.append(w)
                if search(j+1): return True
                tmp.pop()
            return False
        
        
        return search(0)
```

## refs

* [lc](https://leetcode.com/problems/additive-number/)

