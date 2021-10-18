class treenode():
    def __init__(self,val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class solution:
    def buildtree(self,preorder,inorder):

        if len(inorder) == 0:
            return None

        if len(preorder) == 1:
            last_node = treenode(preorder[0])
            return last_node

        ind = inorder.index(preorder.pop(0))
        node = treenode(inorder[ind])

        node.left = self.buildtree(preorder , inorder[:ind])
        node.right = self.buildtree(preorder, inorder[ind + 1:])

        return node