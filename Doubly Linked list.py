# Doubly and Circular linked list
class Node:
        def __init__(self, value=None):
            self.data = value
            self.next = None
            self.prev = None


class doublyLL:
        def __init__(self):
            self.head = None

        def insertatEnd(self,value):
            temp = Node(value)
            if(self.head == None):
                self.head = temp
                return
            else:
                t = self.head
                while t.next != None:
                    t = t.next

                t.next = temp
                temp.prev = t

                #insertion At biginning

        def insertatBig(self,value):
            temp = Node(value)
            if(self.head == None):
                self.head = temp
                return
            else:
                temp.next = self.head
                self.head.prev = temp
                self.head = temp

            #insertion at middle

        def insertatmid(self,value,x):
            t = self.head
            while(t.next != None):
                if(t.data == x):
                    break
                else:
                    t = t.next
            temp = Node(value)
            temp.next = t.next
            t.next.prev = temp
            t.next = temp
            temp.prev = t

        #deletion At DLL

        def deleteDLL(self,value):
            if (self.head == None):
                print("Linked list is Empty")
                return
            t = self.head
            if(t.data == value):
                self.head = t.next
                self.head.prev = None
                return
            while(t.next != None):
                if(t.data == value):
                    t.prev.next = t.next
                    t.next.prev = t.prev
                    return
                else:
                    t = t.next
            if(t.data == value):
                t.prev.next = None

        def printDLt(self):
            t1 = self.head
            while(t1.next!= None):
                print(t1.data)
                t1 = t1.next
            print(t1.data)

obj = doublyLL()
obj.insertatEnd(10)
obj.insertatEnd(20)
obj.insertatEnd(30)
obj.insertatEnd(40)
obj.insertatBig(5)
obj.insertatmid(50,20)
obj.deleteDLL(40)
obj.printDLt()




