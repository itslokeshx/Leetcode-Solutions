# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        maxsum=float("-inf")
        def maxpath(node):
            nonlocal maxsum
            if(node is None):
                return 0
            left=maxpath(node.left)
            right=maxpath(node.right)
            left=max(0,left)
            right=max(0,right)
            maxsum=max(maxsum,node.val+left+right)
            return node.val + max(left,right)
        maxpath(root)
        return maxsum
        
        
            
            
            

            
        