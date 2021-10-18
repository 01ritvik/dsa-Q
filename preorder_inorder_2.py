class treenode:
    def __init__(self,val = 0 , left= None, right = None):
        self.val = val
        self.left = left
        self.right = right

class solution:
    def buildtree(self,preorder,inorder):

        memory = {}

        for index,key in enumerate(inorder):
            memory[key] = index

        root = self.helper(preorder[::-1], inorder, 0, len(inorder), memory)

        return root

    def helper(self, preorder,inorder, leftpointer,rightpointer, memory):

        if leftpointer < rightpointer:
            num = preorder.pop()
            root = treenode(num)
            idx = memory.get(num)

            root.left = self.helper(preorder, inorder, leftpointer, idx, memory)
            root.right = self.helper(preorder, inorder, idx + 1, rightpointer, memory)

            return root
        else:
            return None

