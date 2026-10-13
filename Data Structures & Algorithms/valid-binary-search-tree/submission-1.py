# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validNode(root, leftBound, rightBound):
            if not root:
                return True

            elif root.val > leftBound and root.val < rightBound:
                left = validNode(root.left, leftBound, root.val)
                right = validNode(root.right, root.val, rightBound)
                return left and right

            else:
                return False

        return validNode(root, float("-inf"), float("inf"))
                
        