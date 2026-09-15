# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def checkvalid(node,min,max):
            if(node is None):
                return True
            elif(node.val <= min or node.val >= max):
                return False
            left=checkvalid(node.left,min,node.val)
            right=checkvalid(node.right,node.val,max)
            return left and right
        return checkvalid(root,float("-inf"),float("+inf"))
        