# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxD = 0

        def backtracking(node, depth):
            if not node:
                return

            self.maxD = max(self.maxD, depth)

            backtracking(node.left, depth + 1)
            backtracking(node.right, depth + 1)
            
        backtracking(root, 1)
        return self.maxD
