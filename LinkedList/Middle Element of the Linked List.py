class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

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


    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next


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

    def display(self):
        current = self.head
        while current:
            print(f"[{current.data}] → ", end="")
            current = current.next
        print("None")

    def middle(self):
        '''

        current = self.head
        length = 0
        while current:
            current = current.next
            length += 1

        mid_index = length // 2
        current = self.head
        for _ in range(mid_index):
            current = current.next

        print(current.data)    This approach will takes O(2n) for finding the length there is optimal solution using fast and slow pointers    '''

        #Slow and Fast pointers

        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)

        '''
        O(n)
        '''

        

ll = SinglyLinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_after_value(20, 25)
ll.insert_at_position(2, 15)
ll.insert_at_beginning(5)
ll.display()
ll.middle()