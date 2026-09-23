# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        def check_cousins(root, x, y):
            queue = deque()
            queue.append(root)
            while queue:
                level_size = len(queue)
                x_parent = None
                y_parent = None

                for _ in range(level_size):
                    current = queue.popleft()

                    if current.left:
                        if current.left.val == x:
                            x_parent = current
                        if current.left.val == y:
                            y_parent = current
                        queue.append(current.left)
                    if current.right:
                        if current.right.val == x:
                            x_parent = current
                        if current.right.val == y:
                            y_parent = current
                        queue.append(current.right)
                if x_parent is not None and y_parent is not None:
                    return x_parent != y_parent
                if x_parent is not None or y_parent is not None:
                    return False
            return False
        return check_cousins(root, x, y)
   