class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        def build_tree(preorder_part, inorder_part):

            if len(preorder_part) == 0:
                return None

            root_value = preorder_part[0]
            root_index = inorder_part.index(root_value)

            root = TreeNode(root_value)

            left_inorder = inorder_part[:root_index]
            right_inorder = inorder_part[root_index + 1:]

            left_preorder = preorder_part[1:root_index + 1]
            right_preorder = preorder_part[root_index + 1:]

            root.left = build_tree(left_preorder, left_inorder)
            root.right = build_tree(right_preorder, right_inorder)

            return root

        return build_tree(preorder, inorder)