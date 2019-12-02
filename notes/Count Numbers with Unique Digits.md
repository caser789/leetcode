---
tags: [2019/11/16, application/combination, leetcode/357, method/backtrack]
title: Count Numbers with Unique Digits
created: '2019-11-16T04:32:26.291Z'
modified: '2019-11-24T04:50:02.090Z'
---

# Count Numbers with Unique Digits

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99


## Solution

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        f(1) = 10
        f(2) = 91 = f(1) + 9*9
        f(3) = f(2) + 9*9*8
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n == 2:
            return 91
        
        x = self.countNumbersWithUniqueDigits(n-1)
        start = y = 9
        for i in range(n-1):
            y *= start - i

        
        return x + y
        
```

### backtrace

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            return self.countNumbersWithUniqueDigits(10)
        count = 1
        _max = 10**n
        seen = [False] * 10
        
        def search(prev, seen):
            count = 0
            if prev < _max:
                count += 1
            else:
                return count
            
            for num in range(10):
                if seen[num]: continue
                seen[num] = True
                count += search(prev*10+num, seen)
                seen[num] = False
            
            return count
        
        for num in range(1, 10):
            seen[num] = True
            count += search(num, seen)
            seen[num] = False
            
        return count

```

### backtrack

```python
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n > 10:
            return self.countNumbersWithUniqueDigits(10)
        self.count = 0
        seen = [False] * 10

        def search(i, seen, cnt):
            if cnt < 0:
                return
            self.count += 1

            for num in range(10):
                if i == 0 and num == 0: continue
                if seen[num]: continue

                seen[num] = True
                search(i+1, seen, cnt-1)
                seen[num] = False


        search(0, seen, n)

        return self.count

```

## refs

* [lc](https://leetcode.com/problems/count-numbers-with-unique-digits/)


