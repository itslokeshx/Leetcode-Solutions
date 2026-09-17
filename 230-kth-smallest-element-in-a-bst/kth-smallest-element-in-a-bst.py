# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count=0
        def findsmall(node,k):
            nonlocal count
            if(node is None):
                return
            left=findsmall(node.left,k)
            count+=1
            if(left is not None):
                return left
            if(count==k):
                return node.val
            right=findsmall(node.right,k)
            if(right is not None):
                return right
        return findsmall(root,k)

            
        