""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

from binary_tree import binary_tree_implementation


def checkBST(root):
    return check_bst_helper(root, float('-inf'), float('inf'))

def check_bst_helper(root, min_val, max_val):
    if root is None:
        return True

    return min_val < root.value < max_val and \
        check_bst_helper(root.left, min_val, root.value) and \
        check_bst_helper(root.right, root.value, max_val)

tree = binary_tree_implementation.Tree()
tree.add(3)
tree.add(4)
tree.add(10)
tree.add(10)  # makes tree as not binary tree
tree.add(8)
tree.add(2)
tree.print_tree()

print(checkBST(tree.root))
