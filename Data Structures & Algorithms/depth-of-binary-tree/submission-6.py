# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        que = deque()
        if root:
            que.append(root)
        length = 0
        
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if node.left != None:
                    que.append(node.left)

                if node.right != None:
                    que.append(node.right)

            length += 1

        return length