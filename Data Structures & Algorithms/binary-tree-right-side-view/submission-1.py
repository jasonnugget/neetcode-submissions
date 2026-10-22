# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque()
        res = []
        
        queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                if i == size - 1:
                    res.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
        return res
