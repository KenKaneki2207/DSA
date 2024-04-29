class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.insertAtBegin(data)
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        pos = 0
        if index == 0:
            self.insertAtBegin(data)
        else:
            current_node = self.head
            while pos < (index):
                current_node == current_node.next
                pos += 1
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node
            
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, '--->', end='')
            current_node = current_node.next
        print('\n')

    def length_linkedlist(self):
        count = 0
        current_node = self.head
        while current_node:
            current_node = current_node.next
            count+=1
        return count

    def print_leftnode(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    found_node = current_node.prev
                    print('The left node of ', data, 'is :', found_node.data)
                else:
                    print('There is no left node of ', data)
            current_node = current_node.next

    def print_rightnode(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.next:
                    found_node = current_node.next
                    print('The right node of ', data, 'is :', found_node.data)
                else:
                    print('There is no right node of ', data)
            current_node = current_node.next
    
    def print_reverse(self):
        print('The reverse of the linked list :')
        current_node = self.tail
        while current_node:
            print(current_node.data, '--->', end='')
            current_node = current_node.prev
        print('\n')

    def print_mid_index(self):
        length = self.length_linkedlist()
        mid = length // 2
        current_node = self.head
        pointer = 0
        while current_node:
            if pointer == mid:
                print('Middle node is :',current_node.data)
            current_node= current_node.next
            pointer +=1

dll = DoubleLinkedList()
dll.insertAtBegin(10)
dll.insertAtBegin(9)
dll.insertAtEnd(11)
dll.insertAtEnd(15)
# dll.insertAtEnd(19)
dll.insertAtIndex(99,1)
dll.insertAtIndex(991,1)
dll.display()
print('The length of the Linked lIst is :', dll.length_linkedlist())

# head and tail of the linked list
print('The head of the linkd list :',dll.head.data)
print('The tail of the linkd list :',dll.tail.data)

# left_node of the linked list
dll.print_leftnode(10)

# right node of the linked list
dll.print_rightnode(10)

# print reverse
dll.print_reverse()

# print middle node
dll.print_mid_index()

