class node:
    def __init__(self,value = None , next = None , prev = None):
        self.value = value
        self.next = next
        self.prev = prev


class linkedlist:
    def __init__(self):
        self.head = None

LL = linkedlist()

n1 = node(3)
n2 = node(5)
n3 = node(7)
n4 = node(9)

LL.head = n1
n1.next = n2
n2.next = n3
n3.next = n4

n2.prev = n1
