class Node():
    def __init__(self,value):
        self.value = value
        self.adjecent_list = []
        self.visited = False

class graph():

    def BFS(self,node):
        queue = []
        queue.append(node)
        node.visited = True

        traversal = []

        while queue:
            actualnode = queue.pop(0)
            traversal.append(actualnode.value)

            for i in actualnode.adjecent_list:
                if i.visited is False:
                    queue.append(i)
                    i.visited = True

        return traversal

    def DFS(self,node,trav):
        node.visited = True
        trav.append(node.value)

        for element in node.adjecent_list:
            if element.visited is False:
                self.DFS(element, trav)

        return trav


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")

node1.adjecent_list.append(node2)
node1.adjecent_list.append(node3)
node1.adjecent_list.append(node4)

node2.adjecent_list.append(node5)
node2.adjecent_list.append(node6)

node4.adjecent_list.append(node7)


Graph = graph()
print(Graph.DFS(node1,[]))