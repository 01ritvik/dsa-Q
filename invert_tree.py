class treenode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def inverttree(self,root):

        if root is None:
            return None

        root.left , root.right = root.right, root.left

        self.inverttree(root.left)
        self.inverttree(root.right)

        return root
