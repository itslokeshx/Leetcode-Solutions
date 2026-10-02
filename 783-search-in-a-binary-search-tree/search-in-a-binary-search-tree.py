# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def findnode(node,target):
            queue=deque()
            if(node is None):
                return
            queue.append(node)
            tarnode=None
            while queue:
                removed=queue.popleft()
                if(removed.val == target):
                    tarnode=removed
                if(removed.left):
                    queue.append(removed.left)
                if(removed.right):
                    queue.append(removed.right)
            return tarnode
        return findnode(root,val)
            
            

        