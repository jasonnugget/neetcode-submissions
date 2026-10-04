# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if root == None:
                return
    
            left = root.left
            right = root.right

            root.left = right
            root.right = left

            traverse(root.left)
            traverse(root.right)
        
        if not root:
            return

        traverse(root)

        return root

        

    
