# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        def checkcousin(node,x,y):
            queue=deque()
            queue.append(root)

            while queue:
                curlvl=len(queue)
                x_parent=None
                y_parent=None
                for i in range(curlvl):
                    removed=queue.popleft()
                    if removed.left:
                        if removed.left.val == x:
                            x_parent = removed
                        if removed.left.val == y:
                            y_parent = removed
                        queue.append(removed.left)
                    if removed.right:
                        if removed.right.val == x:
                            x_parent = removed
                        if removed.right.val == y:
                            y_parent = removed
                        queue.append(removed.right)
                if x_parent is not None and y_parent is not None:
                    return x_parent != y_parent
                if x_parent is not None or y_parent is not None:
                    return False
        return checkcousin(root,x,y)






        