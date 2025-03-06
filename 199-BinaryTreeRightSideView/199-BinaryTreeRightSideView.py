# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        dq = deque([root])
        res = []

        while dq:
            q_length = len(dq)
            right_view = None
            for i in range(q_length):
                node = dq.popleft()
                if node:
                    right_view = node
                    dq.append(node.left)
                    dq.append(node.right)
            if right_view:
                res.append(right_view.val)        

        return res
              