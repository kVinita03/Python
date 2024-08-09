class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return LinkedList(self.head)
      
    def add_first(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def add_last(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1

    def remove_last(self):
        if self.head:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next != self.tail:
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
            self.size -= 1

    def remove_node(self, index):
        if index < 0 or index >= self.size:
            print("Not Found !!")
            return
        if index == 0:
            self.remove_first()
            return
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next
        if current_node.next == self.tail:
            current_node.next = None
            self.tail = current_node
        else:
            current_node.next = current_node.next.next
        self.size -= 1

    def print_ll(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def __contains__(self, data):
        current_node = self.head
        while current_node is not None and current_node.data != data:
            current_node = current_node.next
        return current_node is not None

llist = LinkedList()

# Add nodes to the linked list
llist.add_first('Nice')
llist.add_last('to')
llist.add_last('meet')
llist.add_last('you')
llist.add_last('.')

# Print the linked list
print("Node : ")
llist.print_ll()

# Remove nodes from the linked list
print("\nRemove First Node :")
llist.remove_first()
llist.print_ll()
print("\nRemove Last Node :")
llist.remove_last()
llist.print_ll()
print("\nRemove Node 1:")
llist.remove_node(1)
llist.print_ll()

print("\nCheck if 'you' is in the linked list:", 'you' in llist)
print("Check if 'Nice' is in the linked list:", 'Nice' in llist)