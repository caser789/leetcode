---
tags: [2019/11/05, data structure/tree, leetcode/437, method/recursion, TODO]
title: Path Sum III
created: '2019-09-07T06:54:48.784Z'
modified: '2019-11-29T01:54:51.171Z'
---

# Path Sum III

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

### Example:

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

## Solution

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        a = count(root, sum)
        b = self.pathSum(root.left, sum)
        c = self.pathSum(root.right, sum)
        return a + b + c

def count(node, s):
    if node is None:
        return 0
    mid = 1 if node.val == s else 0
    left = count(node.left, s - node.val)
    right = count(node.right, s-node.val)
    return mid + left + right
```

### recur 2

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.num_of_path = 0
        self.dfs(root, target)
        return self.num_of_path
    
    def dfs(self, node, target):
        if node is None:
            return
        
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
    
    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.num_of_path += 1
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)
        
```

### with cache

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        
        cache = {0: 1}
        
        def count(node, prefix_sum):
            if node is None:
                return 0
            
            prefix_sum += node.val
            prev = prefix_sum - target
            
            m = cache.get(prev, 0)
            
            cache[prefix_sum] = cache.get(prefix_sum, 0) + 1
            
            a = count(node.left, prefix_sum)
            b = count(node.right, prefix_sum)
            cache[prefix_sum] -= 1
            
            return a + b + m
        
        return count(root, 0)
```

## schedule

* [x] 0 2019/09/09
* [x] 1 2019/09/10
* [x] 1 2019/09/13
* [x] 1 2019/09/20
* [x] 1 2019/10/05
* [ ] 1 2019/11/05

## refs

* [dis](https://leetcode.com/problems/path-sum-iii/discuss/91878/17-ms-O(n)-java-Prefix-sum-method)
* [lc](https://leetcode.com/problems/path-sum-iii/)
* [dis](https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-))
