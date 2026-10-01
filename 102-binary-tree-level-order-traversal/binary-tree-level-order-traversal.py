# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        def levelorder(node):
            queue=deque()
            levelarr=[]
            if(node is None):
                return []
            levelarr.append([node.val])
            queue.append(node)
            while queue:
                temparr=[]
                level_size=len(queue)
                for _ in range(0,level_size):
                    removed=queue.popleft()
                    if removed.left:
                        queue.append(removed.left)
                        temparr.append(removed.left.val)

                    if removed.right:
                        queue.append(removed.right)
                        temparr.append(removed.right.val)
                if(temparr):
                    levelarr.append(temparr)
            return levelarr
        return levelorder(root)
            
                    



        
        