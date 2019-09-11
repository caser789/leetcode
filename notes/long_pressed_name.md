---
tags: [2019/09/17, application/array/group, leetcode/925, method/2 pointers]
title: Long Pressed Name
created: '2019-08-31T09:15:08.335Z'
modified: '2019-09-10T14:21:47.522Z'
---

# Long Pressed Name

Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

### Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

### Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

### Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true

### Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


## Note:

* name.length <= 1000
* typed.length <= 1000
* The characters of name and typed are lowercase letters.

## Solution

### group

```python
import itertools
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        >>> name = 'saeed'
        >>> typed = 'ssaaedd'
        >>> Solution().isLongPressedName(name, typed)
        True
        """
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]

        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))
```

### 2 pointer

```python
import itertools
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        >>> name = 'saeed'
        >>> typed = 'ssaaedd'
        >>> Solution().isLongPressedName(name, typed)
        True
        """
        j = 0
        for c in name:
            if j == len(typed):
                return False

            if typed[j] != c:
                if j == 0:
                    return False

                if typed[j-1] != typed[j]:
                    return False

                cur = typed[j]
                while j < len(typed) and typed[j] == cur:
                    j += 1

                if j == len(typed) or typed[j] != c:
                    return False
            j += 1
        return True
```

## schedule

* [x] 0 2019/09/03
* [x] 1 2019/09/04
* [x] 1 2019/09/05
* [x] 1 2019/09/06
* [x] 1 2019/09/07
* [x] 1 2019/09/10
* [ ] 1 2019/09/17
