---
tags: [2019/09/05, application/array/status, leetcode/443]
title: String Compression
created: '2019-08-31T09:25:29.121Z'
modified: '2019-09-04T14:14:03.558Z'
---

# String Compression

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


## Follow up:

Could you solve it using only O(1) extra space?


### Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


### Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.


### Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.


## Note:

All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.

## Solution

```python
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        n = len(chars)
        v = None
        cnt = 0
        j = 0
        while j < n:
            if v is None:
                cnt = 1
                v = chars[j]
            elif chars[j] == v:
                cnt += 1
            else:
                if i < n:
                    chars[i] = v
                    i += 1
                if i < n and 10 >cnt > 1:
                    chars[i] = str(cnt)
                    i += 1
                elif i < n and cnt > 9:
                    for c in str(cnt):
                        chars[i] = c
                        i += 1
                v = chars[j]
                cnt = 1
            j += 1

        if i < n:
            chars[i] = v
            i += 1
        if i < n and 10 > cnt > 1:
            chars[i] = str(cnt)
            i += 1
        elif i < n and cnt > 9:
            for c in str(cnt):
                chars[i] = c
                i += 1

        return i
```

## schedule

* [x] 0 2019/09/04
* [ ] 1 2019/09/05
