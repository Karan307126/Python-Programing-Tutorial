class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def display(self):
        temp = self.head
        while(temp.next != self.head):
            print(f"{temp.data} -> ", end = "")
            temp = temp.next
        print(temp.data)

    def insertion(self):
        val = int(input("Enter number you have insert in linked list : "))
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.tail.next = self.head


cl = CLL()
cl.insertion()
cl.insertion()
cl.insertion()
cl.insertion()
cl.insertion()
cl.display()