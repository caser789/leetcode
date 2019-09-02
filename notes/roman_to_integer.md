---
tags: [2019/09/02, leetcode/13, TODO]
title: Roman to Integer
created: '2019-08-31T09:05:05.950Z'
modified: '2019-09-02T01:05:52.277Z'
---

# Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

### Example 1:

Input: "III"
Output: 3

### Example 2:

Input: "IV"
Output: 4

### Example 3:

Input: "IX"
Output: 9

### Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

### Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


## Solution

```
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

```

## schedule

* [ ] 0 2019/09/02
* [ ] 1 2019/09/03
* [ ] 3 2019/09/05
* [ ] 7 2019/09/09
* [ ] 15 2019/09/17
* [ ] 13 2019/10/03
* [ ] 13 2019/11/04
