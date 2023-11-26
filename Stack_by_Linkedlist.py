class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        value = int(input("Enter number you have push in stack : "))
        new_node = Node(value)
        
        if self.top is None:
            self.top = new_node
            return
        
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top == None:
            print("STACK UNDERFLOW!")
            return
        
        temp = self.top.data
        self.top = self.top.next
        return temp


s = Stack()
while(True):
    print("*****    STACK MENU    *****")
    print("1. push element.")
    print("2. pop element.")
    print("3. exit.")
    val = int(input("Enter Number : "))
    if val == 1:
        s.push()
    elif val == 2:
        num = s.pop()
        print(f"The poped value is {num}.")
    elif val == 3:
        print("*****    Thank you   *****")
        break
    else:
        print("Enter Valid Number, Pleas.")