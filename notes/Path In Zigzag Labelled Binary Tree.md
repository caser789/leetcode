---
tags: [2020/01/01, application/tree/zigzag, data structure/tree, leetcode/1104]
title: Path In Zigzag Labelled Binary Tree
created: '2019-12-01T08:15:55.971Z'
modified: '2019-12-01T12:03:42.590Z'
---

# Path In Zigzag Labelled Binary Tree

In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

![pic](https://assets.leetcode.com/uploads/2019/06/24/tree.png)

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6

## Solution

```
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        res = []
        node_count = 1
        level = 1
        
        # get level
        while label >= node_count*2:
            node_count *= 2
            level += 1
        
        while label != 0:
            res.append(label)
            level_max = 2**level-1
            level_min = 2**(level-1)
            label = int((level_max + level_min - label)/2)
            level -= 1
        
        return res[::-1]
```

## refs

* [lc](https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/)
