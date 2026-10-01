# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def rightview(node):
            queue=deque()
            if(node is None):
                return []
            queue.append(node)
            arr=[]
            while queue:
                level_size=len(queue)
                for _ in range(0,level_size):
                    removed=queue.popleft()
                    if removed.left:
                        queue.append(removed.left)
                    if removed.right:
                        queue.append(removed.right)
                arr.append(removed.val)
            return arr
        return rightview(root)




        