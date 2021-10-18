class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if len(self.items):
            return self.items.pop(0)

    def peek(self):
        if len(self.items):
            return self.items[0].value

class node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class binary_tree():
    def __init__(self , value):
        self.root = node(value)

    def levelorder(self,start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = []

        while len(queue.items) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal



tree = binary_tree(3)

tree.root.left = node(4)
tree.root.left.left = node(6)
tree.root.left.right = node(7)

tree.root.right = node(5)
tree.root.right.left = node(8)
tree.root.right.right = node(9)


print(tree.levelorder(tree.root))