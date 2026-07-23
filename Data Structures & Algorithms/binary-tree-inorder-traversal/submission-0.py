# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root: Optional[TreeNode], result: List[int]):
        if not root:
            return
        
        self.traversal(root.left, result)
        result.append(root.val)
        self.traversal(root.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traversal(root, result)

        return result

        