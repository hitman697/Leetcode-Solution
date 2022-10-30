class TreeNode(obj):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Sol(obj):
    def insertBST(self, root, val):
        current, parent = root, None
        while current:
            parent = current
            if val <= current.val:
                current = current.left
            else:
                current = current.right
        if not parent:
            root = TreeNode(val)
        elif val <= parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root

