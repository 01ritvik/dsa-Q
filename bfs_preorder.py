class treenode:
    def __init__(self, val = 0 , right = None, left = None):
        self.val = val
        self.right = right
        self.left = left

class solution:
    def bts_preorder(self,preorder):

        root = treenode(preorder[0])

        stack = [root]

        for i in range(1,len(preorder)):
            if preorder[i] < stack[-1].val:
                node = treenode(preorder[i])
                stack[-1].left = node
                stack.append(node)

            else:
                while stack and stack[-1].val < preorder[i]:
                    pop = stack.pop()

                node = treenode(preorder[i])
                pop.right = node
                stack.append(node)

        return root

