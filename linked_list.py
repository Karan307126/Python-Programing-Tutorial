class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(f"{temp.data} -> ", end = "")
            temp = temp.next
        print("None")

    def insertAtEnd(self):
        value = int(input("Enter number you have insert at end in linked list : "))
        new_node = Node(value)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while(temp.next):
            temp = temp.next

        temp.next = new_node

    def insertAtStart(self):
        value = int(input("Enter number you have insert at start in linked list : "))
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

    def insertAfterValue(self):
        key = int(input("Enter number after which value to insert : "))
        value = int(input("Enter number you have insert : "))
        new_node = Node(value)
        
        temp = self.head
        while(temp.data != key and temp.next != None):
            temp = temp.next
        
        if temp.data == key:
            new_node.next = temp.next
            temp.next = new_node
        
        else:
            print(f"The {key} is not present in this linked list.")

    def deletionAtStart(self):
        if self.head == None:
            print("Linked list is empty.")
            return
        
        self.head = self.head.next

    def deletionAtEnd(self):
        if self.head == None:
            print("Linked list is empty.")
        
        temp = self.head
        p = self.head.next
        while(p.next and p):
            temp = temp.next
            p = p.next
        
        temp.next = None

    def reverse(self):
        prev_node = None
        curr_node = self.head
        next_node = None
        while(curr_node != None):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        self.head = prev_node
        






l1 = LinkedList()
while True:
    print("*****    LINKED LIST MENU    *****")
    print("\n1. Insert node at start.")
    print("2. Insert node at end.")
    print("3. Insert node after given value.")
    print("4. Delete node at start.")
    print("5. Delete node at end.")
    print("6. Print linkrd list.")
    print("7. Reverse Linked list.")
    print("8. Exit")

    n = int(input("Enter number : "))
    if n == 1:
        l1.insertAtStart()
    elif n == 2:
        l1.insertAtEnd()
    elif n == 3:
        l1.insertAfterValue()
    elif n == 4:
        l1.deletionAtStart()
    elif n == 5:
        l1.deletionAtEnd()
    elif n == 6:
        l1.printList()
    elif n == 7:
        l1.reverse()
    elif n == 8:
        print("*****    Thank you    *****")
        break
    else:
        print("Enter valid number.")