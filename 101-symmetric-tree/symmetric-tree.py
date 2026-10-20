# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        def ismirror(node):
            if(node is None):
                return
            queue=deque()
            queue.append((node.left,node.right))
            while queue:
                currlvl=len(queue)
                for _ in range(currlvl):
                    left_node,right_node=queue.popleft()
                    if(left_node is None and right_node is None):
                        continue
                    if(left_node is None and right_node is not None):
                        return False
                    if(left_node is not None and right_node is None):
                        return False
                    if(left_node and right_node):
                        if(left_node.val == right_node.val):
                            queue.append((left_node.left,right_node.right))
                            queue.append((left_node.right,right_node.left))
                        else:
                            return False
            return True

        return ismirror(root)
        