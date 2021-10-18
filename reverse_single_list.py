class solution:
    def reverserlist(self,head):

        pre = None
        cur = head
        suc = None

        while cur != None:
            suc = cur.next
            cur.next = pre
            pre = cur
            cur = suc


        return pre