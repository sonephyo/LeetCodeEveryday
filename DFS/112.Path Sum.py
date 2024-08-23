# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        # If the tree is empty i.e. root is NULL, return false...
	    if root is None: return 0
        # If there is only a single root node and the value of root node is equal to the targetSum...
	    if root.val == targetSum and (root.left is None and root.right is None):  return 1
        # Call the same function recursively for left and right subtree...
	    return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)