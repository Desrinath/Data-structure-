class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at a specific position (0-based index)
    def insert_at_position(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if not current:
            print("Index out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    # Insert after a given value
    def insert_after_value(self, target_data, new_data):
        current = self.head
        while current:
            if current.data == target_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Value {target_data} not found")

    # Delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next

    # Delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # Delete a node by value
    def delete_by_value(self, target_data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == target_data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == target_data:
                current.next = current.next.next
                return
            current = current.next

        print(f"Value {target_data} not found")

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(f"[{current.data}] → ", end="")
            current = current.next
        print("None")

ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_after_value(20, 25)
ll.insert_at_position(2, 15)
ll.insert_at_beginning(5)
ll.display()  

ll.delete_by_value(15)
ll.delete_from_beginning()
ll.delete_from_end()
ll.display() 