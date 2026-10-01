class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        def rightview(node):
            queue = deque()
            if node is None:
                return []
            queue.append(node)
            arr = [node.val]
            while queue:
                level_size = len(queue)
                visible = None
                for _ in range(level_size):
                    removed = queue.popleft()
                    if removed.right:
                        visible = removed.right
                    elif removed.left:
                        visible = removed.left
                    if removed.left:
                        queue.append(removed.left)
                    if removed.right:
                        queue.append(removed.right)
                if visible:
                    arr.append(visible.val)
            return arr
        return rightview(root)