class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rare = None

    def enqueue(self):
        value = int(input("Enter number you have enqueue in queue : "))
        new_node = Node(value)
        if self.front is None and self.rare is None:
            self.front = new_node
            self.rare = new_node

        else:
            self.rare.next = new_node
            self.rare = new_node
        
        self.rare.next = None

    def dequeue(self):
        if self.front is None:
            print("Queue is Underflow.")

        elif self.front == self.rare:
            print(self.front.data)
            self.front = self.rare = None
        
        else:
            print(self.front.data)
            self.front = self.front.next
        

    def display(self):
        temp = self.front
        while(temp):
            print(f"{temp.data} -> ", end="")
            temp = temp.next
        print("None")


q = Queue()

while(True):
    print("*****    QUEUE MENU    *****")
    print("1. Enqueue element")
    print("2. Dequeue element")
    print("3. Display Queue")
    print("4. Exit")

    n = int(input("Enter number : "))

    if n == 1:
        q.enqueue()
        print("\n\n")
    elif n == 2:
        q.dequeue()
        print("\n\n")
    elif n == 3:
        q.display()
        print("\n\n")
    elif n == 4:
        print("*****    Thank you    *****")
        break
    else:
        print("Enter valid number.")
        print("\n\n")