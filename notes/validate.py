# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        if not root.left and not root.right:
            return True

        if root.left and root.left.val >= root.val:
            return False

        if root.right and root.val >= root.right.val:
            return False

        if not self.isValidBST(root.left):
            return False

        if not self.isValidBST(root.right):
            return False

        return True
