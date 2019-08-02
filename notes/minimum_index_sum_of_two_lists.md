---
tags: [sum]
title: Minimum Index Sum of Two Lists
created: '2019-07-30T15:43:48.074Z'
modified: '2019-08-02T05:35:15.175Z'
---

# Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

### Example 1:

```
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
```

* The only restaurant they both like is "Shogun".

### Example 2:

```
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
```

* The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

> The length of both lists will be in the range of [1, 1000].
> The length of strings in both lists will be in the range of [1, 30].
> The index is starting from 0 to the list length minus 1.
> No duplicates in both lists.

## Solution

```python
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        >>> a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        >>> b = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        >>> Solution().findRestaurant(a, b)
        ['Shogun']
        >>> a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        >>> b = ["KFC", "Shogun", "Burger King"]
        >>> Solution().findRestaurant(a, b)
        ['Shogun']
        """
        s1 = {}
        for i, n in enumerate(list1):
            s1[n] = i

        s2 = {}
        for i, n in enumerate(list2):
            s2[n] = i

        for k, v in s2.items():
            if k not in s1:
                s2.pop(k)
            else:
                s2[k] = v + s1[k]

        k = None
        v = 2000
        for _k, _v in s2.items():
            if _v < v:
                v = _v
                k = _k

        res = []
        for _k, _v in s2.items():
            if _v == v:
                res.append(_k)
        return res
```

```python

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        >>> a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        >>> b = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        >>> Solution().findRestaurant(a, b)
        ['Shogun']
        >>> a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        >>> b = ["KFC", "Shogun", "Burger King"]
        >>> Solution().findRestaurant(a, b)
        ['Shogun']
        """
        s1 = {}
        for i, n in enumerate(list1):
            s1[n] = i

        res = []
        best = 2000
        for i, n in enumerate(list2):
            if n not in s1:
                continue
            if s1[n] + i < best:
                res = [n]
                best = s1[n] + i
            elif s1[n] + i == best:
                res.append(n)
        return res
```
