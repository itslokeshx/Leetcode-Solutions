# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        patharray=[]
        path=[]
        def treepath(node):
            if(node is None):
                return 
            path.append(str(node.val))
            if( node.left is None and node.right is None):
                patharray.append("->".join(path))
            else:
                treepath(node.left)
                treepath(node.right)
            path.pop()
        treepath(root)
        return patharray

            
        
