---
tags: [2019/12/22, leetcode/818, method/dp]
title: Race Car
created: '2019-12-18T15:02:31.894Z'
modified: '2019-12-19T15:35:49.006Z'
---

# Race Car

Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
 

Note:

1 <= target <= 10000.

## Solution

### brute force

```python
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """

        def helper(t):
            if t == 0:
                return 0
            
            a = t.bit_length()
            if 2**a-1 == t:
                return a
            
            x = helper(2**a-1-t) + a + 1
            for m in range(a-1):
                x = min(x, helper(t - 2**(a-1) + 2**m) + a + m + 1)
            return x
        
        
        return helper(target)
```

### dp top-down

```python
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        cache = {0: 0}
        def helper(t):
            if t in cache:
                return cache[t]
             
            a = t.bit_length()
            if 2**a-1 == t:
                cache[t] = a
                return cache[t]
            
            x = helper(2**a-1-t) + a + 1
            for m in range(a-1):
                x = min(x, helper(t - 2**(a-1) + 2**m) + a + m + 1)
            cache[t] = x
            return cache[t]
        
        
        return helper(target)

```

### dp bottom-up

```python
a
```

## refs

* [lc](https://leetcode.com/problems/race-car/)


## schedule

* [x] 2019/12/18
* [x] 2019/12/19
* [ ] 2019/12/22
