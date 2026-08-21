# logic of sigly linklist
"""temp = head
    while(temp.next!=None):
        temp = temp.next"""
class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class Singlylinkedlist:
    def __init__(self,head=None):
        self.head = head
        #insertion at end
    def insertatEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next!= None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

            #insertion at the bigining
    def insertatBig(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head =temp

            #insertion at middle

    def insertatMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        while (t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next


            #Deletion  of the element
    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next

        while(t1.next != None):
            if( t1.data ==value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
        if(t1.data == value):
            prev.next = None

    def printLL(self):
        t1 = self.head
        while(t1.next!= None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = Singlylinkedlist()
obj.insertatEnd(10)
obj.insertatEnd(20)
obj.insertatEnd(40)
obj.insertatEnd(30)
obj.insertatBig(5)
obj.insertatMid(7,20)
obj.deleteLL(30)

obj.printLL()





