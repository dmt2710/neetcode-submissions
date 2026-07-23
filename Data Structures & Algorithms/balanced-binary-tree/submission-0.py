# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return [True, 0]
        
        left, right = self.dfs(root.left), self.dfs(root.right)
        if not left[0]:
            return False, -1
        if not right[0]:
            return False, -1
        
        balanced = abs(left[1] - right[1]) <= 1

        return [balanced, 1 + max(left[1], right[1])]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]