class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        pos = 0
        if pos == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and pos+1 != index):
                pos = pos + 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index Not Found")

    def insertAtEnd(self, data):
        current_node = self.head
        new_node = Node(data)
        while(current_node.next):
            current_node = current_node.next        
        current_node.next = new_node

    def deleteAtBegin(self):
        if (self.head == None):
            return
        self.head = self.head.next

    def deleteAtEnd(self):
        current_node = self.head
        while (current_node.next.next != None):
            current_node = current_node.next
        current_node.next = None

    def deleteAtIndex(self, index):
        pos = 0
        current_node = self.head
        if pos == 0:
            self.deleteAtBegin()
            return
        while (pos+1 != index):
            pos += 1
            current_node = current_node.next
        current_node.next = current_node.next.next

    def printll(self):
        current_node = self.head
        while(current_node):
            print(current_node.data,end="-->")
            current_node = current_node.next
        
    def length(self):
        current_node = self.head
        count = 1
        while(current_node.next != None):
            count += 1
            current_node = current_node.next
        print("\nLength of the Linked List is :", count)

List = linkedlist()
List.insertAtBegin('a')
List.insertAtBegin('b')
List.insertAtBegin('c')
List.insertAtEnd('d')
List.insertAtIndex('e',1)
# List.deleteAtIndex(0)
List.printll()
List.length()