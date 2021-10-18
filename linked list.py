class node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None




class mylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        if index < 0  or index >= self.size:
            return -1

        cur = self.head

        while index != 0:
            cur = cur.next
            index = index -1

        return cur.val

    def addathead(self,val):
        new_node = node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size = self.size + 1

    def addatTail(self,val):
        new_node = node(val)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size = self.size + 1

    def addatIndex(self,index,val):
         if index < 0 or index >= self.size:
             return  -1

         elif index ==0:
             self.addathead(val)

         elif index == self.size:
             self.addatTail(val)

         else:
             cur = self.head
             while index-1 != 0:
                 cur = cur.next
                 index -= 1

             new_node = node(val)

             new_node.next = cur.next
             cur.next.prev = new_node
             cur.next = new_node
             new_node.prev = cur
             self.size = self.size +1


    def deleteatIndex(self,index,val):
        if index < 0 or index >= self.size:
            return -1

        elif index == 0:
            cur = self.head.next
            if cur:
                cur.prev = None

            self.head = self.head.next
            self.size -= 1

            if self.size == 0:
                self.tail = None

        elif index == self.size-1:
            cur = self.tail.prev
            if cur:
                cur.next = None
            self.tail = self.tail.prev
            size -= 1

            if self.size == 0:
                self.head = None

        else:
            cur = self.head
            while index-1 != 0:
                cur = cur.next
                index -= 1
            cur.next = cur.next.next
            cur.next.prev = cur

            self.size -=1
