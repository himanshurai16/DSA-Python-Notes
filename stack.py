#uses of stack in redu undo
#LIFO
class stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    #insert the element
    def push (self,value):
        self.s.insert(0,value)

        #check the top of element
    def peek(self):
        if len(self.s)==0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]

        #delete the element
    def pop(self):
        if len(self.s)==0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop(0)

stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)
print(stk.peek())
print(stk.pop())
print(stk.pop())
