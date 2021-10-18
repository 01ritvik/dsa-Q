class node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class binary_tree():
    def __init__(self , value):
        self.root = node(value)


    def pre_order(self,start, traversal):

        if start == None:
            return

        traversal.append(start.value)
        self.pre_order(start.left , traversal)
        self.pre_order(start.right , traversal)

        return traversal
    

    def in_order(self,start, traversal):

        if start == None:
            return

        self.in_order(start.left , traversal)
        traversal.append(start.value)
        self.in_order(start.right , traversal)

        return traversal



    def post_order(self,start, traversal):

        if start == None:
            return

        self.post_order(start.left , traversal)
        self.post_order(start.right , traversal)
        traversal.append(start.value)

        return traversal



tree = binary_tree(3)
tree.root.left = node(4)
tree.root.left.left = node(6)
tree.root.left.right = node(7)

tree.root.right = node(5)
tree.root.right.left = node(8)
tree.root.right.right = node(9)

print(tree.pre_order(tree.root , []))
print(tree.in_order(tree.root , []))
print(tree.post_order(tree.root , []))