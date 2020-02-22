
def search(root, key):
    if root == None or root.val == key:
        return root

    if root.val<key:
        return search(root.right, key)

    return search(root.left,key)