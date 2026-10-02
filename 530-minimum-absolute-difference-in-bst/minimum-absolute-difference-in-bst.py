# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minval=float('inf')
        prev_node=None
        def mindiff(node):
            nonlocal minval,prev_node
            if(node is None):
                return
            left=mindiff(node.left)
            if prev_node is not None:
                minval=min(minval,node.val-prev_node)
            prev_node=node.val
            right=mindiff(node.right)
            return minval
        return mindiff(root)


        