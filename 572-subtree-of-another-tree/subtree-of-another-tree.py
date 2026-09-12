# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag=False
        def compare(node,subRoot):
            nonlocal flag
            if(node is None and subRoot is None):
                return True
            elif(node is None and subRoot is not None):
                return False
            elif(node is not None and subRoot is None):
                return False
            elif(node.val != subRoot.val):
                return False
            left=compare(node.left,subRoot.left)
            right=compare(node.right,subRoot.right)
            if(left ==True and right ==True):
                return True
            else:
                return False

        def duplicate(node):
            nonlocal flag
            if(node is None):
                return False
            left=duplicate(node.left)
            right=duplicate(node.right)
            return compare(node,subRoot) or left or right
        return duplicate(root) 

            

        