# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        def bstbuilder(prearray,inarray):
            if(len(prearray)==0):
                return
            root=prearray[0]
            index=inarray.index(root)
            rootnode=TreeNode(root)

            left_inorder=inarray[:index]
            right_inorder=inarray[index+1:]

            left_preorder=prearray[1:index+1]
            right_preorder=prearray[index+1:]

            rootnode.left=bstbuilder(left_preorder,left_inorder)
            rootnode.right=bstbuilder(right_preorder,right_inorder)

            return rootnode
        return bstbuilder(preorder,inorder)

        

       





            



        