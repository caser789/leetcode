---
tags: [2019/12/01, application/tree/vertical, data structure/tree, leetcode/1261]
title: Find Elements in a Contaminated Binary Tree
created: '2019-12-01T03:03:34.925Z'
modified: '2019-12-03T14:22:14.852Z'
---

# Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:

root.val == 0
If treeNode.val == x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val == x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

You need to first recover the binary tree and then implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contamined binary tree, you need to recover it first.
bool find(int target) Return if the target value exists in the recovered binary tree.
 

Example 1:

![pic](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4-1.jpg)

Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
Example 2:

![pic](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4.jpg)

Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
Example 3:

![pic](https://assets.leetcode.com/uploads/2019/11/07/untitled-diagram-4-1-1.jpg)

Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:

TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 10^4]
Total calls of find() is between [1, 10^4]
0 <= target <= 10^6

## Solution

### brute force

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if root is None: return
        

        root.val = 0
       
        def dfs(node):
            if node is None:
                return
            
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)
        dfs(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """

        def dfs(node):
            if node is None:
                return False
            
            if node.val > target:
                return False
            
            if node.val == target:
                return True
            
            if dfs(node.left): return True
            if dfs(node.right): return True
            return False
        return dfs(self.root)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
```

### cache

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.seen = set()
        if root is None: return
        

        root.val = 0
       
        def dfs(node):
            if node is None:
                return
            self.seen.add(node.val)
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)
        dfs(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.seen


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
```

### log(n) find

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        
        if root is None: return
        

        root.val = 0
       
        def dfs(node):
            if node is None:
                return
            
            if node.left:
                node.left.val = node.val * 2 + 1
                dfs(node.left)
            
            if node.right:
                node.right.val = node.val * 2 + 2
                dfs(node.right)
        dfs(root)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """    
        root = self.root
        binary = bin(target+1)[3:]
        index = 0
        while root and index <= len(binary):
            if root.val == target:
                return True
            if binary[index] == '0':
                root = root.left
            else:
                root = root.right
            index += 1
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
```

## refs

* [lc](https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/)
