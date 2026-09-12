# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare(node, target):
            if node is None and target is None:
                return True
            elif node is None and target is not None:
                return False
            elif node is not None and target is None:
                return False
            elif node.val != target.val:
                return False

            left = compare(node.left, target.left)
            right = compare(node.right, target.right)

            if left == True and right == True:
                return True
            else:
                return False

        def search(node):
            if node is None:
                return False

            left = search(node.left)
            right = search(node.right)

            return compare(node, subRoot) or left or right

        return search(root)
            

        