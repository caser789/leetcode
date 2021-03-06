---
favorited: true
tags: [2019/08/17, application/tree/serialization, data structure/tree, leetcode/606, method/traversal/preorder, TODO]
title: Construct String from Binary Tree
created: '2019-08-17T04:40:02.815Z'
modified: '2019-12-01T11:04:35.625Z'
---

# Construct String from Binary Tree

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

### Example 1:

```
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".
```

### Example 2:

```
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
```

## Solution

### recursion

```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ''
        if not t.left and not t.right:
            return '{}'.format(t.val)
        if not t.right:
            return '{}({})'.format(t.val, self.tree2str(t.left))
        return '{}({})({})'.format(t.val, self.tree2str(t.left), self.tree2str(t.right))


_1 = TreeNode(1)
_2 = TreeNode(2)
_3 = TreeNode(3)
_4 = TreeNode(4)

_1.left = _2
_1.right = _3
_2.right = _4

s = Solution().tree2str(_1)
print(s)
assert s == '1(2()(4))(3)'
```

### iter

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ''
        
        stack = [t]
        visited = set()
        s = []
        while stack:
            n = stack[-1]
            if n in visited:
                stack.pop()
                s.append(')')
            else:
                visited.add(n)
                s.append('(')
                s.append(str(n.val))
                if n.left is None and n.right is not None:
                    s.append('()')
                if n.right:
                    stack.append(n.right)
                if n.left:
                    stack.append(n.left)
        
        return ''.join(s[1:-1])
                
```

## TODO

* iter

## refs

* [lc](https://leetcode.com/problems/construct-string-from-binary-tree/)
* [ans](https://leetcode.com/problems/construct-string-from-binary-tree/solution/)
