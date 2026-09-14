# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node,t1,t2):
            if(node is None):
                return
            elif(node.val > t1.val and node.val > t2.val):
                left=lca(node.left,t1,t2)
                return left
            elif(node.val < t1.val and node.val < t2.val):
                right=lca(node.right,t1,t2)
                return right
            else:
                return node
        return lca(root,p,q)


        